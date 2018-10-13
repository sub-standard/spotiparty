<template>
  <div id="make-room">
    <h2>Make a new Room</h2>

    <input v-model="title" placeholder="Room title">

    <button v-on:click="onCreateRoom">
      Create room
    </button>
  </div>
</template>

<script>
import Room from '../models/Room'

export default {
  data: function() {
    return {
      title: ''
    }
  },
  methods: {
    onCreateRoom: function() {
      // TODO get room id from server
      const code = 1234

      const room = new Room(this.title, code)

      this.$emit('create-room', room)
    }
  }
}
</script>
