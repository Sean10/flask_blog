<template>
  <div class="Foot">
    Copyright &copy; {{getYear}} <a target="_blank" href="http://sean10.github.io">sean10</a>. All rights reserved.
    <span class="r pr10">
      <a target="_blank" href="https://github.com/sean10l/flask_blog/issues">反馈建议</a>V0.1
    </span>
  </div>
</template>

<script>
  export default {
    name: "footerM",
    computed: {
      getYear() {
        let y = new Date().getFullYear();
        let showY = y;
        if (y > 2017) {
          showY = "2017-" + y;
        }
        return showY;
      }
    }
  }
</script>

<style>
  .Foot {
    position: absolute;
    bottom: 0;
    width: 100%;
    height: 20px;
  }
</style>
