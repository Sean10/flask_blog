<template>
  <div class="upload_view">
  <upload></upload>
</div>
</template>

<script>
  import Upload from '../components/upload.vue'

    export default {
        name: "upload_view",
      components: {
          Upload
      },
      // props: {
      //     type: object,
      //     required: true
      // }
    }
</script>

<style scoped>

</style>
