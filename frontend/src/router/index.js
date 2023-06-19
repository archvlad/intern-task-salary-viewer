import Vue from 'vue'
import VueRouter from 'vue-router'
import LoginForm from '../LoginForm.vue'
import MainPanel from '../MainPanel.vue'
import CurrentSalary from '../CurrentSalary.vue'
import NextIncrease from '../NextIncrease.vue'

Vue.use(VueRouter)

const routes = [
  { path: '/login', component: LoginForm, alias: '/' },
  {
    path: '/me', component: MainPanel, redirect: 'me/current_salary', children: [
      {
        path: 'current_salary',
        component: CurrentSalary,
      },
      {
        path: 'next_increase',
        component: NextIncrease,
      },
    ],
  }
]

export default new VueRouter({
  mode: 'history',
  routes
})
