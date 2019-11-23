<template>
  <div class="dashboard">
    <ChartContainer />
    <kpi />
    <ButtonEmphasisExample :buttonName="newInvestmentButton" />
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
    }
</style>