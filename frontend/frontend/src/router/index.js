import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import TodoList from '@/components/TodoList'

Vue.use(Router)


export default new Router({
	mode: 'history',
  routes: [
    {
      path: '/hello',
      name: 'HelloWorld',
      component: HelloWorld
  },
  {
      path: '/todo',
      name: 'todo',
	  // props: ['todos']
      component: TodoList
  }
  ]
})
