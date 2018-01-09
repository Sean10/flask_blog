<template lang="html">
  <div id="topbar">
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
		<el-submenu index="-1" id="login" class="el-footer">
			<template slot="title" id="username">{{ username }}</template>
			<el-menu-item index="grzx-bky"><a href='http://sean10.github.io' target="_blank">博客地址</a></el-menu-item>
			<el-menu-item index="grzx-xmdz"><a href='https://github.com/sean10' target="_blank">项目地址</a></el-menu-item>
			<el-menu-item index="/login">退出</el-menu-item>
		  </el-submenu>
      <el-menu-item index="4">
        <router-link to="/uploads">Uploads</router-link>
      </el-menu-item>
	  </el-menu>

  </div>
</template>

<script>
export default {
	name: 'topbar',
	data() {
		return {
			num1: 1,
			activeIndex: '1',
      username: 'ttt'
		};
	},
	methods: {
		handleSelect(key, keyPath) {
			console.log(key, keyPath);
		}
	}
}
</script>

<style lang="css">
/*#topbar {*/
	/*font-family: 'Avenir', Helvetica, Arial, sans-serif;*/
	/*-webkit-font-smoothing: antialiased;*/
	/*-moz-osx-font-smoothing: grayscale;*/
	/*text-align: center;*/
	/*margin: 0 auto;*/
	/*line-height: 1.4;*/
  /*color: #2c3e50;*/
  /*!*display: flex;*!*/
  /*!*align-items: center;*!*/
  /*!*justify-content: space-between;*!*/
/*}*/

#login {
  position: fixed;
  right: 20px;
}
</style>
