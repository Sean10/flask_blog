import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import TodoList from '@/components/TodoList'
import Login from '../view/Login'
import UploadView from '../view/upload_view'
import About from '../view/about'
import UserInfo from '../view/userInfo'
import SignUp from '../view/signup'

Vue.use(Router);


export default new Router({
  // mode: 'history',
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/todo',
      name: 'todo',
      component: TodoList,
      meta: {
        requireAuth: false,
      }
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignUp
    },
    {
      path: '/uploads',
      name: 'uploads',
      component: UploadView
    },
    {
      path: '/about',
      name: 'about',
      component: About
    },
    {
      path: '/userInfo',
      name: 'UserInfo',
      component: UserInfo
    }
  ]
})
