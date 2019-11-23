<template lang="html">
  <div>
    <sui-button primary> +  {{ buttonName }}</sui-button>
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
};
</script>