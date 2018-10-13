<template>
  <div id="app">
    <h1>SpotiParty</h1>

    <div v-if="accessToken !== null">
      <ShowRoom v-if="room !== null" v-bind:room="room" />
      <MakeRoom v-else v-on:create-room="onCreateRoom" />
    </div>
    <div v-else>
      <Authorise v-on:authorised="onAuthorised" />
    </div>
  </div>
</template>

<script>
import MakeRoom from './MakeRoom'
import ShowRoom from './ShowRoom'
import Authorise from './Authorise'
import Room from '../models/Room'

export default {
  name: 'app',
  components: {
    MakeRoom,
    ShowRoom,
    Authorise
  },
  data: function() {
    return {
      room: null,
      accessToken: null
    }
  },
  methods: {
    onAuthorised: function(accessToken) {
      this.accessToken = accessToken
    },
    onCreateRoom: function(title) {
      // TODO get room id from server
      const code = 1234

      this.room = new Room(title, code)
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

body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto,
    Oxygen-Sans, Ubuntu, Cantarell, 'Helvetica Neue', sans-serif;
  font-size: 62.5%;
}
</style>