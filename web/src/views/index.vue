<template>
  <div class="header">
    <div class="face"> <!-- 头像 -->
      <el-icon><User /></el-icon>
    </div>
    <div class="relation">
      <span class="name">{{ view.username }}</span>
      <div class="uid"><span>uid: {{ view.uid }}</span></div>
      <span class="content"></span> <!--个性签名 留空-->
    </div>
  </div>
  <div class="main">
    <div class="item">
      <div><el-icon><Headset /></el-icon></div>
      <span>听单词</span>
    </div>
    <router-link :to="{ name: 'dictation_select' }" class="item">
      <div><el-icon><EditPen /></el-icon></div>
      <span>默单词</span>
    </router-link>
    <div class="item">
      <div><el-icon><Collection /></el-icon></div>
      <span>错词本</span>
    </div>
  </div>
  <div class="list">
    <div class="item">
      <span>单词表管理</span>
      <el-icon><ArrowRightBold /></el-icon>
    </div>
    <div class="item">
      <span>默写历史</span>
      <el-icon><ArrowRightBold /></el-icon>
    </div>
    
  </div>
</template>

<script>
import API from '@/network/API';
export default {
  name: 'index',
  data() {
    return {
      view: {
        username: "(请先登录)",
        uid: 0,
      },
    }
  },
  mounted: function () {
    this.init_user_info()
  },
  methods: {
    init_user_info(){
      var that = this
      API.user.info()
        .then(res=>{
          localStorage.setItem("userid", res.data.userid)
          localStorage.setItem("username", res.data.username)
          that.view.uid = res.data.userid;
          that.view.username = res.data.username;
        })
    },
  },
}
</script>

<style scoped>
  .header{
    padding: 8px;
    background-color: #E6E8EB;
    cursor: context-menu;
  }
  .header > .face{
    width: 100px;
    height: 100px;
    border-radius: 50%;
    background: #fff;
    display: inline-block;
    margin: 0 16px 0 0
  }
  .header > .face > .el-icon{
    width: 100%;
    height: 100%;
  }
  .header > .face > .el-icon svg{
    height: 80%;
    width: 80%;
    padding: 10px;
  }
  .header > .relation{
    height: 75px;
    display: inline-block;
    vertical-align: top;
    margin-top: 25px;
  }
  .header > .relation > .name{
    font-size: 20px;
    color: #212121;
    max-width: 190px;
    vertical-align: middle;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    display: inline-block;
  }
  .header > .relation > .uid{
    clear: both;
  }
  .header > .relation > .uid span{
    display: inline-block;
    font-size: 8px;
    padding: 2px 3.5px;
    color: #505050;
    background: #f4f4f4;
    transform: scale(.71);
    transform-origin: left;
  }
  .header > .relation > .content{
    max-width: 210px;
    margin-top: 5px;
    font-size: 8px;
    color: #666;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    float: left;
  }
  .main {
    --item-size: 80px;
    display: flex;
    justify-content: space-evenly;
    height: var(--item-size);
    margin: 12px 0;
    cursor: context-menu;
  }
  .main > .item {
    width: var(--item-size);
    height: var(--item-size);
    color: black;
    cursor: context-menu;
    text-decoration: auto;
  }
  .main > .item > div {
    --icon-size: calc(var(--item-size) * 3 / 5);
    width: var(--icon-size);
    height: var(--icon-size);
    margin: 0 auto;
    border-radius: calc(var(--icon-size) / 2);
    background-color: #F0F2F5; /* 颜色 */
    position: relative;
  }
  .main > .item > div > .el-icon,
  .main > .item > div > .el-icon > svg {
    width: calc(var(--icon-size) * 4 / 5);
    height: calc(var(--icon-size) * 4 / 5);
    display: block;
    position: absolute;
    top: calc((var(--icon-size) - var(--icon-size) * 4 / 5) / 2 / 2);
    right: calc((var(--icon-size) - var(--icon-size) * 4 / 5) / 2 / 2);
  }
  .main > .item > span {
    height: calc(var(--item-size) * 2 / 5);
    display: block;
    text-align: center;
    line-height: calc(var(--item-size) * 2 / 5);
    font-size: 18px;
  }
  .list {
    cursor: context-menu;
    --item-height: 50px;
  }
  .list > .item {
    height: var(--item-height);
    border-top: #DCDFE6 solid 1px;
    border-bottom: #DCDFE5 solid 1px;
    position: relative;
  }
  .list > .item > span {
    height: var(--item-height);
    display: inline-block;
    text-align: center;
    line-height: var(--item-height);
    font-size: calc(var(--item-height) * 2 / 5);
    margin-left: 10px;
  }
  .list > .item > .el-icon {
    position: absolute;
    right: 10px;
    height: var(--item-height);
  }
</style>