<template>
  <div id="app">

    <el-container>
      <el-header>
        <topbar :login="islogin"></topbar>
      </el-header>
      <el-main>
        <transition name="fade">
          <router-view @succeedLogin="changelogin"></router-view>
        </transition>
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
    components: {
      topbar,
      Footer,
    },
    data() {
      return {
        islogin: false
      }
    }
    ,
    created() {
      this.checkLogin();
    }
    ,
    methods: {
      changelogin() {
        this.islogin = true
      },
      checkLogin() {
        console.log(this.$library.state)
        //检查是否存在session
        //cookie操作方法在源码里有或者参考网上的即可
        // if (!this.getCookie('token')) {
        //   //如果没有登录状态则跳转到登录页
        //   this.$router.push('/login');
        // } else {
        //   //否则跳转到登录后的页面
        //   this.$router.push('/userInfo');
        // }
        ;
      }
      ,
      getUserInfo() {
        //发送http请求获取，这里写死作演示
        // this.userInfo = {
        //   nick: 'Doterlin',
        //   ulevel: 20,
        //   uid: '10000',
        //   portrait: 'images/profile.jpg'
        // }
        //
        // //实例开发中这里会向服务端请求数据
        // //如下(用了vue-resource):
        // /*ts.$http.get(url, {
        //   //参数
        //   "params":{}
        // }).then((response) => {
        ;
        //   //Success
        // }, (response) => {
        //   //Error
        // });*/
        //
        // //提交mutation到Store
        // this.$store.commit('updateUserInfo', this.userInfo);
      }
    }
    ,
    mounted() {
      //组件开始挂载时获取用户信息
      this.getUserInfo();
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
