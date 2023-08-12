<template>
  <el-container>
    <el-header class="header">
      <router-link
        :to="{ name: 'wordsadmin_group', params: { bookid: bookid ? bookid : 0 } }"
      >
        <el-link :underline="false"
          ><el-icon :size="25"><Back /></el-icon
        ></el-link>
      </router-link>
      <span>单词管理</span>
      <div class="bookname">
        <span>{{ bookname }}</span> <span>{{ groupname }}</span>
      </div>
    </el-header>
    <el-main>
      <div class="tools-bar">
        <el-button type="primary" @click="$router.push({ name: 'wordsadmin_word_add', params: {groupid: groupid} });">添加单词</el-button>
      </div>
      <el-table :data="wordsData" border>
        <el-table-column prop="wordid" label="id" />
        <el-table-column prop="name" label="分组名" />
      </el-table>
    </el-main>
  </el-container>
</template>

<script>
import API from '@/network/API'
export default {
  name: 'wordsadmin_word',
  data() {
    //数据
    return {
      bookid: null,
      bookname: '',
      groupid: null,
      groupname: '',
      wordsData: [],
    }
  },
  mounted: function () {
    this.groupid = this.$route.params.groupid

    this.getGroupInfo()
    this.getWord()
  },
  methods: {
    getGroupInfo() {
      const that = this
      API.wordsadmin.groups.info(this.groupid).then((e) => {
        that.groupname = e.data.group
        that.bookid = e.data.book.bookid
        that.bookname = e.data.book.name
      })
    },
    getWord() {
      const that = this
      API.wordsadmin.words.get(this.groupid).then((e) => {
        that.wordsData = e.data
      })
    },
    delWord(wordid, wordname) {
      const that = this
      this.$messageBox
        .confirm('确定要删除 ' + word + ' 吗？', '删除操作', {
          confirmButtonText: '删除',
          cancelButtonText: '取消',
          type: 'warning',
        })
        .then(() => {
          API.wordsadmin.words
            .del(wordid)
            .then((e) => {
              that.$message.success(e.msg)

              that.getWord()
            })
            .catch((e) => {
              that.$message.error(e.msg)
            })
        })
    },
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
.tools-bar {
  height: 40px;
  background-color: #fff;
  margin-bottom: 5px;
}
.el-main {
  margin-top: 60px;
}
.tools-bar > .el-select {
  margin: 4px;
}
.tools-bar > .el-button {
  margin: 4px;
  float: right;
}
.el-table {
  width: 100%;
  height: calc(100vh - 60px - 20px * 2 - 40px - 5px);
}
</style>
