<template>
  <div id="app">
    <DashBoard></DashBoard>
  </div>
</template>

<script>
import DashBoard from './pages/DashboardPage/index'

export default {
  name: 'app',
  components: {
    DashBoard
  }
}
</script>

<style>
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: Arial, Helvetica, sans-serif;
}
</style>
