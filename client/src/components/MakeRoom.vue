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
import AccessToken from '../models/AccessToken'

export default {
  props: {
    accessToken: AccessToken
  },
  data: function() {
    return {
      title: ''
    }
  },
  methods: {
    onCreateRoom: function() {
      this.$http
        .post('http://localhost:5000/create-room', {
          access_token: this.accessToken.token
        })
        .then(
          response => {
            const code = response.data
            const room = new Room(this.title, this.code)

            this.$emit('create-room', room)
          },
          response => {
            // Error
          }
        )
    }
  }
}
</script>
