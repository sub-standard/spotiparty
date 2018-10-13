<template>
  <div class="container">
    <div class="playback-container">
      <div class="playback-info">
        <img class="playback-info-art" src="https://i.pinimg.com/474x/25/12/28/2512289ea977440827a012d64ebda89e--night-vision-my-music.jpg" />
        <div class="playback-info-song">Demons - Imagine Dragons</div>
      </div>
    </div>
    
    <div class="queue-container">
      <p class="queue-container-title">Up Next</p>
      <ol>
        <li>Song 1</li>
        <li>Song 2</li>
        <li>Song 3</li>
      </ol>
    </div>
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
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 16px;
  flex: 1;
}

.playback-container {
  flex: 1;
  margin-right: 32px;
  display: flex;
  flex-direction: column;
  height: 100%;
  justify-content: center;
  align-items: center;
}

.playback-info {
  box-shadow: 10px 10px 0 0 black;
  border: 5px solid black;
}

.playback-info-art {
  width: 100%;
}

.playback-info-song {
  border-top: 5px solid black;
  background: #1db954;
  color: white;
  font-size: 2em;
  padding: 16px;
}

.queue-container {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
}

.queue-container-title {
  font-size: 2.4em;
  font-weight: bold;
  margin-bottom: 24px;
}

.queue-container ol {
  list-style-position: inside;
}

.queue-container ol li {
  font-size: 2em;
  margin-bottom: 24px;
}
</style>