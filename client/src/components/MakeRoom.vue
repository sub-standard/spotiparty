<template>
  <div id="make-room">
    <h2>Make a new Room</h2>

    <input v-model="title" placeholder="Room title">

    <button v-on:click="$emit('create-room', title)">
      Create room
    </button>
  </div>
</template>

<script>
export default {
  data: function() {
    return {
      title: ''
    }
  }
}
</script>
