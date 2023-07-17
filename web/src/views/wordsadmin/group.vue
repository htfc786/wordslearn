<template>
  <el-container>
    <el-header class="header">
      <router-link :to="{ name: 'wordsadmin_book' }">
        <el-link :underline="false"><el-icon :size="25"><Back /></el-icon></el-link>
      </router-link>
      <span>分组管理</span>
    </el-header>
    <el-main>
      <div class="tools-bar">
        <el-button type="primary" @click="addGroup_open()">添加分组</el-button>
      </div>
      <el-table :data="groupsData" border>
        <el-table-column prop="groupid" label="id" />
        <el-table-column prop="name" label="分组名" />
        <el-table-column prop="description" label="描述" />
        <el-table-column fixed="right" label="操作">
          <template #default="scope">
            <el-button @click="editGroup_open(scope.row.groupid,scope.row.name,scope.row.description,scope.row.cover)" size="small">编辑</el-button>
            <el-button @click="delGroup(scope.row.groupid)" type="danger" size="small">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
    </el-main>
  </el-container>

  <el-dialog v-model="addGroup.show" :title="addGroup.title">
    <el-form>
      <el-form-item label="组名">
        <el-input v-model="addGroup.name" placeholder="请输入组名" ></el-input>
      </el-form-item>
      <el-form-item label="描述">
        <el-input v-model="addGroup.description" :autosize="{ minRows: 4 }" type="textarea" placeholder="请输入描述 不可大于255字 可空" height="40px" ></el-input>
      </el-form-item>
    </el-form>
    <template #footer>
      <span class="dialog-footer">
        <el-button @click="addGroup.show = false">关闭</el-button>
        <el-button type="primary" @click="addGroup_close()">完成</el-button>
      </span>
    </template>
  </el-dialog>
</template>

<script>
import API from '@/network/API';
export default {
  name: 'wordsadmin_groups',
  data() {  //数据
    return {
      bookid: NaN,
      groupsData: [],
      addGroup: {
        show: false,
        title: "添加组",
        type: "add",
        bookid: 0,
        groupid: 0,
        name: "",
        description: "",
      }
    }
  },
  mounted: function () {
    this.bookid = this.$route.params.bookid;

    this.getGroup()
  },
  methods: {
    getGroup(){
      const that = this;
      API.wordsadmin.groups.get(this.bookid)
        .then(e=>{
          that.groupsData = e.data;
        })
    },
    addGroup_open(){
      this.addGroup.show = true;

      this.addGroup.title = "添加组";
      this.addGroup.type = "add";
      this.addGroup.bookid = 0;
      this.addGroup.groupid = 0;
      this.addGroup.name = "";
      this.addGroup.description = "";
    },
    addGroup_close(){
      if(this.addGroup.type=="edit"){
        this.editGroup_close();
        return;
      }

      this.addGroup.show = false;

      const that = this;
      API.wordsadmin.groups.add(this.bookid, this.addGroup.name, this.addGroup.description)
        .then((e)=>{
          that.$message.success(e.msg);
          
          that.getGroup()
        })
        .catch(e=>{
          that.$message.error(e.msg);
        })
    },
    delGroup(groupid){
      const that = this;
      API.wordsadmin.groups.del(groupid)
        .then((e)=>{
          that.$message.success(e.msg);
          
          that.getGroup()
        })
        .catch(e=>{
          that.$message.error(e.msg);
        })
    },
    editGroup_open(groupid, name, description){
      this.addGroup.show = true;

      this.addGroup.title = "编辑组";
      this.addGroup.type = "edit";
      this.addGroup.groupid = groupid;
      this.addGroup.name = name;
      this.addGroup.description = description;
    },
    editGroup_close(){
      this.addGroup.show = false;

      const that = this;
      API.wordsadmin.groups.edit(this.addGroup.groupid,this.addGroup.name, this.addGroup.description, this.addGroup.cover)
        .then((e)=>{
          that.$message.success(e.msg);
          
          that.getGroup()
        })
        .catch(e=>{
          that.$message.error(e.msg);
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
    border-bottom: #E4E7ED 2px solid;
    z-index: 10;
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
    height: calc(100vh - 60px - 20px*2 - 40px - 5px);
  }
</style>