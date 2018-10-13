<template>
  <div class="container">
    <h1 class="title">SpotiParty™️</h1>
    <p class="description">
      Queue songs on Spotify with your friends.
    </p>

    <a v-bind:href="url">
      <button class="authorise-button">Sign in with Spotify</button>
    </a>
  </div>
</template>

<script>
import queryString from 'query-string'

import AccessToken from '../models/AccessToken'

export default {
  mounted: function() {
    this.$nextTick(function() {
      const { access_token, token_type, expires_in, state } = queryString.parse(
        location.hash
      )

      if (
        access_token !== null &&
        access_token !== undefined &&
        access_token !== ''
      ) {
        const accessToken = new AccessToken(
          access_token,
          token_type,
          expires_in,
          state
        )

        this.$emit('authorised', accessToken)
      }
    })
  },
  computed: {
    url: () => {
      const client_id = '2ceb460f532b46ac9e50a3fd7a9db083'
      const scopes = 'playlist-modify-public'
      const redirect_uri = 'http://localhost:4000'

      return (
        'https://accounts.spotify.com/authorize' +
        '?response_type=token' +
        '&client_id=' +
        client_id +
        (scopes ? '&scope=' + encodeURIComponent(scopes) : '') +
        '&redirect_uri=' +
        encodeURIComponent(redirect_uri)
      )
    }
  }
}
</script>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  flex: 1;
}

.title {
  font-size: 4em;
  margin: 0 0 24px 0;
}

.description {
  font-size: 2.4em;
  margin: 0 0 80px 0;
}

.authorise-button {
  border: 5px solid black;
  box-shadow: 10px 10px 0 0 black;
  background: #1db954;
  color: white;
  padding: 16px;
  cursor: pointer;
  font-size: 2em;
}
</style>