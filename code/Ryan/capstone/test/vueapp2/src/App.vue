<template>
  <div id="app">
    <Users />
  </div>
</template>

<script>
import Users from './components/war.vue'


export default {
  name: 'app',
  components: {
    war
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
