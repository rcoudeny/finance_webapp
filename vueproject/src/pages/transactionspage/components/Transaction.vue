<template>
  <table
    class="transaction"
    v-bind:class="
      transaction.amount > 0 ? 'background-green' : 'background-red'
    "
  >
    <tr>
      <th>Date</th>
      <td>{{ convertDate(transaction.date) }}</td>
    </tr>
    <tr>
      <th>Amount</th>
      <td>{{ convertAmount(transaction.amount) }}</td>
    </tr>
    <tr>
      <th>Comment</th>
      <td>{{ transaction.comment }}</td>
    </tr>
    <tr>
      <th>Opponent Name</th>
      <td>{{ transaction.opponentName }}</td>
    </tr>
    <tr>
      <th>Opponent Account</th>
      <td>{{ transaction.opponentAccount }}</td>
    </tr>
    <tr>
      <th>Account</th>
      <td>{{ transaction.ownAccount }}</td>
    </tr>
  </table>
</template>
<script>
import moment from "moment";
export default {
  props: {
    transaction: {
      date: Date,
      amount: Number,
      opponentName: String,
      opponentAccount: String,
      comment: String,
      ownAccount: String,
    },
  },
  methods: {
    convertDate(date) {
      return moment(date).format("MMMM [the] Do YYYY");
    },
    convertAmount(amount) {
      return "€ " + parseFloat(amount).toFixed(2);
    },
  },
};
</script>
<style scoped>
table > tr > th {
  text-align: left;
  width: 40%;
}
.background-red {
  background-color: red;
}
.background-green {
  background-color: green;
}
.transaction {
  color: white;
  border: 2px solid black;
  padding: 10px;
  margin: 20px 0;
  width: 100%;
}
</style>