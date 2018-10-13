<template>
  <div class="container">
    <div class="playback-container">
      <template v-if="track">
        <div class="playback-info">
          <img class="playback-info-art" v-bind:src="track.album.images[0].url" />
          <div class="playback-info-song">{{track.name + ' - ' + track.artists[0].name }}</div>
        </div>
      </template>
      <div class="playback-controls">
        <button class="playback-button" v-on:click="onPrevious">
          <font-awesome-icon icon="backward" />
        </button>
        <button class="playback-button" v-on:click="onPlayPause">
          <font-awesome-icon v-bind:icon="playing ? 'pause' : 'play'" />
        </button>
        <button class="playback-button" v-on:click="onNext">
          <font-awesome-icon icon="forward" />
        </button>
      </div>
    </div>

    <div class="queue-container">
      <p class="queue-container-title">{{ playlistTitle }}</p>
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
    playing: false,
    interval: null,
    playlistTitle: null
  }),
  props: {
    room: Room,
    accessToken: AccessToken
  },
  methods: {
    async getPlaylistName() {
      const response = await this.$http.get(
        `https://api.spotify.com/v1/playlists/${this.room.playlistId}`,
        {
          headers: {
            Authorization: 'Bearer ' + this.accessToken.token
          }
        }
      )

      this.playlistTitle = response.data.name
    },
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
    },
    async onPlayPause() {
      const response = await this.$http.put(
        `https://api.spotify.com/v1/me/player/${
          this.playing ? 'pause' : 'play'
        }`,
        {},
        {
          headers: {
            Authorization: 'Bearer ' + this.accessToken.token
          }
        }
      )

      this.destroyInterval()
      this.playing = !this.playing
      setTimeout(this.setupInterval, 500)
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
    },
    setupInterval: function() {
      this.interval = setInterval(() => {
        this.getCurrentData()
      }, 500)
    },
    destroyInterval: function() {
      clearInterval(this.interval)
      this.interval = null
    }
  },
  beforeMount: function() {
    this.getCurrentData()
  },
  mounted: function() {
    this.setupInterval()
    this.getPlaylistName()
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
  margin-bottom: 16px;
}

.playback-controls {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  box-shadow: 10px 10px 0 0 black;
  border: 5px solid black;
}

.playback-button {
  border: none;
  background-color: #3ad772;
  flex: 1;
  font-size: 3.2em;
  height: 80px;
}

.playback-button:focus {
  outline: none;
}

.playback-button:not(:last-child) {
  border-right: 5px solid black;
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