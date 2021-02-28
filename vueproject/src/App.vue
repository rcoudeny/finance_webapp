<template>
  <div id="appContent">
    <div>
      <Navigation></Navigation>
      <router-view />
    </div>
    <Footer></Footer>
  </div>
</template>

<script>
import Navigation from "@/components/Navigation";
import Footer from "@/components/Footer";

export default {
  name: "App",
  components: {
    Navigation,
    Footer,
  },
};
</script>

<style>
@import "./assets/globalVariables.css";

html,
body,
#app {
  height: 100%;
  margin: 0;
  font-size: 20px;
  font-family: Helvetica Neue, Helvetica, Arial, sans-serif;
}
#appContent {
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
footer {
  flex-shrink: 0;
}
</style>
