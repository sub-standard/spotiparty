<template>
  <div>
    <a v-bind:href="url">Authorise Spotify</a>
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

      console.log(access_token)

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
