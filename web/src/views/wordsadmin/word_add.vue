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
          <el-form-item>
            <el-button type="primary" @click="addWord()"
              >添加</el-button
            >
            <el-button @click="$refs.wordForm.resetFields()">重置</el-button>
          </el-form-item>
        </el-form>
        <!--批量添加-->
        <el-form
          ref="batchForm"
          class="batchForm"
          :model="wordForm"
          size="small"
        >
          <h1 class="from-text-1">批量添加</h1>
          <el-input
            v-model="wordForm.note"
            type="textarea"
            :autosize="{ minRows: 4, maxRows: 12 }"
          />
          <el-form-item>
            <el-button type="primary" @click="addWord()"
              >添加</el-button
            >
            <el-button @click="$refs.wordForm.resetFields()">重置</el-button>
          </el-form-item>
        </el-form>
      </div>
    </el-main>
  </el-container>
</template>

<script>
import { ElMessage } from 'element-plus'
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
      hasWordsData: true,
      wordForm: {
        word: '', // 单词
        pronounce: '', // 音标
        chinese: '', // 中文
        note: '', // 备注
        type: 1, // 单词类型 1-单词 0-词组
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
    }
  },
  components: { WordsadminHeader },
  mounted: function () {
    this.groupid =  this.$route.params.groupid

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
          that.hasWordsData = false;
        })
    },
    addWord() {
      const that = this
      this.$refs.wordForm.validate((valid, fields) => {
        if (valid) {
          API.wordsadmin.words.add(
            that.groupid,
            that.wordForm.word,
            that.wordForm.pronounce,
            that.wordForm.chinese,
            that.wordForm.note,
            that.wordForm.type,
          )
            .then(e=>{
              ElMessage.success('添加成功');
              that.$refs.wordForm.resetFields()
              
            })
        } else {
          ElMessage.error(fields);
        }
      });
      
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
  padding: 30px 40px 0 40px;
  max-width: 500px;
  margin: 0 auto;
}
.batchForm .from-text-1 {
  display: block;
  margin: 0px 0 20px 40px;
  font-size: 30px;
}
.batchForm .el-form-item {
  margin-top: 18px;
  margin-left: 60px;
}
</style>
