<template>
  <el-container>
    <el-header>
      <el-link :underline="false"><el-icon :size="25"><Back /></el-icon></el-link>
      <span>单词表</span>
    </el-header>
    <el-main>
      <div class="tools-bar">
        <el-select v-model="value" placeholder="请选择分类">
          <el-option
            v-for="item in options"
            :key="item.value"
            :label="item.label"
            :value="item.value"
          />
        </el-select>
        
        <el-button type="primary" @click="dialogFormVisible = true">Primary</el-button>
      </div>
      <el-table :data="tableData" border style="width: 100%">
        <el-table-column prop="date" label="Date" width="180" />
        <el-table-column prop="name" label="Name" width="180" />
        <el-table-column prop="address" label="Address" />
      </el-table>


    </el-main>
  </el-container>

  <el-dialog v-model="dialogFormVisible" title="Shipping address">
    <el-form :model="form">
      <el-form-item label="Promotion name" :label-width="formLabelWidth">
        <el-input v-model="tableData[5].name" autocomplete="off" />
      </el-form-item>
      <el-form-item label="Zones" :label-width="formLabelWidth">
        <el-select v-model="tableData[5].address" placeholder="Please select a zone">
          <el-option label="Zone No.1" value="shanghai" />
          <el-option label="Zone No.2" value="beijing" />
        </el-select>
      </el-form-item>
    </el-form>
    <template #footer>
      <span class="dialog-footer">
        <el-button @click="dialogFormVisible = false">Cancel</el-button>
        <el-button type="primary" @click="dialogFormVisible = false">
          Confirm
        </el-button>
      </span>
    </template>
  </el-dialog>
</template>

<script>
export default {
  name: 'vocabulary',
  data() {  //数据
    return {
      username: "",
      access_token: "",
      albums: [],
      dialogFormVisible: false,

      tableData: [
        {
          date: '2016-05-03',
          name: 'Tom',
          address: 'No. 189, Grove St, Los Angeles',
        },
        {
          date: '2016-05-02',
          name: 'Tom',
          address: 'No. 189, Grove St, Los Angeles',
        },
        {
          date: '2016-05-04',
          name: 'Tom',
          address: 'No. 189, Grove St, Los Angeles',
        },
        { date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },{ date: '2016-05-01', name: 'Tom', address: 'No. 189, Grove St, Los Angeles', },
      ],
    }
  },
}
</script>

<style>
  .el-container {
    background-color: #f2f2f2;
  }
  .el-header {
    background-color: #fff;
  }
  .el-header > span{
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
  .tools-bar > .el-select {
    margin: 4px;
  }
  .tools-bar > .el-button {
    margin: 4px;
    float: right;
  }
</style>