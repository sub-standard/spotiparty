export default function AccessToken(token, token_type, expires, state) {
  this.token = token
  this.token_type = token_type
  this.expires = expires
  this.state = state

  this.needsRenewing = function() {
    this.expires <= Date.now()
  }
}
