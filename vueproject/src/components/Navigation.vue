<template>
  <nav>
    <div id="logo">
      <router-link class="link" to="/">LiAsset</router-link>
    </div>
    <div id="navbar">
      <router-link class="link" to="/about">About</router-link>
      <router-link v-if="currentUser.token" class="link" to="/transactions"
        >Transactions</router-link
      >
      <router-link v-if="!currentUser.token" class="link" to="/login">Log in</router-link>
      <span v-if="!currentUser.token" class="link">|</span>
      <router-link v-if="!currentUser.token" class="link" to="/register">Register</router-link>
      <a v-if="currentUser.token" class="link" v-on:click="logout()">Logout</a>
    </div>
  </nav>
</template>
<script>
import {mapGetters} from 'vuex';
import { LOGOUT } from '../store/actions.type';

export default {
  computed: {
    ...mapGetters(["currentUser", "isAuthenticated"])
  },
  methods: {
    logout: function(){
      this.$store.dispatch(LOGOUT);
    }
  },
};
</script>
<style scoped>
a{
  cursor: pointer;
}
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