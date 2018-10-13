<template>
  <div class="container">
    <p class="title">
      <a href="/">SpotiParty</a>
    </p>
    
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
  padding: 24px 16px;
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