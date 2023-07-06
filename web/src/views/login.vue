<template>
  <div id="app">
    <h1 id="page-title">登录</h1>
    <hr>
    <div id="page-title">
      用户名：<input v-model="username" type="text" name="username" />  
      <br/>  
      密码：<input v-model="password" type="password" name="password" />  
      <br/>
      {{ info }}
      <input @click="login()" type="submit" value="登录" />
      <br/>  
      <span>没有账号？<router-link :to="{ name: 'register' }">注册</router-link></span>
    </div>
    <hr>
  </div>
</template>

<script>
import API from '@/network/API';
export default {
  data() {
    return {
      username: "",
      password: "",
      info: ""
    }
  },
  mounted: function () {  // 打开页面时执行
    
  },
  methods:{ // 方法
    login: function () {
      let that = this
      API.user.login(this.username, this.password)
        .then(res => {
          that.info = "登陆成功，即将跳转。。。";
          setTimeout(() => {
            this.$router.push({ name:"index" });
          }, 3000)
        })
        .catch(res => {
          that.info = res.data.msg;
        });
    }
  },
}
</script>

<style scoped>
  body {
    background: #f3f3f3;
  }
  #app {
    background: #fff;
    margin: 0 auto;
    padding: 10px;
  }
  #page-title {
    text-align: center;
  }
</style>
