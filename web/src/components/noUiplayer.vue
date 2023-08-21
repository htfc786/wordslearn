<template>
  <audio
    :src="src"
    ref="musicPlay"
    autoplay="autoplay"
  ></audio>
</template>

<script>
export default {
  data() {
    //数据
    return {
      src: "", //目标地址
      sound_start: 0,
      sound_end: 0,
      canPlay: false,
    }
  },
  watch: {
    src(newItem, oldItem) {
      this.canPlay = false;
    },
    canPlay(newItem, oldItem) {
      if (newItem){
        const musicPlay = this.$refs.musicPlay
        musicPlay.currentTime = this.sound_start
        musicPlay.play()
      }
    }
  },
  mounted: function () {
    this._initPlayer()
  },
  methods: {
    _initPlayer() {
      const musicPlay = this.$refs.musicPlay
      const that = this
      musicPlay.ontimeupdate = () => {
        if (musicPlay.duration){
          if (musicPlay.currentTime >= that.sound_end){
            musicPlay.pause()
          }
        }
      }
      musicPlay.oncanplay = () => {
        that.canPlay = true;
      }
    },
    play(url, sound_start, sound_end) {
      const musicPlay = this.$refs.musicPlay

      this.sound_start = sound_start
      this.sound_end = sound_end
      
      this.src = url
      if (this.canPlay){
        musicPlay.currentTime = sound_start
        musicPlay.play()
      }
    },
  },
}
</script>

<style>

</style>
