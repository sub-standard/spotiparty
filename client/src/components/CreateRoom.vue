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
    onCreateRoom: function(playlistId) {
      this.$http
        .post('http://localhost:5000/create-room', {
          access_token: this.accessToken.token,
          playlist_id: playlistId
        })
        .then(
          response => {
            const code = response.data
            const room = new Room(this.title, code)

            this.$emit('create-room', room)
          },
          response => {
            // Error
            // TODO don't make fake code
            const room = new Room(this.title, '0000')

            this.$emit('create-room', room)
          }
        )
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
  box-shadow: 10px 10px 0 0 black;
  border: 5px solid black;
  margin: 16px;
  cursor: pointer;
}

.playlists-container li img {
  width: 240px;
}

.playlists-container li p {
  font-size: 1.6em;
  background: #1db954;
  color: white;
  padding: 8px;
  text-align: center;
}
</style>

