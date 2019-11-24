<template>
  <div id="app">
    <TransactionTable />
  </div>
</template>

<script>
// import DashBoard from './pages/DashboardPage/index'
import TransactionTable from 'transactionPage'

export default {
  name: 'app',
  components: {
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
