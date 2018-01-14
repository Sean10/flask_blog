<template>
<div id="app">

<el-container>
  <el-header>	<topbar></topbar>
  </el-header>
  <el-main>
    <router-view></router-view>
  </el-main>
  <el-footer>
    <Footer></Footer>
  </el-footer>
</el-container>


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
import topbar from './components/topbar.vue'
import Footer from './components/footer.vue'

export default {
	components:{
		topbar,
    Footer,
	}
}
</script>

<style>
*,
*::before,
*::after {
	box-sizing: border-box;
}
</style>
