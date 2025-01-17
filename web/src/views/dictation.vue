<template>
  <div class="top">
    <el-icon @click="this.$router.go(-1)"><ArrowLeftBold /></el-icon>
  </div>
  <div class="main">
    
  </div>
</template>

<script>

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
</style>