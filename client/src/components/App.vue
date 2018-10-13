<template>
  <div id="app">
    <Header v-bind:room="room"  v-if="accessToken" />

    <Authorise v-if="!hasValidAccessToken()" v-on:authorised="onAuthorised" v-bind:accessToken="accessToken" />
    <template v-else>
      <ShowRoom v-if="room" v-bind:room="room"  v-bind:accessToken="accessToken" v-bind:playlistId="playlistId" />
      <CreateRoom v-else v-on:create-room="onCreateRoom" v-bind:accessToken="accessToken" />
    </template>
  </div>
</template>

<script>
import Header from './Header'
import CreateRoom from './CreateRoom'
import ShowRoom from './ShowRoom'
import Authorise from './Authorise'
import AccessToken from '../models/AccessToken'
import Room from '../models/Room'

export default {
  name: 'app',
  components: {
    Header,
    CreateRoom,
    ShowRoom,
    Authorise
  },
  data: function() {
    return {
      room: (function() {
        if (localStorage.room) {
          const { title, code } = JSON.parse(localStorage.room)
          return new Room(title, code)
        }
        return null
      })(),
      accessToken: (function() {
        if (localStorage.accessToken) {
          const { token, token_type, expires, state } = JSON.parse(
            localStorage.accessToken
          )
          return new AccessToken(token, token_type, expires, state)
        }
        return null
      })(),
      playlistId: null
    }
  },
  watch: {
    room(newRoom) {
      localStorage.room = JSON.stringify(newRoom)
    },
    accessToken(newAccessToken) {
      localStorage.accessToken = JSON.stringify(newAccessToken)
    }
  },
  methods: {
    hasValidAccessToken: function() {
      return (
        this.accessToken !== null &&
        this.accessToken.token !== null &&
        this.accessToken.token !== '' &&
        !this.accessToken.needsRenewing()
      )
    },
    onAuthorised: function(accessToken) {
      this.accessToken = accessToken
    },
    onCreateRoom: function(room, playlistId) {
      this.room = room
      this.playlistId = playlistId
    }
  }
}
</script>

<!-- CSS libraries -->
<style src="normalize.css/normalize.css"></style>

<!-- Global CSS -->
<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

a {
  color: inherit;
  text-decoration: none;
}

#app {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto,
    Oxygen-Sans, Ubuntu, Cantarell, 'Helvetica Neue', sans-serif;
  font-size: 62.5%;
  background-color: #fefefe;
}
</style>