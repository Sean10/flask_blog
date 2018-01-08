<template>
<div id="app">
	<!-- <div class="line"></div> -->
	<el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect" background-color="#545c64" text-color="#fff" active-text-color="#ffd04b">
		<el-menu-item index="1">
			<router-link to="/todo">TodoList</router-link>
		</el-menu-item>
		<!-- <router-link :to="/todo">Todo</router-link> -->
		<el-submenu index="2">
			<template slot="title">我的工作台</template>
			<el-menu-item index="2-1">选项1</el-menu-item>
			<el-menu-item index="2-2">选项2</el-menu-item>
			<el-menu-item index="2-3">选项3</el-menu-item>
		</el-submenu>
		<el-menu-item index="3"><a href="https://www.ele.me" target="_blank">订单管理</a></el-menu-item>
	</el-menu>

	<img src="./assets/logo.png">
	<router-view></router-view>
	<!-- <el-button>默认按钮</el-button>
	<el-button type="primary">主要按钮</el-button>
	<el-button type="text">文字按钮</el-button>
	<el-input-number v-model="num1" @change="handleChange" :min="1" :max="10"></el-input-number>
	<br />
	<el-input placeholder="elinput输入框">a</el-input>
	<input placeholder="input输入框">b</input> -->
</div>
</template>

<script>
export default {
	name: 'app',
	data() {
		return {
			num1: 1,
			activeIndex: '1',
		};
	},
	methods: {
		// handleChange(value) {
		//   console.log(value);
		// },
		handleSelect(key, keyPath) {
			console.log(key, keyPath);
		}
	}
}
</script>

<style>
*,
*::before,
*::after {
	box-sizing: border-box;
}

#app {
	font-family: 'Avenir', Helvetica, Arial, sans-serif;
	-webkit-font-smoothing: antialiased;
	-moz-osx-font-smoothing: grayscale;
	text-align: center;
	color: #2c3e50;
	margin: 0 auto;
	line-height: 1.4;
	color: $vue-blue;

/* margin-top: 60px; */

}
</style>
