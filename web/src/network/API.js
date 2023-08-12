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
      info: function(bookid){
        return get("/wordsadmin/book/info", {
          bookid: bookid
        })
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
    groups: {
      get: function(bookid){
        return get("/wordsadmin/group", {
          bookid: bookid,
        })
      },
      info: function(groupid){
        return get("/wordsadmin/group/info", {
          groupid: groupid
        })
      },
      add: function(bookid, name){
        return post("/wordsadmin/group/add", {
          bookid: bookid,
          name: name,
        })
      },
      del: function(groupid){
        return post("/wordsadmin/group/del", {
          groupid: groupid,
        })
      },
      edit: function(groupid, name){
        return post("/wordsadmin/group/edit", {
          groupid: groupid,
          name: name,
        })
      },
    },
    words: {
      get: function(groupid){
        return get("/wordsadmin/word", {
          groupid: groupid,
        })
      },
      add: function(bookid, name){
        return post("/wordsadmin/word/add", {
          bookid: bookid,
          name: name,
        })
      },
      del: function(wodrid){
        return post("/wordsadmin/word/del", {
          wodrid: wodrid,
        })
      },
      edit: function(groupid, name){
        return post("/wordsadmin/word/edit", {
          groupid: groupid,
          name: name,
        })
      },
    },
  },
}