import Vue from 'vue'
import VueResource from 'vue-resource'
import { library } from '@fortawesome/fontawesome-svg-core'
import {
  faBackward,
  faForward,
  faPause,
  faPlay
} from '@fortawesome/free-solid-svg-icons'
import { faSpotify } from '@fortawesome/free-brands-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import App from './components/App.vue'

Vue.use(VueResource)

library.add(faBackward, faForward, faPause, faPlay, faSpotify)

Vue.component('font-awesome-icon', FontAwesomeIcon)

Vue.config.productionTip = false

new Vue({
  el: '#app',
  render: h => h(App)
})
