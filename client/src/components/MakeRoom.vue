<template>
  <div class="container">
    <form v-on:submit="e => {e.preventDefault(); onCreateRoom()}">
      <input v-model="title" placeholder="Room title"/>
      <button>Create a room</button>
    </form>
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

<style scoped>
.container {
  display: flex;
  align-items: center;
  justify-content: center;
  flex: 1;
}

form {
  display: flex;
  font-size: 2em;
  width: 500px;
  box-shadow: 10px 10px 0 0 black;
}

input {
  flex: 1;
  border: none;
  border: 5px solid black;
  padding: 0 16px;
}

input:focus {
  outline: none;
}

button {
  border: 5px solid black;
  border-left: none;
  background: #1db954;
  color: white;
  padding: 16px;
  cursor: pointer;
}
</style>

