<template>
  <el-container>
    <el-header class="header">
      <router-link :to="{ name: 'index' }">
        <el-link :underline="false"
          ><el-icon :size="25"><Back /></el-icon
        ></el-link>
      </router-link>
      <span>书籍管理</span>
    </el-header>
    <el-main>
      <div class="tools-bar">
        <el-button type="primary" @click="addBook_open()">添加书籍</el-button>
      </div>
      <el-table :data="booksData" border>
        <el-table-column prop="bookid" label="id" />
        <el-table-column prop="name" label="书名" />
        <el-table-column prop="description" label="描述" />
        <el-table-column fixed="right" label="操作">
          <template #default="scope">
            <el-button
              @click="
                editBook_open(
                  scope.row.bookid,
                  scope.row.name,
                  scope.row.description,
                  scope.row.cover
                )
              "
              size="small"
              >编辑</el-button
            >
            <el-button
              @click="delBook(scope.row.bookid, scope.row.name)"
              type="danger"
              size="small"
              >删除</el-button
            >
            <el-button
              @click="inBook(scope.row.bookid)"
              type="success"
              size="small"
              >进入</el-button
            >
          </template>
        </el-table-column>
      </el-table>
    </el-main>
  </el-container>

  <el-dialog v-model="addBook.show" :title="addBook.title">
    <el-form>
      <el-form-item label="书名">
        <el-input v-model="addBook.name" placeholder="请输入书名"></el-input>
      </el-form-item>
      <el-form-item label="描述">
        <el-input
          v-model="addBook.description"
          :autosize="{ minRows: 4 }"
          type="textarea"
          placeholder="请输入描述 不可大于255字 可空"
          height="40px"
        ></el-input>
      </el-form-item>
      <el-form-item label="封面">
        <el-input
          v-model="addBook.cover"
          placeholder="请输入封面图片地址 可空"
        ></el-input>
      </el-form-item>
    </el-form>
    <template #footer>
      <span class="dialog-footer">
        <el-button @click="addBook.show = false">关闭</el-button>
        <el-button type="primary" @click="addBook_close()">完成</el-button>
      </span>
    </template>
  </el-dialog>
</template>

<script>
import API from '@/network/API'
export default {
  name: 'wordsadmin_books',
  data() {
    //数据
    return {
      booksData: [],
      addBook: {
        show: false,
        title: '添加书',
        type: 'add',
        bookid: 0,
        name: '',
        description: '',
        cover: '',
      },
    }
  },
  mounted: function () {
    this.getBook()
  },
  methods: {
    getBook() {
      const that = this
      API.wordsadmin.books.get().then((e) => {
        that.booksData = e.data
      })
    },
    addBook_open() {
      this.addBook.show = true

      this.addBook.title = '添加书'
      this.addBook.type = 'add'
      this.addBook.bookid = 0
      this.addBook.name = ''
      this.addBook.description = ''
      this.addBook.cover = ''
    },
    addBook_close() {
      if (this.addBook.type == 'edit') {
        this.editBook_close()
        return
      }

      this.addBook.show = false

      const that = this
      API.wordsadmin.books
        .add(this.addBook.name, this.addBook.description, this.addBook.cover)
        .then((e) => {
          that.$message.success(e.msg)

          that.getBook()
        })
        .catch((e) => {
          that.$message.error(e.msg)
        })
    },
    delBook(bookid, bookname) {
      const that = this
      this.$messageBox
        .confirm('确定要删除 ' + bookname + ' 吗？', '删除操作', {
          confirmButtonText: '删除',
          cancelButtonText: '取消',
          type: 'warning',
        })
        .then(() => {
          API.wordsadmin.books
            .del(bookid)
            .then((e) => {
              that.$message.success(e.msg)

              that.getBook()
            })
            .catch((e) => {
              that.$message.error(e.msg)
            })
        })
    },
    editBook_open(bookid, name, description, cover) {
      this.addBook.show = true

      this.addBook.title = '编辑书'
      this.addBook.type = 'edit'
      this.addBook.bookid = bookid
      this.addBook.name = name
      this.addBook.description = description
      this.addBook.cover = cover
    },
    editBook_close() {
      this.addBook.show = false

      const that = this
      API.wordsadmin.books
        .edit(
          this.addBook.bookid,
          this.addBook.name,
          this.addBook.description,
          this.addBook.cover
        )
        .then((e) => {
          that.$message.success(e.msg)

          that.getBook()
        })
        .catch((e) => {
          that.$message.error(e.msg)
        })
    },
    inBook(bookid) {
      this.$router.push({
        name: 'wordsadmin_group',
        params: {
          bookid: bookid,
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
  height: calc(100vh - 60px - 20px * 2 - 40px - 5px);
}
</style>
