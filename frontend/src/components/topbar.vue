<template lang="html">
  <div id="topbar">
    <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect"
             background-color="#545c64" text-color="#fff" active-text-color="#ffd04b">
      <el-menu-item index="1">
        <router-link to="/todo">TodoList</router-link>
      </el-menu-item>
      <el-menu-item index="2">
        <router-link to="/about">About</router-link>
      </el-menu-item>

      <template v-if="!login" v-model="login">
      <el-menu-item index="-1" id="login" class="el-footer" >
        <router-link to="/login">登录</router-link>
      </el-menu-item>
      </template>
      <template v-else>
      <el-submenu index="4" class="el-footer" id="login2">
          <div slot="title" v-model="username">{{ username }}</div>
          <!--<el-menu-item index="grzx-bky"><a href='http://sean10.github.io' target="_blank">博客地址</a></el-menu-item>-->
          <!--<el-menu-item index="grzx-xmdz"><a href='https://github.com/sean10' target="_blank">项目地址</a></el-menu-item>-->
          <el-menu-item index="\login" @click="logout">退出</el-menu-item>
      </el-submenu>
      </template>
    </el-menu>

  </div>
</template>

<script>
  export default {
    name: 'topbar',
    data() {
      return {
        activeIndex: '1',
        username: this.$library.state.uid,
        // islogin: this.$library.state.islogin
        // username: "sean10"
      };
    },
    props: ['login'],
    methods: {
      handleSelect(key, keyPath) {
        console.log(key, keyPath);
      },
      logout() {
        this.$delCookie("token")
        this.$library.state.islogin = false
        this.$router.push("/login")
        console.log("logout")
      }
    }
  }
</script>

<style lang="css">
  #topbar {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    margin: 0 auto;
    line-height: 1.4;
    color: #2c3e50;
    /*display: flex;*/
    /*align-items: center;*/
    /*justify-content: space-between;*/
  }

  #login {
    position: fixed;
    right: 50px;
  }
  #login2 {
    position: fixed;
    right: 50px;
  }
</style>
