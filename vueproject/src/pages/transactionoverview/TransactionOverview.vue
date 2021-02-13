<template>
  <h1>Hoi</h1>
</template>

<script>
import axios from "axios";

export default {
  name: "TransactionOverview",
  data() {
    return {
      category: axios
        .get("https://localhost:5001/api/Category")
        .then((response) => response),
    };
  },
  mounted() {},
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
