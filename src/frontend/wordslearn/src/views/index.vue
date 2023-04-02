<template>
  <div id="header">
    <div class="face"> <!-- 头像 -->
      <el-icon><User /></el-icon>
    </div>
    <div class="relation">
      <span class="name">htfc786</span>
      <div class="uid"><span>uid:626519554</span></div>
      <span class="content">这个人很神秘，什么都没写。。。 </span>
    </div>
  </div>
</template>

<script>
export default {
  name: 'index',
}
</script>

<style scoped>
  #header{
    padding: 8px;
    background-color: #dedede;
  }
  #header > .face{
    width: 100px;
    height: 100px;
    border-radius: 50%;
    background: #fff;
    display: inline-block;
    margin: 0 16px 0 0
  }
  #header > .face > .el-icon{
    width: 100%;
    height: 100%;
  }
  #header > .face > .el-icon svg{
    height: 80%;
    width: 80%;
    padding: 10px;
  }
  #header > .relation{
    height: 75px;
    display: inline-block;
    vertical-align: top;
    margin-top: 25px;
  }
  #header > .relation > .name{
    font-size: 20px;
    color: #212121;
    max-width: 190px;
    vertical-align: middle;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    display: inline-block;
  }
  #header > .relation > .uid{
    clear: both;
  }
  #header > .relation > .uid span{
    display: inline-block;
    font-size: 8px;
    padding: 2px 3.5px;
    color: #505050;
    background: #f4f4f4;
    transform: scale(.71);
    transform-origin: left;
  }#header > .relation > .content{
    max-width: 210px;
    margin-top: 5px;
    font-size: 8px;
    color: #666;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    float: left;
  }
  

    
</style>