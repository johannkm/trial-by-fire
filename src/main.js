// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import VueCodeMirror from 'vue-codemirror'

import { VTooltip } from 'v-tooltip'
Vue.directive('tooltip', VTooltip)

Vue.use(VueCodeMirror)

import Notifications from 'vue-notification'

Vue.use(Notifications)

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  template: '<App/>',
  components: { App }
})
