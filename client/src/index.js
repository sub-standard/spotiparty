import Vue from 'vue'
import VueResource from 'vue-resource'
import App from './components/App.vue'

Vue.config.productionTip = false
Vue.use(VueResource)

new Vue({
  el: '#app',
  render: h => h(App)
})
