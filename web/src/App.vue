<template>
    <div ref="app" class="phone">
      <router-view></router-view>
    </div>
</template>

<script>
export default {
  name: 'App',
  components: {
  },
  watch: {
    $route: {
      handler: function(val, oldVal){
        //判断页面是手机模式还是电脑模式
        if (val.meta.mode == 'phone'){
          this.$refs.app.classList.add("phone")
        } else {
          this.$refs.app.classList.remove("phone")
        }
      },
      deep: true
    }
  },
}
</script>

<style scoped>
  @media screen and (min-width: 400px) {
    .phone {
      width: 400px;
      margin: 0 auto;
    }
  }
</style>