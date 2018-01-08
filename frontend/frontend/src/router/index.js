import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import TodoList from '@/components/TodoList'

Vue.use(Router)

const Foo = { template:`<div id="todo">
		<h1>My Test App!</h1>
	</div>`, component: Foo}


export default new Router({
  routes: [
    {
      path: '/hello',
      name: 'HelloWorld',
      component: HelloWorld
  },
  {
      path: '/Foo',
      name: 'Foo',
      component: Foo
  },
  {
      path: '/todo',
      name: 'todo',
      component: TodoList
  }
  ]
})
