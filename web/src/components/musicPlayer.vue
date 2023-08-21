<template>
  <div class="musicPlayer" :class="{ musicPlayer_open: show }">
    <div class="musicPlayer_close_btn" @click="show = !show">
      <el-icon v-if="show"><ArrowDown /></el-icon>
      <el-icon v-else="show"><ArrowUp /></el-icon>
    </div>
    <div class="musicPlayer_playbutton" @click="isPlaying = !isPlaying">
      <el-icon v-if="isPlaying"><VideoPause /></el-icon>
      <el-icon v-else="isPlaying"><VideoPlay /></el-icon>
    </div>
    <div class="musicPlayer_main">
      <span class="musicPlayer_name">{{ name }}</span>
      <div class="musicPlayer_slider">
        <el-slider
          v-model="progress"
          @input="_playingChange"
          :show-tooltip="false"
        />
        <span>{{ currenttime }} / {{ duration }}</span>
      </div>
    </div>

    <audio :src="src" ref="musicPlay" autoplay="autoplay"></audio>
  </div>
</template>

<script>
export default {
  props: {
    src: { type: String, required: true },
    name: { type: String },
  },
  data() {
    //数据
    return {
      show: false, //是否显示
      canPlay: false, //可以播放
      isPlaying: false, // 正在播放
      progress: 0,
      duration: '00:00',
      currenttime: '00:00',
    }
  },
  watch: {
    isPlaying(newItem, oldItem) {
      if (this.canPlay) {
        const musicPlay = this.$refs.musicPlay
        if (newItem) {
          musicPlay.play()
        } else {
          musicPlay.pause()
        }
      }
    },
    src(newItem, oldItem) {
      this.canPlay = false
      this.show = true
    },
  },
  mounted: function () {
    this._initPlayer()
  },
  methods: {
    _initPlayer() {
      const musicPlay = this.$refs.musicPlay
      const that = this
      musicPlay.onpause = musicPlay.onplay = () => {
        that.isPlaying = !musicPlay.paused
      }
      musicPlay.ontimeupdate = () => {
        if (musicPlay.duration) {
          that.progress = Math.floor(
            (musicPlay.currentTime / musicPlay.duration) * 100
          )
          that.duration = that.handleTime(musicPlay.duration)
          that.currenttime = that.handleTime(musicPlay.currentTime)
        } else {
          that.duration = '00:00'
          that.currenttime = '00:00'
        }
      }
      musicPlay.oncanplay = () => {
        that.canPlay = true
      }
    },
    _playingChange(e) {
      if (this.canPlay) {
        const progress = e / 100
        //进度条反向控制
        const musicPlay = this.$refs.musicPlay
        musicPlay.currentTime = musicPlay.duration * progress
      }
    },
    handleTime(seconedTime) {
      // https://blog.csdn.net/qq_41888962/article/details/108859534
      // 定义一个变量保存分钟
      var minute = parseInt(seconedTime / 60, 10)
      if (minute < 10) {
        minute = '0' + minute
      }
      // 定义变量存放秒数
      var second = (seconedTime - minute * 60).toFixed(2).split('.')[0]
      if (second < 10) {
        second = '0' + second
      }
      // 返回最终的时间数值
      return minute + ':' + second
    },
  },
}
</script>

<style>
.musicPlayer {
  position: fixed;
  width: 100%;
  height: 60px;
  padding: 10px;
  bottom: -80px;
  z-index: 10;
  box-shadow: 0px 0px 12px rgba(0, 0, 0, 0.12);
  background: #ffffff;
  transition: left var(--el-transition-duration),
    right var(--el-transition-duration), top var(--el-transition-duration),
    bottom var(--el-transition-duration);
}
.musicPlayer_close_btn {
  position: absolute;
  top: -20px;
  right: 30px;
  z-index: 11;
  width: 40px;
  height: 20px;
  background: #ffffff;
  box-shadow: 0px 0px 12px rgba(0, 0, 0, 0.12);
}
.musicPlayer_open {
  bottom: 0;
}
.musicPlayer_open .musicPlayer_close_btn {
  top: -10px;
}
.musicPlayer_close_btn .el-icon {
  width: 100%;
  height: 100%;
  line-height: 100%;
}
.musicPlayer_playbutton {
  width: 60px;
  height: 60px;
  overflow: hidden; /* margin塌陷 */
  display: inline-block;
}
.musicPlayer_playbutton .el-icon {
  margin: 5px;
}
.musicPlayer_playbutton .el-icon,
.musicPlayer_playbutton .el-icon svg {
  width: 50px;
  height: 50px;
  display: block;
}
.musicPlayer_main {
  display: inline-block;
  width: calc(100% - 110px);
  overflow: hidden;
}
.musicPlayer_name {
  margin-left: 20px;
}
.musicPlayer_slider {
  overflow: hidden;
}
.musicPlayer_slider .el-slider {
  width: calc(100% - 150px);
  display: inline-flex;
  margin-right: 20px;
  margin-left: 20px;
  --el-slider-main-bg-color: #000;
}
</style>
