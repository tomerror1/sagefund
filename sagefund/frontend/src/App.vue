<template>
  <div id="app">
    <DashBoard />
    <TransactionTable />
  </div>
</template>

<script>
import DashBoard from './pages/DashboardPage/index'
import TransactionTable from './pages/TransactionPage/index'

export default {
  name: 'app',
  components: {
    DashBoard,
    TransactionTable
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
