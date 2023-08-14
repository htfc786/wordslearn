<template>
  <el-container>
    <WordsadminHeader
      title="单词管理"
      :router_to="{
        name: 'wordsadmin_group',
        params: { bookid: bookid ? bookid : 0 },
      }"
      :bookname="bookname"
      :groupname="groupname"
    />
    <el-main>
      <div class="tools-bar">
        <el-button
          type="primary"
          @click="
            $router.push({
              name: 'wordsadmin_word_add',
              params: { groupid: groupid },
            })
          "
        >
          添加单词
        </el-button>
      </div>
      <el-skeleton v-if="!wordsData" animated />
      <el-result
        v-else-if="wordsData && !hasWordsData"
        icon="error"
        title="您请求的内容不存在！"
        sub-title="请检查请求内容是否正确"
      >
        <template #extra>
          <el-button type="primary" @click="$router.push({ name: 'index' })"
            >返回首页</el-button
          >
        </template>
      </el-result>
      <el-table
        v-else-if="wordsData"
        :data="wordsData"
        :row-class-name="wordRowColor"
        border
      >
        <el-table-column type="index" />
        <el-table-column prop="id" label="id" width="48px" />
        <el-table-column prop="word" label="单词" />
        <el-table-column
          prop="type"
          :formatter="formatWordType"
          label="类型"
          width="53px"
        />
        <el-table-column prop="pronounce" label="音标" />
        <el-table-column prop="chinese" label="中文" />
        <el-table-column prop="note" label="备注" />
      </el-table>
    </el-main>
  </el-container>
</template>

<script>
import API from '@/network/API'
import WordsadminHeader from '@/components/wordsadmin_header.vue'

export default {
  name: 'wordsadmin_word',
  data() {
    //数据
    return {
      bookid: null,
      bookname: '',
      groupid: null,
      groupname: '',
      wordsData: null, // list
      hasWordsData: true,
    }
  },
  components: { WordsadminHeader },
  mounted: function () {
    this.groupid = this.$route.params.groupid

    this.getGroupInfo()
    this.getWord()
  },
  computed: {},
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
      API.wordsadmin.words
        .get(this.groupid)
        .then((e) => {
          that.wordsData = e.data
        })
        .catch((e) => {
          if (e.msg === '没有当前分组！') {
            that.wordsData = []
            that.hasWordsData = false
          }
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
    wordRowColor({ row, rowIndex }) {
      if (!row.type) {
        return 'phrase-row'
      }
      return ''
    },
    formatWordType(row, column, cellValue, index) {
      return cellValue ? '单词' : '词组'
    },
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
.el-result,
.el-skeleton,
.el-table {
  width: 100%;
  height: calc(100vh - 60px - 20px * 2 - 40px - 5px);
}
.el-table .phrase-row {
  --el-table-tr-bg-color: var(--el-color-primary-light-9);
}
</style>
