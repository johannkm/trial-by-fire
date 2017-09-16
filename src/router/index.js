import Vue from 'vue'
import Router from 'vue-router'
import Dashboard from '@/pages/Dashboard'
import CodeProblem from '@/pages/CodeProblem'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Dashboard
    },
    {
      path: '/problem/:id',
      name: 'Code Problem',
      component: CodeProblem
    }
  ]
})
