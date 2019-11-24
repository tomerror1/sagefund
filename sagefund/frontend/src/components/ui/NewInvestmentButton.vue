<template lang="html">
  <div class="investment_button">
    <sui-button primary v-bind:style="{fontSize: style+'rem'}"> +  {{ buttonName }}</sui-button>
  </div>
</template>

<script>
export default {
  name: 'ButtonEmphasisExample',
  data: function() {
      return {
      }
  },
  props: {
    buttonName: {
      type: String,
      default: null
    },
  },
  computed: {
    style: function(){
      return 1.2
    }
  }
};
</script>

<style >
.primary{
  font-size: 1.2rem;
}
</style>