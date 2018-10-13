<template>
  <div id="app">
    <Header v-bind:room="room" />

    <Authorise v-on:authorised="onAuthorised" v-if="!accessToken" />
    <template v-else>
      <ShowRoom v-if="room"  v-bind:room="room" />
      <MakeRoom v-else v-on:create-room="onCreateRoom" v-bind:accessToken="accessToken" />
    </template>
  </div>
</template>

<script>
import Header from './Header'
import MakeRoom from './MakeRoom'
import ShowRoom from './ShowRoom'
import Authorise from './Authorise'

export default {
  name: 'app',
  components: {
    Header,
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