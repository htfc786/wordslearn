<template>
    <div class="phone">
      <router-view></router-view>
    </div>
</template>

<script>
export default {
  name: 'App',
  components: {
  }
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