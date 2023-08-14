<template>
  <el-container>
    <WordsadminHeader
      title="分组管理"
      :router_to="{ name: 'wordsadmin_book' }"
      :bookname="bookname"
    />
    <el-main>
      <div class="tools-bar">
        <el-button type="primary" @click="addGroup_open()">添加分组</el-button>
      </div>
      <el-skeleton v-if="!groupsData" animated />
      <el-result
        v-else-if="groupsData && !hasGroupsData"
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
      <el-table v-else-if="groupsData" :data="groupsData" border>
        <el-table-column prop="groupid" label="id" />
        <el-table-column prop="name" label="分组名" />
        <el-table-column fixed="right" label="操作">
          <template #default="scope">
            <el-button
              @click="editGroup_open(scope.row.groupid, scope.row.name)"
              size="small"
              >编辑</el-button
            >
            <el-button
              @click="delGroup(scope.row.groupid, scope.row.name)"
              type="danger"
              size="small"
              >删除</el-button
            >
            <el-button
              @click="inGroup(scope.row.groupid)"
              type="success"
              size="small"
              >进入</el-button
            >
          </template>
        </el-table-column>
      </el-table>
    </el-main>
  </el-container>

  <el-dialog v-model="addGroup.show" :title="addGroup.title">
    <el-form>
      <el-form-item label="组名">
        <el-input v-model="addGroup.name" placeholder="请输入组名" />
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
import API from '@/network/API'
import WordsadminHeader from '@/components/wordsadmin_header.vue'

export default {
  name: 'wordsadmin_groups',
  data() {
    //数据
    return {
      bookid: null,
      bookname: '',
      groupsData: null, // list
      hasGroupsData: true,
      addGroup: {
        show: false,
        title: '添加组',
        type: 'add',
        bookid: 0,
        groupid: 0,
        name: '',
      },
    }
  },
  components: { WordsadminHeader },
  mounted: function () {
    this.bookid = this.$route.params.bookid

    this.getBookname()
    this.getGroup()
  },
  methods: {
    getBookname() {
      const that = this
      API.wordsadmin.books.info(this.bookid)
        .then((e) => {
          that.bookname = e.data.name
        })
    },
    getGroup() {
      const that = this
      API.wordsadmin.groups.get(this.bookid)
        .then((e) => {
          that.groupsData = e.data
        })
        .catch((e) => {
          if (e.msg == "查询没有当前书！") {
            that.groupsData = [];
            that.hasGroupsData = false;  
          }
        })
    },
    addGroup_open() {
      this.addGroup.show = true

      this.addGroup.title = '添加组'
      this.addGroup.type = 'add'
      this.addGroup.bookid = 0
      this.addGroup.groupid = 0
      this.addGroup.name = ''
    },
    addGroup_close() {
      if (this.addGroup.type == 'edit') {
        this.editGroup_close()
        return
      }

      this.addGroup.show = false

      const that = this
      API.wordsadmin.groups
        .add(this.bookid, this.addGroup.name)
        .then((e) => {
          that.$message.success(e.msg)

          that.getGroup()
        })
        .catch((e) => {
          that.$message.error(e.msg)
        })
    },
    delGroup(groupid, groupname) {
      const that = this
      this.$messageBox
        .confirm('确定要删除 ' + groupname + ' 吗？', '删除操作', {
          confirmButtonText: '删除',
          cancelButtonText: '取消',
          type: 'warning',
        })
        .then(() => {
          API.wordsadmin.groups
            .del(groupid)
            .then((e) => {
              that.$message.success(e.msg)

              that.getGroup()
            })
            .catch((e) => {
              that.$message.error(e.msg)
            })
        })
    },
    editGroup_open(groupid, name) {
      this.addGroup.show = true

      this.addGroup.title = '编辑组'
      this.addGroup.type = 'edit'
      this.addGroup.groupid = groupid
      this.addGroup.name = name
    },
    editGroup_close() {
      this.addGroup.show = false

      const that = this
      API.wordsadmin.groups
        .edit(this.addGroup.groupid, this.addGroup.name)
        .then((e) => {
          that.$message.success(e.msg)

          that.getGroup()
        })
        .catch((e) => {
          that.$message.error(e.msg)
        })
    },
    inGroup(groupid) {
      this.$router.push({
        name: 'wordsadmin_word',
        params: {
          groupid: groupid,
        },
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
.el-result,
.el-skeleton,
.el-table {
  width: 100%;
  height: calc(100vh - 60px - 20px * 2 - 40px - 5px);
}
</style>
