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

import Constants from '../Constants'
import AccessToken from '../models/AccessToken'

export default {
  props: {
    accessToken: AccessToken
  },
  mounted: function() {
    this.$nextTick(function() {
      const { access_token, token_type, expires_in, state } = queryString.parse(
        window.location.hash
      )

      if (
        access_token !== null &&
        access_token !== undefined &&
        access_token !== ''
      ) {
        const accessToken = new AccessToken(
          access_token,
          token_type,
          Date.now() + expires_in * 100,
          state
        )

        window.location.hash = ''

        this.$emit('authorised', accessToken)
      } else if (this.accessToken != null && this.accessToken.needsRenewing()) {
        window.location.href = this.url
        return
      }
    })
  },
  computed: {
    url: () => {
      return (
        'https://accounts.spotify.com/authorize' +
        '?response_type=token' +
        '&client_id=' +
        Constants.CLIENT_ID +
        (Constants.SCOPES ? '&scope=' + encodeURIComponent(scopes) : '') +
        '&redirect_uri=' +
        encodeURIComponent(Constants.REDIRECT_URI)
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
  background: #3ad772;
  color: black;
  padding: 16px;
  cursor: pointer;
  font-size: 2em;
  font-weight: bold;
}
</style>