<template>
    <div id="kpi-container">
        <div class="kpi-container_heading">KPI</div>
        <div class="portfolio">
            <div class="portfolio_label">Portfolio Value</div>
            <div class="portfolio_value">‎€ {{ currentValue }}</div>
        </div>
        <div class="yield">
            <div class="yield_euro">
                <div class="yield_euro_label">Yield in Euro</div>
                <div class="yield_euro_value">{{ calculateEuroYield }}</div>
            </div>
            <div class="yield_percentage">
                <div class="yield_percentage_label">Yield %</div>
                <div class="yield_percentage_value">{{ calculatePercentageYield }}</div>
            </div> 
        </div>   
    </div>
</template>

<script>
export default {
    data: function() {
        return {
            previousValue: 1000,
            currentValue: 1200,
        }
    },
    methods: {
        valueDifference: function(oldValue, newValue){
            return newValue - oldValue
        }
    },
    computed: {
        calculateEuroYield: function() {
            let diff = this.valueDifference(this.currentValue, this.previousValue);
            return diff
        },
        calculatePercentageYield: function() {
            let diff = this.valueDifference(this.currentValue, this.previousValue);
            return ((diff/this.previousValue) *100)
        },
    },
    components: {

    }
}
</script>

<style scoped>

</style>