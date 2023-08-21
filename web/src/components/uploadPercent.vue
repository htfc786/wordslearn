<template>
  <div class="uploadPercent" :class="{ uploadPercent_open: show }">
    上传进度：
    <el-progress :percentage="percent" />
  </div>
</template>

<script>
export default {
  props: {
    show: { type: Boolean, required: true }, //是否显示
    percent: { type: Number, required: true }, //进度
  },
}
</script>

<style>
.uploadPercent {
  position: fixed;
  bottom: 30px;
  right: -350px;
  /* height: 100px; */
  width: 300px;
  padding: 14px 26px 14px 13px;
  border-radius: 8px;
  border: 1px solid #ebeef5;
  box-shadow: 0px 0px 12px rgba(0, 0, 0, 0.12);
  overflow: hidden;
  z-index: 11;
  background: white;
  transition: opacity var(--el-transition-duration),
    transform var(--el-transition-duration), left var(--el-transition-duration),
    right var(--el-transition-duration), top 0.4s,
    bottom var(--el-transition-duration);
}
.uploadPercent_open {
  right: 30px;
}
.el-progress {
  margin: 8px;
}
</style>
