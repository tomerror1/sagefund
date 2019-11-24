<template>
  <div class="chart">
    <div class="chart_label">Performance Graph</div>
    <line-chart :chartdata="chartdata"
                :options="options"
                v-bind:style="{ height: height + 'vh' }"
    />
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
        height: 40,
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
    },
    computed: {
    }
  }
</script>

<style>
  .chart {
    display: flex;
    flex-direction: column;
    border: 5px solid black;
    width: 40vw;
    padding: 5vh;
  }
  .chart_label{
    font-weight: 600;
    font-size: 1.5rem;
    text-decoration: underline;
    margin-bottom: 5vh;
  }
</style>