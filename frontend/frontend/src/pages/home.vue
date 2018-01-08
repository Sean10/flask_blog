<template>
	<div class="home">
	<img src="../assets/logo.png">
    <router-view></router-view>
    <el-button>默认按钮</el-button>
    <el-button type="primary">主要按钮</el-button>
    <el-button type="text">文字按钮</el-button>
    <el-input-number v-model="num1" @change="handleChange" :min="1" :max="10"></el-input-number>
    <br />
    <el-input placeholder="elinput输入框">a</el-input>
    <input placeholder="input输入框">b</input>
</div>
</template>

<script>

export default {
  name: 'home',
  data() {
      return {
        num1: 1,
      };
    },
    methods: {
      handleChange(value) {
        console.log(value);
      }
    }
}
</script>

<style>
</style>
