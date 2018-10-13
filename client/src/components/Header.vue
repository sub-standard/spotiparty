<template>
  <div class="container">
    <h1 class="title">
      <a href="/">SpotiParty</a>
    </h1>
    
    <p v-if="room">Room Code: {{ room.code }}</p>
  </div>
</template>

<script>
import Room from '../models/Room'

export default {
  props: {
    room: Room
  }
}
</script>

<style scoped>
.container {
  padding: 8px 16px;
  border-bottom: 5px solid black;
  display: flex;
  align-items: center;
  font-size: 1.6rem;
  font-weight: bold;
  background: #1db954;
  color: white;
}

.title {
  font-size: inherit;
  flex: 1;
}
</style>