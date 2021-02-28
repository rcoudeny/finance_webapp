<template>
  <nav>
    <div id="logo">
      <router-link class="link" to="/">LiAsset</router-link>
    </div>
    <div id="navbar">
      <router-link class="link" to="/about">About</router-link>
      <router-link v-if="isLoggedIn()" class="link" to="/transactions"
        >Transactions</router-link
      >
      <router-link class="link" to="/login">Log in</router-link>
      <span class="link">|</span>
      <router-link class="link" to="/register">Register</router-link>
    </div>
  </nav>
</template>
<script>
import ApiService from "../api/api.service";

export default {
  methods: {
    isLoggedIn: function () {
      return ApiService.isLoggedIn();
    },
  },
};
</script>
<style scoped>
.link {
  color: white;
  text-decoration: none;
}
nav {
  background-color: var(--color-dark-brown);
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 20px;
}
#logo {
  color: white;
  font-weight: 700;
  padding-left: 50px;
  font-size: 50px;
}
#navbar > *:not(span) {
  margin: 20px;
}
</style>