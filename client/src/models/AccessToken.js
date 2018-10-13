export default function AccessToken(token, token_type, expires_in, state) {
  this.token = token
  this.token_type = token_type
  this.expires_in = expires_in
  this.state = state
}
