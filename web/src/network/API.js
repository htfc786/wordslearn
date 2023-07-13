import { post,get,form } from '@/network/request'

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
    // 获取用户信息
    info: function(){
      return get("/user/info", {})
    },
  },
  wordsadmin: {
    books: {
      get: function(){
        return get("/wordsadmin/book", {})
      },
      add: function(name, description, cover){
        return post("/wordsadmin/book/add", {
          name: name,
          description: description,
          cover: cover,
        })
      },
      del: function(bookid){
        return post("/wordsadmin/book/del", {
          bookid: bookid,
        })
      },
      edit: function(bookid, name, description, cover){
        return post("/wordsadmin/book/edit", {
          bookid: bookid,
          name: name,
          description: description,
          cover: cover,
        })
      },
    },
  },
}