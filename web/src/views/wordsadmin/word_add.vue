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
      <div class="tools-bar"></div>
      <el-result
        v-if="!hasWordsData"
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
      <div class="main-body">
        <!--单个添加-->
        <el-form
          ref="wordForm"
          class="wordForm"
          :model="wordForm"
          :rules="wordFormRules"
          label-width="100px"
          size="small"
        >
          <h1 class="from-text-1">单个添加</h1>
          <el-form-item label="单词" prop="word">
            <el-input v-model="wordForm.word" />
          </el-form-item>
          <el-form-item label="音标" prop="pronounce">
            <el-input v-model="wordForm.pronounce" />
          </el-form-item>
          <el-form-item label="中文" prop="chinese">
            <el-input v-model="wordForm.chinese" type="textarea" autosize />
          </el-form-item>
          <el-form-item label="备注" prop="note">
            <el-input
              v-model="wordForm.note"
              type="textarea"
              :autosize="{ minRows: 2 }"
            />
          </el-form-item>
          <el-form-item label="单词类型" prop="type">
            <el-radio-group v-model="wordForm.type">
              <el-radio-button :label="1" border>单词</el-radio-button>
              <el-radio-button :label="0" border>词组</el-radio-button>
            </el-radio-group>
          </el-form-item>
          <el-form-item label="音频id" prop="sound_id">
            <el-input v-model="wordForm.sound_id" />
          </el-form-item>
          <el-form-item label="音频起始" prop="sound_start">
            <el-input v-model="wordForm.sound_start" />
          </el-form-item>
          <el-form-item label="音频结束" prop="sound_end">
            <el-input v-model="wordForm.sound_end" />
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="oneAddWord()">添加</el-button>
            <el-button @click="$refs.wordForm.resetFields()">重置</el-button>
          </el-form-item>
        </el-form>
        <!--批量添加-->
        <el-form
          ref="batchForm"
          class="batchForm"
          :model="batchWordFrom"
          size="small"
        >
          <h1 class="from-text-1">批量添加</h1>
          <el-form-item>
            <el-input
              v-model="batchWordFrom.batchText"
              type="textarea"
              :autosize="{ minRows: 4, maxRows: 12 }"
            />
          </el-form-item>
          <el-form-item class="btn">
            <el-button type="primary" @click="batchAddWord()">添加</el-button>
            <el-button @click="batchWordFrom.batchText = ''">重置</el-button>
            <el-button @click="showbatchWord = true">详细信息</el-button>
          </el-form-item>
        </el-form>
      </div>
    </el-main>

    <el-dialog v-model="showbatchWord" title="添加信息">
      <!-- 感谢：程序员小山与Bug https://github.com/sunzsh/vue-el-demo/blob/master/src/views/table-scroll-tr.vue -->
      <el-table
        ref="batchWordTable"
        :data="batchWordTableData"
        height="300"
        border
        :row-class-name="({ row }) => (row.loading ? 'is-loading-row' : '')"
      >
        <el-table-column prop="ind" label="序号" align="center" width="80">
          <template #default="scope">
            <el-icon v-if="scope.row.status === 'success'" style="color: green"
              ><Check
            /></el-icon>
            <el-tooltip
              v-else-if="scope.row.status === 'error'"
              effect="dark"
              :content="scope.row.errormsg"
              placement="right"
            >
              <el-icon style="color: red"><CircleCloseFilled /></el-icon>
            </el-tooltip>
            <el-icon v-else-if="scope.row.loading"><Loading /></el-icon>
            <span v-else>{{ scope.$index + 1 }}</span>
            <i class="el-icon-loading"></i>
          </template>
        </el-table-column>
        <el-table-column prop="word" label="单词" />
        <el-table-column prop="type" label="类型" />
        <el-table-column prop="pronounce" label="音标" />
        <el-table-column prop="chinese" label="中文" />
        <el-table-column prop="note" label="备注" />
        <el-table-column prop="sound_id" label="音频id" />
        <el-table-column prop="sound_start" label="音频起始" />
        <el-table-column prop="sound_end" label="音频结束" />
      </el-table>
      <template #footer>
        <span class="dialog-footer"> </span>
      </template>
    </el-dialog>
  </el-container>
</template>

<script>
import { ElMessage } from 'element-plus'
import API from '@/network/API'
import WordsadminHeader from '@/components/wordsadmin_header.vue'
import elTableScrollToRow from '@/components/elTableScrollToRow.js'

export default {
  name: 'wordsadmin_word_add',
  data() {
    //数据
    return {
      bookid: null,
      bookname: '',
      groupid: null,
      groupname: '',
      hasWordsData: true,
      wordForm: {
        word: '', // 单词
        pronounce: '', // 音标
        chinese: '', // 中文
        note: '', // 备注
        type: 1, // 单词类型 1-单词 0-词组
        sound_id: '', // 音频id
        sound_start: '', // 音频起始
        sound_end: '', // 音频结束
      },
      wordFormRules: {
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
      batchWordFrom: {
        batchText: '',
      },
      showbatchWord: false,
      batchWordTableData: [],
    }
  },
  components: { WordsadminHeader },
  mounted: function () {
    this.groupid = this.$route.params.groupid

    this.getGroupInfo()
  },
  methods: {
    getGroupInfo() {
      const that = this
      API.wordsadmin.groups
        .info(this.groupid)
        .then((e) => {
          that.groupname = e.data.group
          that.bookid = e.data.book.bookid
          that.bookname = e.data.book.name
        })
        .catch((e) => {
          that.hasWordsData = false
        })
    },
    async addWord() {
      const that = this
      return new Promise((resolve, reject) => {
        this.$refs.wordForm.validate((valid, fields) => {
          if (valid) {
            API.wordsadmin.words
              .add(
                that.groupid,
                that.wordForm.word,
                that.wordForm.pronounce,
                that.wordForm.chinese,
                that.wordForm.note,
                that.wordForm.type,
                that.wordForm.sound_id,
                that.wordForm.sound_start,
                that.wordForm.sound_end
              )
              .then((e) => {
                // ElMessage.success(e.msg)
                resolve({ word: that.wordForm.word, message: e.msg })
                that.$refs.wordForm.resetFields()
              })
          } else {
            Object.values(fields).forEach((item, index) => {
              item.forEach((item, index) => {
                // ElMessage.error(msgHead + item.message)
                reject({ word: that.wordForm.word, message: item.message })
              })
            })
          }
        })
      })
    },
    oneAddWord() {
      this.addWord()
        .then(({ word, message }) => {
          var msgHead = word + (word ? ': ' : '')
          ElMessage.success(msgHead + message)
        })
        .catch(({ word, message }) => {
          var msgHead = word + (word ? ': ' : '')
          ElMessage.error(msgHead + message)
        })
    },
    async batchAddWord() {
      var wordDataList = this.batchWordFrom.batchText.split('\n')
      wordDataList.forEach((item, index) => {
        if (!item) {
          wordDataList.splice(index, 1)
        }
      })

      // 处理wordData数据
      var wordData = [] //最终数据
      for (var i = 0; i < wordDataList.length; i++) {
        var wordDataListRow = wordDataList[i]
        if (!wordDataListRow) {
          continue
        } //空字符串

        //csv格式 没有空着
        // 单词,类型(1-单词\0-词组),音标,中文,备注,音频id,音频起始,音频结束
        var readDataList = wordDataListRow.split(',')
        // 处理""问题
        var dataList = []
        var textBuffer = '',
          saveTextBuffer = false
        readDataList.forEach((item, index) => {
          if (saveTextBuffer) {
            textBuffer += item
          }
          if (item.indexOf('"') === 0) {
            textBuffer += item
            saveTextBuffer = true
          } else if (item.indexOf('"') !== -1) {
            saveTextBuffer = false
            dataList.push(textBuffer.slice(0, textBuffer.length - 1).slice(1))
          } else {
            dataList.push(item)
          }
        })

        if (dataList.length !== 8) {
          //数据格式错误
          wordData.push({ error: '行：' + wordDataListRow + ' 数据格式错误' })
          continue
        }
        //音频id,音频起始,音频结束 暂未涉及 ###
        wordData.push({
          word: dataList[0], // 单词
          type: parseInt(dataList[1], 10), // 单词类型 1-单词 0-词组
          pronounce: dataList[2], // 音标
          chinese: dataList[3], // 中文
          note: dataList[4], // 备注
          sound_id: dataList[5], // 音频id
          sound_start: dataList[6], // 起始
          sound_end: dataList[7], // 结束
        })
      }
      // 放batchWordTableData里
      const that = this
      this.batchWordTableData = []
      wordData.forEach((item, index) => {
        if (item.error) {
          this.batchWordTableData.push({
            word: '',
            type: '',
            pronounce: '',
            chinese: '',
            note: '',
            sound_id: '',
            sound_start: '',
            sound_end: '',
            status: 'error',
            loading: false,
            errormsg: item.error,
          })
          return
        }
        this.batchWordTableData.push({
          word: item.word,
          type: item.type,
          pronounce: item.pronounce,
          chinese: item.chinese,
          note: item.note,
          sound_id: item.sound_id,
          sound_start: item.sound_start,
          sound_end: item.sound_end,

          loading: false,
          status: '',
        })
      })
      //显示窗口
      this.showbatchWord = true

      //开始添加
      for (var i = 0; i < this.batchWordTableData.length; i++) {
        var item = this.batchWordTableData[i]

        item.loading = true
        // 滚动到这一行
        if (this.$refs.batchWordTable) {
          elTableScrollToRow(this.$refs.batchWordTable, item)
        }

        if (item.errormsg) {
          item.loading = false
          continue
        }
        // 赋值
        this.wordForm.word = item.word
        this.wordForm.pronounce = item.pronounce
        this.wordForm.chinese = item.chinese
        this.wordForm.note = item.note
        this.wordForm.type = item.type
        this.wordForm.sound_id = item.sound_id
        this.wordForm.sound_start = item.sound_start
        this.wordForm.sound_end = item.sound_end

        //添加
        await this.addWord()
          .then(({ word, message }) => {
            item.status = 'success'
            item.loading = false
          })
          .catch(({ word, message }) => {
            var msgHead = word + (word ? ': ' : '')

            ElMessage.error(msgHead + message)
            item.errormsg = message
            item.status = 'error'
            item.loading = false
          })
      }
      ElMessage.success('数据添加成功！具体请见详情信息')
      this.batchWordFrom.batchText = ''
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
.el-result {
  width: 100%;
  height: calc(100vh - 60px - 20px * 2 - 40px - 5px);
}
.main-body {
  width: 100%;
  height: calc(100vh - 60px - 20px * 2 - 40px - 5px);
  background: white;
  overflow: auto;
}
.el-form {
  border: 1px solid var(--el-border-color);
}
.wordForm {
  padding: 30px 40px 0 0;
  max-width: 500px;
  margin: 0 auto;
}
.wordForm .from-text-1 {
  display: block;
  margin: 0px 0 20px 80px;
  font-size: 30px;
}
.batchForm {
  padding: 30px 20px 0 20px;
  max-width: 500px;
  margin: 0 auto;
}
.batchForm .from-text-1 {
  display: block;
  margin: 0px 0 20px 60px;
  font-size: 30px;
}
.batchForm .btn {
  margin-top: 18px;
  margin-left: 80px;
}
.el-dialog {
  --el-dialog-width: 80%;
  --el-dialog-margin-top: 10vh;
}
</style>
