<template>
<div class="signup">
	<section class="login-wrapper">
		<div class="login-content">
			<el-input placeholder="请输入用户名" name="username" class="username" v-model="username">{{ username }}</el-input>
			<el-input placeholder="请输入密码" name="password1" type="password" class="password" v-model="password1" >{{ password1 }}</el-input>
      <el-input placeholder="请重复密码" name="password2" type="password" class="password" v-model="password2" @keyup.enter.native="login">{{ password2 }}</el-input>
			<a class="submit" href="javascript:;" @click="signup">注册</a>
		</div>
	</section>
</div>
</template>

<script>
export default {
  data: function () {
    return {
      username: "",
      password1: "",
      password2: ""
    }
  },
	methods: {
		// 模拟登录
		signup() {
		  var qs = require('qs');
			if (this.username && this.password2) {
			  this.$axios.post("/author/api/signup",qs.stringify({'username':this.username,'password':this.password2})).then(
			    response => {
			      console.log(response.data)
            if (response.data)
            {
              // console.log(this.username)
              // console.log(this.$library.state.uid )
              // this.$library.state.uid = this.username
              // this.$library.state.islogin = true;
              // this.$emit("succeedLogin")
              this.$router.push("/login");
              console.log("succeed signup")
              // this.username = ""
              // this.password = ""
            }
          }
        )
				// this.$store
				// 	.dispatch("login", "tokenvalue" + Math.random(1000))
				// 	.then(() => {
				// 		this.$router.push("/home");
				// 	});
			} else {
				this.$message({
					message: "请输入用户名和密码",
					type: "warning",
					showClose: false
				});
			}
		}
	}
};
</script>

<style>
.signup {
	width: 100%;
	height: 100%;
	filter: progid:DXImageTransform.Microsoft.gradient( startColorstr=#00a597,
	endColorstr=#FFFFFFFF,
	GradientType=0);
	background-color: #00a597;
	background: linear-gradient(to bottom, #00a597 45%, #fff 45%, #fff 100%);
	position: relative;
	.login-wrapper {
		position: absolute;
		top: 50%;
		left: 50%;
		-webkit-transform: translate(-50%, -50%);
		transform: translate(-50%, -50%);
		width: 650px;
		height: 500px;
		background: #fff;
		border: 1px solid #ccc;
		padding: 0 30px;
		h1 {
			height: 73px;
			line-height: 72px;
			text-align: center;
			font-size: 30px;
		}
		.login-content {
			margin: 20px 95px 0;
			border-bottom: 1px solid #ccc;
			overflow: hidden;
			input {
				display: block;
				width: 100%;
				margin-top: 30px;
				background: #f8f8f8;
			}
		}
		.submit {
			display: block;
			height: 45px;
			text-align: center;
			line-height: 45px;
			border-radius: 6px;
			background: $--color--primary;
			color: #fff;
			font-size: 16px;
			margin: 30px 0;
		}
	}
}
</style>
