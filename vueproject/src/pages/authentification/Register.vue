<template>
  <div>
    <div>
      <div>
        <div>
          <h1>Register</h1>
          <p>
            <router-link to="/login">
              Already have an account?
            </router-link>
          </p>
          <ul v-if="errors">
            <li v-for="(v, k) in errors" :key="k">{{ k }} {{ v }}</li>
          </ul>
          <form @submit.prevent="onSubmit">
            <fieldset>
              <label for="username">Username</label>
              <input
                id="username"
                type="text"
                v-model="username"
                placeholder="Username"
              />
            </fieldset>
            <fieldset>
              <input
                type="text"
                v-model="email"
                placeholder="Email"
              />
            </fieldset>
            <fieldset>
              <input
                type="password"
                v-model="password"
                placeholder="Password"
              />
            </fieldset>
            <button>
              Sign up
            </button>
          </form>
        </div>
      </div>
    </div>
  </div>

</template>
<script>
import { REGISTER } from '../../store/actions.type';
import { mapState } from 'vuex';

export default {
  data() {
    return {
      username: "",
      email: "",
      password: ""
    };
  },
  computed: {
    ...mapState({
      errors: state => state.auth.errors
    })
  },
  methods: {
    onSubmit() {
      this.$store
        .dispatch(REGISTER, {
          email: this.email,
          password: this.password,
          username: this.username
        })
        .then(() => this.$router.push({ name: "Home" }));
    }
  }
};
</script>
<style scoped>
</style>