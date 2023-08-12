<template>
  <el-header class="header">
    <router-link :to="{ name: 'index' }">
      <el-link :underline="false"
        ><el-icon :size="25"><Back /></el-icon
      ></el-link>
    </router-link>
    <span>{{ title }}</span>
    <div class="bookname">
      <span v-if="bookname">{{ bookname }}</span>
      <span v-if="groupname">{{ groupname }}</span>
    </div>
  </el-header>
</template>

<script>
export default {
  props: {
    title: { type: String, required: true }, //标题
    router_to: { type: Object, required: true }, // router-link跳转
    bookname: { type: String }, // 书名称
    groupname: { type: String }, // 组名称
  },
}
</script>

<style>
.el-container {
  background-color: #f2f2f2;
}
.el-header {
  background-color: #fff;
  position: fixed;
  height: 58px;
  width: 100%;
  top: 0;
  border-bottom: #e4e7ed 2px solid;
  z-index: 10;
}
.el-header > span {
  display: inline-block;
  vertical-align: middle;
  font-size: 1.5em;
  font-weight: bold;
  margin: 0.86rem;
}
.el-header > .bookname {
  display: inline-block;
  clear: both;
}
.el-header > .bookname span {
  display: inline-block;
  font-size: 8px;
  padding: 2px;
  color: #505050;
  background: #f4f4f4;
}
</style>
