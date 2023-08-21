// https://blog.csdn.net/saienenen/article/details/115030205
import axios from 'axios'
import { ElMessage } from 'element-plus'

import CONF from '@/config'

const service = axios.create({
  baseURL: CONF.API_BASE_URL, // api的base_url
  // timeout: 15000 // 请求超时时间
  // .... 其他信息
})

//响应拦截器
service.interceptors.response.use(
  function (response) {
    //....
    return response
  },
  function (error) {
    return Promise.reject(error)
  }
)

//请求拦截器
service.interceptors.request.use(
  function (config) {
    //...
    //配置token的添加
    if (localStorage.getItem('access_token') != null) {
      config.headers.Authorization = localStorage.getItem('access_token')
    }

    //...
    return config
  },
  function (error) {
    return Promise.reject(error)
  }
)

//未登录
function nologin() {
  ElMessage.error('需要登录！')
  localStorage.removeItem('access_token')
  localStorage.removeItem('userid')
  localStorage.removeItem('username')
  window.location.href = '/login'
}

// 封装请求方法
export function request(query) {
  return (
    service
      .request(query)
      .then((res) => {
        if (res.data.code === 401) {
          return Promise.reject(res)
        } else if (res.data.code === 500) {
          return Promise.reject(res)
        } else if (res.data.code === 400) {
          return Promise.reject(res)
        } else {
          return Promise.resolve(res.data)
        }
      })
      //对错误进行处理
      .catch((e) => {
        if (e.status === 200) {
          if (e.data.code === 401) {
            nologin()
            return Promise.reject(e.data)
          } else if (e.data.code === 500) {
            return Promise.reject(e.data)
          } else if (e.data.code === 400) {
            return Promise.reject(e.data)
          }
        } else if (e.code === 'ERR_NETWORK') {
          ElMessage.error('网络错误！接口请求超时')
          return Promise.reject(e)
        } else if (e.code === 'ECONNABORTED') {
          ElMessage.error('服务异常请稍后重试 ' + e.message)
          return Promise.reject(e)
        } else if (
          e.code === 'ERR_BAD_RESPONSE' ||
          e.code === 'ERR_BAD_REQUEST'
        ) {
          if (e.response.status === 401) {
            nologin()
            return Promise.reject(e)
          } else if (e.response.status === 422) {
            nologin()
            return Promise.reject(e)
          } else {
            ElMessage.error('请求接口发生错误：' + e.response.status)
            return Promise.reject(e)
          }
        } else {
          ElMessage.error(e.message)
          return Promise.reject(e)
        }
      })
  )
}

//post请求
export function post(url, params) {
  return request({
    url: url,
    method: 'post',
    headers: {
      'Content-Type': 'multipart/form-data',
    },
    data: params,
  })
}

//Get请求
export function get(url, params) {
  return request({
    url: url,
    method: 'get',
    params: params,
  })
}

//post请求 文件上传
export function uploadFile(url, params, onProgress, onFinish, onError) {
  const req = request({
    url: url,
    method: 'post',
    data: params,
    headers: {
      'Content-Type': 'multipart/form-data',
    },
    onUploadProgress: (e) => {
      const percent = Math.floor((e.loaded / e.total) * 100)
      onProgress(percent)
    },
  })
    .then((e) => {
      onFinish(e)
    })
    .catch((e) => {
      if (!axios.isCancel(e)) {
        onError(e)
      }
    })

  return function () {
    //停止请求用
    request.cancel()
  }
}
