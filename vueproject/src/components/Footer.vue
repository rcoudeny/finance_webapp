<template>
  <footer>
    <div>
      This is a finance application to manage your finances. For more
      information, sent an email to
      <a href="mailto:robbe.coudenys@gmail.com">robbe.coudenys@gmail.com</a>
    </div>
  </footer>
</template>
<script>
export default {};
</script>
<style scoped>
footer {
  padding: 80px 140px;
  background-color: var(--color-dark-brown);
  color: white;
  display: flex;
  justify-content: space-around;
}
a {
  font-weight: 700;
  color: white;
  text-decoration: none;
}
</style>