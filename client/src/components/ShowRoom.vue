<template>
  <div class="container">
    <div class="playback-container">
      <template v-if="this.track">
        <div class="playback-info">
          <img class="playback-info-art" v-bind:src="this.track.album.images[0].url" />
          <div class="playback-info-song">{{this.track.name + ' - ' + this.track.artists[0].name }}</div>
        </div>
      </template>
      <div class="playback-controls">
        <button v-on:click="onPrevious">Previous</button>
        <button v-on:click="onPlayPause">{{ playing ? 'Pause' : ' Play' }}</button>
        <button v-on:click="onNext">Next</button>
      </div>
    </div>

    <div class="queue-container">
      <p class="queue-container-title">Playlist</p>
      <ol>
        <li>Song 1</li>
        <li>Song 2</li>
        <li>Song 3</li>
      </ol>
    </div>
  </div>
</template>

<script>
import Room from '../models/Room'
import AccessToken from '../models/AccessToken'

export default {
  data: () => ({
    track: null,
    playing: false
  }),
  props: {
    room: Room,
    accessToken: AccessToken,
    playlistId: null
  },
  methods: {
    async getCurrentData() {
      const response = await this.$http.get(
        'https://api.spotify.com/v1/me/player/currently-playing',
        {
          headers: {
            Authorization: 'Bearer ' + this.accessToken.token
          }
        }
      )

      this.track = response.data.item
      this.playing = response.data.is_playing
    },
    async onPrevious() {
      const response = await this.$http.post(
        'https://api.spotify.com/v1/me/player/previous',
        {},
        {
          headers: {
            Authorization: 'Bearer ' + this.accessToken.token
          }
        }
      )

      await this.getCurrentData()
    },
    async onPlayPause() {
      const response = await this.$http.put(
        'https://api.spotify.com/v1/me/player/' +
          (this.playing ? 'pause' : 'play'),
        {},
        {
          headers: {
            Authorization: 'Bearer ' + this.accessToken.token
          }
        }
      )

      this.playing = !this.playing
    },
    async onNext() {
      const response = await this.$http.post(
        'https://api.spotify.com/v1/me/player/next',
        {},
        {
          headers: {
            Authorization: 'Bearer ' + this.accessToken.token
          }
        }
      )

      await this.getCurrentData()
    }
  },
  beforeMount: function() {
    this.getCurrentData()
  },
  mounted: function() {
    window.setInterval(() => {
      this.getCurrentData()
    }, 1000)
  }
}
</script>

<style scoped>
.container {
  display: flex;
  justify-content: center;
  padding: 32px;
  flex: 1;
}

.playback-container {
  display: flex;
  flex-direction: column;
  width: 400px;
}

.playback-info-art {
  width: 100%;
  box-shadow: 10px 10px 0 0 black;
  border: 5px solid black;
  margin-bottom: 16px;
}

.playback-info-song {
  box-shadow: 10px 10px 0 0 black;
  border: 5px solid black;
  font-weight: bold;
  font-size: 2em;
  padding: 16px;
  text-align: center;
}

.queue-container {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  box-shadow: 10px 10px 0 0 black;
  border: 5px solid black;
  padding: 32px;
  margin: 0 10px 0 32px;
}

.queue-container-title {
  font-size: 2.4em;
  font-weight: bold;
  margin-bottom: 24px;
}

.queue-container ol {
  list-style-position: inside;
}

.queue-container ol li {
  font-size: 2em;
  margin-bottom: 24px;
}
</style>