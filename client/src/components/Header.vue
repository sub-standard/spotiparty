<template>
  <div class="container">
    <p class="title">
      <a href="/">SpotiParty</a>
    </p>

    <p class="sign-out" @click="signOut">Sign out</p>
  </div>
</template>

<script>
import Room from '../models/Room'

export default {
  props: {
    room: Room
  },
  methods: {
    signOut: function() {
      localStorage.clear()
      location.reload()
    }
  }
}
</script>

<style scoped>
.container {
  padding: 24px;
  border-bottom: 5px solid black;
  display: flex;
  align-items: center;
  font-size: 1.4rem;
  font-weight: bold;
  background: #3ad772;
  color: black;
  transition: all 100ms;
}

.title {
  font-size: inherit;
  flex: 1;
}

.sign-out {
  font-size: 1rem;
  margin-left: 24px;
  cursor: pointer;
}
</style>