<template>
<h1>{{ count }}</h1>
  <div class="wrapper">
    The reasoning behind how this web application is built, is descended from
    the book 'Rich dad, poor dad'. There, everything is either an asset or a
    liability (hence the name, LiAsset). On the assets, you can determine the
    ROI by filling in your current value. Then the average ROI on that category
    gets calculated based on when what amount was deposited.
  </div>

</template>
<script>
import { computed } from 'vue';
import { useStore } from 'vuex';

export default {
  setup(){
    const store = useStore();

    const count = computed(() => store.state.count);
    return {
      count
    }
  }
};
</script>
<style scoped>
.wrapper {
  background-color: var(--primary-color);
}
</style>