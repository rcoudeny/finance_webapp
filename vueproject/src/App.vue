<template>
  <TransactionOverview />
</template>

<script>
import TransactionOverview from "./pages/transactionoverview/TransactionOverview.vue";

export default {
  name: "App",
  components: {
    TransactionOverview,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
