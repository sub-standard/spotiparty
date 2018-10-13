<template>
  <div>
    <h2>{{ room.code }} {{ room.title }}</h2>
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
