<template>
  <section>
    <h1>Букеты</h1>
    <ul>
      <li
        v-for="bouquet of 5"
        :key="bouquet"
      >
        <a href="#" @click.prevent="openBouquet(bouquet)">Букет {{ bouquet }}</a>
      </li>
    </ul>
  </section>
</template>

<script>
export default {
  methods: {
    openBouquet (bouquet) {
      this.$router.push('/bouquets/' + bouquet)
    }
  }
}
</script>
