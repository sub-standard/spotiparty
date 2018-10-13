<template>
  <div class="container">
    <ul class="playlists-container">
      <li v-for="playlist in playlists" :key="playlist.id" @click="() => onCreateRoom(playlist.id)">
        <img v-bind:src="playlist.images[0].url" v-bind:alt="playlist.name" />
        <p>{{ playlist.name }}</p>
      </li>
    </ul>
  </div>
</template>

<script>
import Room from '../models/Room'
import AccessToken from '../models/AccessToken'

export default {
  props: {
    accessToken: AccessToken
  },
  data: () => ({
    playlists: null
  }),
  methods: {
    onCreateRoom: async function(playlistId) {
      const response = await this.$http.post(
        'http://1ddcefc7.ngrok.io/create-room',
        {
          access_token: this.accessToken.token,
          playlist_id: playlistId
        }
      )

      const { code } = response.data
      const room = new Room(this.title, code)

      this.$emit('create-room', room)
    }
  },
  beforeMount: async function() {
    const response = await this.$http.get(
      `https://api.spotify.com/v1/me/playlists`,
      {
        headers: {
          Authorization: 'Bearer ' + this.accessToken.token
        }
      }
    )

    this.playlists = response.body.items
  }
}
</script>

<style scoped>
.container {
  display: flex;
  align-items: flex-start;
  justify-content: center;
  flex: 1;
}

.playlists-container {
  list-style-type: none;
  width: 100vw;
  display: flex;
  flex-wrap: wrap;
}

.playlists-container li {
  margin: 24px;
  cursor: pointer;
}

.playlists-container li img {
  box-shadow: 10px 10px 0 0 black;
  border: 5px solid black;
  width: 232px;
  margin-bottom: 16px;
}

.playlists-container li p {
  box-shadow: 10px 10px 0 0 black;
  border: 5px solid black;
  font-size: 1.6em;
  font-weight: bold;
  padding: 8px;
  text-align: center;
}
</style>

