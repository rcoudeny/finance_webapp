<template>
  <div v-if="mainCategory" class="wrapper">
    <div>{{ mainCategory.name }}</div>
    <div v-for="(transaction, index) in mainCategory.transactions" :key="index">
      <Transaction :transaction="transaction"></Transaction>
    </div>
  </div>
  <div v-else>Het is aan het laden wi</div>
</template>
<script>
import Transaction from "@/pages/transactionspage/components/Transaction";
import { SET_MAIN_CATEGORY } from '../../store/actions.type';
import { useStore } from 'vuex';

export default {
  components: {
    Transaction,
  },
  computed: {
    mainCategory () {
      return this.$store.getters.mainCategory;
    }
  },
  setup(){
    var store = useStore();
    if(!store.state.mainCategory){
      store.dispatch(SET_MAIN_CATEGORY);
    }
  },
};
</script>
<style scoped>
.wrapper {
  margin: 20px;
}
</style>