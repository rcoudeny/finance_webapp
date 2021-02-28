<template>
  <div>
    <div>
      <div>
        <div>
          <h1>Log in</h1>
          <p>
            <router-link to="/register">
              Need an account?
            </router-link>
          </p>
          <ul v-if="errors">
            <li v-for="(v, k) in errors" :key="k">{{ k }} {{ v }}</li>
          </ul>
          <form @submit.prevent="onSubmit(email, password)">
            <fieldset>
              <input
                type="text"
                v-model="email"
                placeholder="Email"
              />
            </fieldset>
            <fieldset class="form-group">
              <input
                type="password"
                v-model="password"
                placeholder="Password"
              />
            </fieldset>
            <button>
              Sign in
            </button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { mapState } from "vuex";
import { LOGIN } from "@/store/actions.type";

export default {
  data() {
    return {
      email: null,
      password: null
    };
  },
  methods: {
    onSubmit(email, password) {
      this.$store
        .dispatch(LOGIN, { email, password })
        .then(() => this.$router.push({ name: "Home" }));
    }
  },
  computed: {
    ...mapState({
      errors: state => state.auth.errors
    })
  }
};
</script>
<style scoped>
</style>