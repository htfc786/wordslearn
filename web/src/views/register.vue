<template>
  <div id="app">
    <h1 id="page-title">注册</h1>
    <hr>
    <div id="page-title">
      用户名：<input v-model="username" type="text" name="username" />  
      <br/>  
      密码：<input v-model="password" type="password" name="password" />  
      <br/>
      确认密码：<input v-model="confirm" type="password" name="confirm"/>  
      <br/>  
      {{ info }}
      <input @click="register()" type="submit" value="注册" />
      <br/>  
      <span>已有账号？<router-link :to="{ name: 'login' }">登录</router-link></span>
    </div>
    <hr>
  </div>
</template>

<script>
import API from '@/network/API';
export default {
  data() {  //数据
    return {
      username: "",
      password: "",
      confirm: "",
      info: ""
    }
  },
  mounted: function () {  // 打开页面时执行

  },
  methods:{ // 方法
    register: function () {
      let that = this
      API.user.register(this.username, this.password, this.confirm)
        .then(res => {
          that.info = "注册成功，即将登录 ";
          setTimeout(() => {
            this.$router.push({ name:"login" });
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
  #app {
    background: #fff;
    margin: 0 auto;
    padding: 10px;
  }
  #page-title {
    text-align: center;
  }
</style>
