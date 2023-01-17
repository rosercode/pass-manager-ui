<template>
  <div>
    <el-header></el-header>
    <el-main>
      <el-row :gutter="20">
        <el-col :span="2"><div class="grid-content bg-purple"></div></el-col>
        <el-col :span="20"><div class="grid-content bg-purple">
          <HelloWorld msg="Welcome to Your Vue.js App"/>
        </div></el-col>
        <el-col :span="2"><div class="grid-content bg-purple"></div></el-col>
      </el-row>
    </el-main>
    <el-footer></el-footer>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'App',
  components: {
    HelloWorld
  }
}
</script>


<style>

.el-col {
  border-radius: 4px;
}

.grid-content {
  border-radius: 4px;
  min-height: 36px;
}

</style>
