<template>
  <div class="top">
    <el-icon @click="this.$router.go(-1)"><ArrowLeftBold /></el-icon>
  </div>
  <div class="main">
    <h1>默写模式选择</h1>
    <el-form
      label-position="right"
      label-width="70px"
    >
      <el-form-item label="范围">
        <el-select
          v-model="b"
          placeholder="请选择一个范围">
          <el-option value="1">1a</el-option>
          <el-option value="2">2s</el-option>
          <el-option value="3">3d</el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="数量">
        <el-select
          v-model="a"
          filterable
          allow-create
          default-first-option
          placeholder="请选择一个分组或输入一个分类"
        >
          <el-option value="5"></el-option>
          <el-option value="10"></el-option>
          <el-option value="15"></el-option>
          <el-option value="20"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="顺序选择">
        <el-radio-group 
          v-model="a">
          <el-radio-button label="asc">顺序模式</el-radio-button>
          <el-radio-button label="desc">倒序模式</el-radio-button>
          <el-radio-button label="random">随机模式</el-radio-button>
        </el-radio-group>
      </el-form-item>
      <el-form-item label="默写模式">
        <el-radio-group
          v-model="a">
          <el-radio-button label="single">听读音听写模式</el-radio-button>
          <el-radio-button label="multiple">中文听写模式</el-radio-button>
          <el-radio-button label="file">听读音打字模式</el-radio-button>
          <el-radio-button label="file">中文打字模式</el-radio-button>
        </el-radio-group>
      </el-form-item>
      
      <el-button type="danger">开始</el-button>
      <el-button type="success">一键错词表</el-button>
      <el-button @click="this.$router.go(-1)">返回首页</el-button>
    </el-form>
  </div>
</template>

<script>
export default {
  name: 'dictation_select',
  data(){
    return{
      a:1,
      b:0,
    }
  }
}
</script>

<style scoped>
  .top {
    position: fixed;
    height: 38px;
    width: 100%;
    max-width: 400px;
    top: 0;
    border-bottom: #E4E7ED 2px solid;
  }
  .top > .el-icon {
    position: absolute;
    left: 10px;
    height: 40px;
  }
  .main {
    margin-top: 40px;
  }
  .main > h1 {
    text-align: center;
  }
  .main > .el-form {
    padding: 20px;
  }
  .main > .el-form > .el-button {
    width: 100%;
    margin: 8px;
  }
</style>