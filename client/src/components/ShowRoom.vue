<template>
  <div class="container">
    <div class="contents">
      <div class="playback-container">
        <template v-if="track">
          <div class="playback-info">
            <img class="playback-info-art" v-bind:src="track.album.images[0].url" />
            <div class="playback-info-song">{{ track.name + ' - ' + track.artists[0].name }}</div>
          </div>
        </template>
        <template v-else>
          <div class="spotify-placeholder">
            <font-awesome-icon :icon="['fab', 'spotify']" class="fa-fw" />
          </div>
          <div class="playback-info-song">{{ device != undefined ? `Connected to ${device.name}` : 'Open the Spotify app to start listening' }}</div>
        </template>
        <div v-if="device != undefined" class="playback-controls">
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

      <div class="commands-container">

        <div class="commands-details-container">
          <p class="commands-details-title">Phone Number</p>
          <p class="commands-details-value commands-details-phone">{{ phoneNo }}</p>
        </div>

        <div class="commands-details-container">
          <p class="commands-details-title">Room Code</p>
          <p class="commands-details-value">{{ room.code }}</p>
        </div>

        <ul class="commands-list">
          <li><b>JOIN {{ room.code }}</b> to join a room</li>
          <li><b>ADD song name</b> to add a song</li>
          <li><b>SKIP</b> to skip the current song</li>
        </ul>
      </div>

      <div class="meta-container">
        <p class="commands-details-title">Room Guests</p>
        <p class="commands-details-value">{{ room.guests || 0 }}</p>
      </div>

      <div class="queue-container">
        <p class="queue-container-title">{{ playlistTitle }}</p>
        <ol>
          <li v-for="t in tracks" v-bind:key="t.id">
            <span class="track-name">{{ t.name }}</span>
            <span v-if="t.artists.length > 0" class="track-artist">{{ t.artists[0].name }}</span>
          </li>
        </ol>
      </div>
    </div>
  </div>
</template>

<script>
import Constants from '../Constants'
import Room from '../models/Room'
import AccessToken from '../models/AccessToken'

export default {
  data: () => ({
    track: null,
    tracks: null,
    playing: false,
    interval: null,
    playlistTitle: null,
    device: undefined
  }),
  props: {
    room: Room,
    accessToken: AccessToken
  },
  computed: {
    phoneNo: function() {
      return Constants.PHONE_NO
    }
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
    async getPlaybackState() {
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

      if (response.data.device != null) {
        this.device = response.data.device
      } else {
        const responseDevices = await this.$http.get(
          'https://api.spotify.com/v1/me/player/devices',
          {
            headers: {
              Authorization: 'Bearer ' + this.accessToken.token
            }
          }
        )

        if (
          responseDevices.data.devices != null &&
          responseDevices.data.devices.length > 0
        ) {
          this.device = responseDevices.data.devices[0]
        } else {
          this.device = undefined
        }
      }
    },
    async getPlaylistContents() {
      const response = await this.$http.get(
        `https://api.spotify.com/v1/playlists/${this.room.playlistId}`,
        {
          headers: {
            Authorization: 'Bearer ' + this.accessToken.token
          }
        }
      )

      this.tracks = response.data.tracks.items.map(item => item.track)
    },
    async getNoGuests() {
      const response = await this.$http.get(
        `${Constants.BACKEND_SERVER}/room-guests/${this.room.code}`
      )

      this.room.guests = response.data.guests
    },
    async getCurrentData() {
      Promise.all([
        this.getPlaybackState(),
        this.getNoGuests(),
        this.getPlaylistContents()
      ])
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
      const body =
        this.track != null
          ? {}
          : { context_uri: `spotify:playlist:${this.room.playlistId}` }
      const response = await this.$http.put(
        `https://api.spotify.com/v1/me/player/${
          this.playing ? 'pause' : 'play'
        }${
          this.track == undefined && this.device != undefined
            ? `?device_id=${this.device.id}`
            : ''
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
    this.getPlaylistContents()
  }
}
</script>

<style scoped>
.container {
  flex: 1;
  display: flex;
  padding: 32px;
}

.contents {
  flex: 1;
  display: grid;
  grid-gap: 32px;
  grid-template-areas:
    'playback'
    'meta'
    'commands'
    'playlist';
}

.playback-container {
  display: flex;
  flex-direction: column;
  grid-area: playback;
}

.spotify-placeholder {
  width: 100%;
  box-shadow: 10px 10px 0 0 black;
  border: 5px solid black;
  margin-bottom: 16px;
  color: #d5f6e0;
  background-color: #fefefe;
}

.spotify-placeholder .svg-inline--fa {
  width: 100%;
  height: auto;
  padding: 60px;
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
  background-color: #fefefe;
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
  cursor: pointer;
}

.playback-button:focus {
  outline: none;
}

.playback-button:not(:last-child) {
  border-right: 5px solid black;
}

.meta-container {
  grid-area: meta;
  box-shadow: 10px 10px 0 0 black;
  border: 5px solid black;
  font-size: 1.8em;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 32px;
  background-color: #fefefe;
}

.commands-details-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background-color: #fefefe;
}

.commands-details-title {
  font-size: 1.2rem;
  font-weight: bold;
  margin-bottom: 4px;
}

.commands-details-value {
  font-size: 3.2rem;
  font-weight: bold;
}

.commands-details-phone {
  font-size: 2.4rem;
  line-height: 3.6rem;
}

.commands-container {
  grid-area: commands;
  box-shadow: 10px 10px 0 0 black;
  border: 5px solid black;
  font-size: 1.8em;
  padding: 32px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background-color: #fefefe;
}

.commands-container-values {
  margin-right: 60px;
}

.commands-container-values p:first-child {
  margin-bottom: 8px;
}

.commands-list {
  list-style-type: none;
}

.commands-list li {
  margin-top: 12px;
}

.commands-list li b {
  padding: 4px 8px;
  border-radius: 4px;
  background-color: #3ad772;
  font-weight: bold;
  font-size: 0.9rem;
}

.queue-container {
  grid-area: playlist;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  box-shadow: 10px 10px 0 0 black;
  border: 5px solid black;
  padding: 32px;
  background-color: #fefefe;
}

.queue-container-title {
  font-size: 2.4em;
  font-weight: bold;
  margin-bottom: 24px;
}

.queue-container ol {
  list-style-position: inside;
  font-size: 1rem;
}

.queue-container ol li {
  font-size: 1rem;
  margin-bottom: 24px;
}

.queue-container ol li:last-child {
  margin-bottom: 0;
}

.queue-container ol li .track-name {
  font-size: 1.2rem;
  font-weight: bold;
}

.queue-container ol li .track-artist {
  font-size: 1rem;
  margin-left: 0.2rem;
}

@media screen and (min-width: 500px) {
  .contents {
    grid-template-areas:
      'playback commands commands'
      'playback playlist meta';
    grid-template-columns: 400px auto 200px;
  }

  .queue-container {
    overflow: scroll;
  }

  .commands-container {
    flex-direction: row;
    justify-content: space-between;
  }
}
</style>