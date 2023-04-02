import { post,form } from '@/network/request'

export default {
  
  user:{
    // 登录
    login: function(username, password){
      return post("/user/login", {
        username: username,
        password: password,
      })
    },
    // 注册
    register: function(username, password, confirm){
      return post("/user/register", {
        username: username,
        password: password,
        confirm: confirm,
      })
    },
  },
}