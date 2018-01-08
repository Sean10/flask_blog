<template>
	<div id="todo">
		<h1>My Todo App!</h1>
		<TodoList/>
	</div>
</template>

<script>
import TodoList from '../components/TodoList.vue'

export default {
	components: {
		TodoList
	}
}
</script>

<style>
#app {
	max-width: 400px;
	margin: 0 auto;
	line-height: 1.4;
	font-family: 'Avenir', Helvetica, Arial, sans-serif;
	-webkit-font-smoothing: antialiased;
	-moz-osx-font-smoothing: grayscale;
	color: $vue-blue;
}

h1 {
	text-align: center;
}
</style>
