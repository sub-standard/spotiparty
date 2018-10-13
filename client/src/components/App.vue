<template>
  <div id="app">
    <Header v-bind:room="room"  v-if="accessToken" />

    <Authorise v-on:authorised="onAuthorised" v-if="!accessToken" />
    <template v-else>
      <ShowRoom v-if="room" v-bind:room="room" />
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
      room: null,
      accessToken: null,
      userId: null
    }
  },
  mounted() {
    if (localStorage.accessToken) {
      const { token, token_type, expires, state } = JSON.parse(
        localStorage.accessToken
      )
      this.accessToken = new AccessToken(token, token_type, expires, state)
    }
    if (localStorage.room) {
      const { title, code } = JSON.parse(localStorage.room)
      this.room = new Room(title, code)
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
    onAuthorised: function(accessToken) {
      this.accessToken = accessToken
    },
    onCreateRoom: function(room) {
      this.room = room
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