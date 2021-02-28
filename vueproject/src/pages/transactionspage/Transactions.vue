<template>
  <div v-if="category" class="wrapper">
    <div>{{ category.name }}</div>
    <div v-for="(transaction, index) in category.transactions" :key="index">
      <Transaction :transaction="transaction"></Transaction>
    </div>
  </div>
  <div v-else>Het is aan het laden wi</div>
</template>
<script>
import Transaction from "@/pages/transactionspage/components/Transaction";
import { useStore } from 'vuex';
import { computed } from 'vue';

export default {
  components: {
    Transaction,
  },
  setup(){
    const store = useStore();
    const category = computed(() => store.state.mainCategory);
    if(!store.state.mainCategory.name){
      store.commit("setMainCategory");
    }
    return {
      category
    }
  },
};
</script>
<style scoped>
.wrapper {
  margin: 20px;
}
</style>