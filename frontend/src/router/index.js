import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import TodoList from '@/components/TodoList'
import Login from '../view/Login'
import UploadView from '../view/upload_view'
import About from '../view/about'

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
      path: '/uploads',
      name: 'uploads',
      component: UploadView
    },
    {
      path: '/about',
      name: 'about',
      component: About
    }
  ]
})
