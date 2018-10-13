<template>
  <div id="app">
    <h1>SpotiParty</h1>

    <ShowRoom v-if="room !== null" v-bind:room="room" />
    <MakeRoom v-else v-on:create-room="onCreateRoom" />
  </div>
</template>

<script>
import MakeRoom from './MakeRoom'
import ShowRoom from './ShowRoom'
import Room from '../models/Room'

export default {
  name: 'app',
  components: {
    MakeRoom,
    ShowRoom
  },
  data: function() {
    return {
      room: null
    }
  },
  methods: {
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