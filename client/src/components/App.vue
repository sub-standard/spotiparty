<template>
  <div id="app">
    <ShowRoom v-if="room !== null" />
    <MakeRoom v-else />
  </div>
</template>

<script>
import MakeRoom from './MakeRoom'
import ShowRoom from './ShowRoom'

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