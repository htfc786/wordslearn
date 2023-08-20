<template>
  <el-container>
    <WordsadminHeader title="音频管理" :router_to="{ name: 'index' }" />
    <el-main>
      <div class="tools-bar">
        <el-button type="primary" @click="addSound.show = true">添加音频</el-button>
      </div>
      <el-skeleton v-if="!soundsData" animated />
      <el-table v-else-if="soundsData" :data="soundsData" border>
        <el-table-column prop="soundid" label="id" />
        <el-table-column prop="name" label="音频名" />
        <el-table-column fixed="right" label="操作" width="80px">
          <template #default="scope">
            <el-button
              @click="delSound(scope.row.soundid, scope.row.name)"
              type="danger"
              size="small"
              >删除</el-button
            >
          </template>
        </el-table-column>
      </el-table>
    </el-main>
  </el-container>

  <el-dialog v-model="addSound.show" title="添加音频">
    <el-form label-width="68px">
      <el-form-item label="音频名">
        <el-input v-model="addSound.name" placeholder="请输入音频名"></el-input>
      </el-form-item>
      <el-form-item label="音频文件">
        <input ref="soundUpload" id="uploadFiles" type="file" accept=".mp3,.wav,.ogg,.bmp,.acc,.webm" />
      </el-form-item>
    </el-form>
    <template #footer>
      <span class="dialog-footer">
        <el-button @click="addSound.show = false">关闭</el-button>
        <el-button type="primary" @click="addSound_close()">完成</el-button>
      </span>
    </template>
  </el-dialog>
  <UploadPercent :show="percent.show" :percent="percent.percent" />
</template>

<script>
import API from '@/network/API'
import WordsadminHeader from '@/components/wordsadmin_header.vue'
import UploadPercent from '@/components/uploadPercent.vue'

export default {
  name: 'wordsadmin_sound',
  data() {
    //数据
    return {
      soundsData: null, // list
      addSound: {
        show: false,
        name: '',
      },
      percent: {
        show: false,
        percent: 0,
      },
    }
  },
  components: { WordsadminHeader, UploadPercent },
  mounted: function () {
    this.getSound()
  },
  methods: {
    getSound() {
      const that = this
      API.wordsadmin.sounds.get().then((e) => {
        that.soundsData = e.data
      })
    },
    addSound_close() {
      const name = this.addSound.name
      const uploadFiles = this.$refs.soundUpload;

      if (!uploadFiles.files[0]) {
        this.$message.error("请选择文件！")
        return;
      }

      this.addSound.show = false
      this.percent.show = true;

      const that = this;
      API.wordsadmin.sounds
        .add(
          name, 
          uploadFiles.files[0],
          function(percent){ //进度条更新
            that.percent.percent = percent
          },
          function(e){ //成功请求
            that.percent.show = false;
            console.log(e)
            that.$message.success(e.msg)
            that.getSound();
          },
          function(e){ //失败请求
            that.percent.show = false;
            console.log(e)
            that.$message.error(e.msg)
          },
        )
    },
    delSound(soundid, soundname) {
      const that = this
      this.$messageBox
        .confirm('确定要删除 ' + soundname + ' 吗？', '删除操作', {
          confirmButtonText: '删除',
          cancelButtonText: '取消',
          type: 'warning',
        })
        .then(() => {
          API.wordsadmin.sounds
            .del(soundid)
            .then((e) => {
              that.$message.success(e.msg)

              that.getSound()
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
