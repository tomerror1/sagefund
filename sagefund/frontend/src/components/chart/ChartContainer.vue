<template>
  <div class="small">
    <line-chart :chartdata="chartdata"
                :options="options"/>
    
  </div>
</template>

<script>
  import LineChart from './LineChart'

  export default {
    components: {
      LineChart
    },
    data () {
      return {
        chartdata: {
          labels: ['1','2','3','4','5','6','7'],
          datasets: [
            {
              data: [10, 12, 8, 19, 25, 50, 20],
              fill: false,
            }
          ]
        },
        options: {
          legend:{
            display: false
          },
          responsive: true,
          maintainAspectRatio: false,
          scales: {
            xAxes: [{
                gridLines: {
                    display: true
                }
            }],
            yAxes: [{
                gridLines: {
                    display: true
                }   
            }]
          }
        }
      }
    },
    mounted () {

    },
    methods: {
    }
  }
</script>

<style>
  .small {
    width: 50%;
  }
</style>