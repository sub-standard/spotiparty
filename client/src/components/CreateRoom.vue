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
import Constants from '../Constants'
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
      const response = await this.$http
        .post(`${Constants.BACKEND_SERVER}/create-room`, {
          access_token: this.accessToken.token,
          playlist_id: playlistId
        })
        .catch(() => {
          const room = new Room(playlistId, '0000')
          this.$emit('create-room', room)
        })

      const { code } = response.data
      const room = new Room(playlistId, code)

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
  transition: all 100ms ease-out;
}

.playlists-container li p {
  box-shadow: 10px 10px 0 0 black;
  border: 5px solid black;
  font-size: 1.6em;
  font-weight: bold;
  padding: 8px;
  text-align: center;
  transition: all 100ms ease-out;
}

.playlists-container li:hover p {
  box-shadow: 14px 14px 0 0 black;
  transform: translateY(-0px) scale(1.02);
}
</style>

