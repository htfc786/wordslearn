// https://blog.csdn.net/saienenen/article/details/115030205
import axios from 'axios'

import CONF from '@/config'

const service = axios.create({
  baseURL: CONF.API_BASE_URL, // api的base_url
  timeout: 15000 // 请求超时时间
  // .... 其他信息
})

//响应拦截器
service.interceptors.response.use(
	function(response) {
		//....
		return response
	},
	function(error) {
		return Promise.reject(error)
	}
)

//请求拦截器 
service.interceptors.request.use(
	function(config) {
		//...
		//配置token的添加
		if (localStorage.getItem("token") != null) {
			config.headers.token = localStorage.getItem("token")
		}
		
		//...
		return config
	},
	function(error) {
		return Promise.reject(error)
	}
)

// 封装请求方法
export function request(query) {
	return service
		.request(query)
		.then((res) => {
			if (res.data?.data?.type === "login") {
				//登录信息存储
				localStorage.setItem('token', res.data.data.token);
				localStorage.setItem('userid', res.data.data.userid);
				localStorage.setItem('username', res.data.data.username);

				return Promise.resolve(res.data)
			} else if (res.data.status === 401) {
				vue.prototype.$$router.push({ path: '/login' })
				return Promise.reject(res)
			} else if (res.data.status === 500) {
				return Promise.reject(res)
			} else if (res.data.status === 400) {
				return Promise.reject(res)
			} else {
				return Promise.resolve(res.data)
			}
		})
		//对错误进行处理
		.catch((e) => {
			return Promise.reject(e)
		})
}

//post请求  ----> json格式的post请求 
export function post(url, params) {
	return request({
		url: url,
		method: 'post',
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

//post请求
export function form(url, params, onUploadProgress) {
	return request({
		url: url,
		method: 'post',
		data: params,
		headers: {
			'Content-Type': 'multipart/form-data',
		},
		onUploadProgress: onUploadProgress,
	})
}
