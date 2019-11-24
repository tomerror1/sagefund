<template>
  <div class="dashboard">
    <div class="dashboard_stats">
      <ChartContainer />
      <kpi />
    </div>
    <ButtonEmphasisExample class="investment-button" :buttonName="newInvestmentButton" />
  </div>
</template>

<script>

import ChartContainer from '../../components/chart/ChartContainer'
import kpi from '../../components/kpi/KpiContainer'
import ButtonEmphasisExample from '../../components/ui/NewInvestmentButton'

export default {
  name: 'DashBoard',
  data: function() {
      return {
          newInvestmentButton: 'New Investment'
      }
  },
  props: {
    msg: String
  },
  components: {
    ChartContainer,
    kpi,
    ButtonEmphasisExample
  }
}
</script>

<style scoped>
    .dashboard{
        width: 100%;
        display: flex;
        flex-direction: column;
    }
    .dashboard_stats{
      display: flex;
      justify-content: space-around;
    }
    .investment-button{
      margin-left: 5vw;
      margin-top: 10vh;
    }
</style>