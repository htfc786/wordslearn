<template>
  <el-container>
    <WordsadminHeader
      title="添加单词"
      :router_to="{
        name: 'wordsadmin_word',
        params: { groupid: groupid ? groupid : 0 },
      }"
      :bookname="bookname"
      :groupname="groupname"
    />
    <el-main>
      <div class="tools-bar">

      </div>
    </el-main>
  </el-container>
</template>

<script>
import API from '@/network/API'
import WordsadminHeader from '@/components/wordsadmin_header.vue'

export default {
  name: 'wordsadmin_word_add',
  data() {
    //数据
    return {
      bookid: null,
      bookname: '',
      groupid: null,
      groupname: '',
      wordsData: null, // list
    }
  },
  components: { WordsadminHeader },
  mounted: function () {

  },
  methods: {
  
  },
}
</script>

<style>
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
.el-skeleton,
.el-table {
  width: 100%;
  height: calc(100vh - 60px - 20px * 2 - 40px - 5px);
}
</style>
