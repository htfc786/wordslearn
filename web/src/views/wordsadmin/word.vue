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
        <el-button type="danger" @click="delCheckWord()">删除所单词</el-button>
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
        @selection-change="wordDataCheck"
      >
        <el-table-column type="selection" width="40"/>
        <el-table-column type="index" />
        <!-- <el-table-column prop="id" label="id" width="48px" /> -->
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
        <el-table-column fixed="right" label="操作">
          <template #default="scope">
            <el-button
              @click="editWord_open(scope.row.id)"
              size="small"
              >编辑</el-button
            >
            <el-button
              @click="delWord(scope.row.id, scope.row.word)"
              type="danger"
              size="small"
              >删除</el-button
            >
          </template>
        </el-table-column>
      </el-table>
    </el-main>
  </el-container>

  <el-dialog v-model="addWord.show" :title="addWord.title">
    <el-form
      ref="addWord"
      class="addWord"
      :model="addWord"
      :rules="addWordRules"
      label-width="100px"
    >
      <el-form-item label="单词" prop="word">
        <el-input v-model="addWord.word" />
      </el-form-item>
      <el-form-item label="音标" prop="pronounce">
        <el-input v-model="addWord.pronounce" />
      </el-form-item>
      <el-form-item label="中文" prop="chinese">
        <el-input v-model="addWord.chinese" type="textarea" autosize />
      </el-form-item>
      <el-form-item label="备注" prop="note">
        <el-input
          v-model="addWord.note"
          type="textarea"
          :autosize="{ minRows: 2 }"
        />
      </el-form-item>
      <el-form-item label="单词类型" prop="type">
        <el-radio-group v-model="addWord.type">
          <el-radio-button :label="true" border>单词</el-radio-button>
          <el-radio-button :label="false" border>词组</el-radio-button>
        </el-radio-group>
      </el-form-item>
    </el-form>
    <template #footer>
      <span class="dialog-footer">
        <el-button @click="addWord.show = false">关闭</el-button>
        <el-button @click="$refs.addWord.resetFields()">重置</el-button>
        <el-button type="primary" @click="editWord_close()">完成</el-button>
      </span>
    </template>
  </el-dialog>
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
      addWord: {
        show: false,
        title: '添加组',
        type: 'add',
        groupid: 0,
        wordid: 0,
        word: '', // 单词
        pronounce: '', // 音标
        chinese: '', // 中文
        note: '', // 备注
        type: 1, // 单词类型 1-单词 0-词组
      },
      addWordRules: {
        word: [
          { required: true, message: '单词不能为空', trigger: 'blur' },
          { min: 1, max: 64, message: '请输入正确的单词', trigger: 'blur' },
        ],
        pronounce: [
          { max: 64, message: '音标过长！最多64个字符', trigger: 'blur' },
        ],
        chinese: [
          { max: 128, message: '中文过长！最多128个字符', trigger: 'blur' },
        ],
        note: [
          { max: 255, message: '备注过长！最多255个字符', trigger: 'blur' },
        ],
        type: [
          { required: true, message: '请选择单词类型', trigger: 'change' },
        ],
      },
      checkIdList: [],
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
    delWord(wordid, word) {
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
    editWord_open(wordid) {
      this.addWord.show = true
      this.addWord.title = '编辑单词'
      this.addWord.type = 'edit'

      this.addWord.wordid = wordid

      const wordsDataRes = this.wordsData.find((currentValue)=>{
        return currentValue.id == wordid;
      })
      console.log(wordsDataRes)
      this.addWord.word = wordsDataRes.word
      this.addWord.pronounce = wordsDataRes.pronounce
      this.addWord.chinese = wordsDataRes.chinese
      this.addWord.note = wordsDataRes.note
      this.addWord.type = wordsDataRes.type
    },
    editWord_close() {
      this.addWord.show = false

      const that = this
      this.$refs.addWord.validate((valid, fields) => {
        if (valid) {
          API.wordsadmin.words
            .edit(
              that.addWord.wordid, 
              that.addWord.word,
              that.addWord.pronounce,
              that.addWord.chinese,
              that.addWord.note,
              that.addWord.type,
            )
            .then((e) => {
              that.$message.success(e.msg)

              that.getWord()
            })
            .catch((e) => {
              that.$message.error(e.msg)
            })
        } else {
          Object.values(fields).forEach((item, index) => {
            item.forEach((item, index) => {
              that.$message.error(item.message)
            })
          })
        }
      })
    },
    wordDataCheck(val) {
      var checklist = [];
      for (var i = 0; i < val.length; i++) {
        checklist.push(val[i].id);
      }
      this.checkIdList = checklist;
    },
    delCheckWord(){
      if (!this.checkIdList.length){
        this.$message.error('请选择单词！');
        return;
      }
      const that = this
      this.$messageBox.confirm('确定要删除所选的 '+this.checkIdList.length+' 个单词吗？', '批量删除', { confirmButtonText: '删除', cancelButtonText: '取消', type: 'warning' })
        .then(async () => {
          for(var i=0;i<that.checkIdList.length;i++){
            var wordid = that.checkIdList[i]

            const wordsDataRes = this.wordsData.find((currentValue)=>{
              return currentValue.id == wordid;
            })
            var msgHead = '';
            if (wordsDataRes) {
              msgHead = wordsDataRes.word + ': ';
            }

            const res = await API.wordsadmin.words.del(wordid)
            if (res.code == 200) {
              that.$message.success(msgHead + res.msg)
            } else {
              that.$message.error(msgHead + res.msg)
            }
          }

          that.$message.success('批量删除完成！');
          that.getWord()
          that.checkIdList = []
        })
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
