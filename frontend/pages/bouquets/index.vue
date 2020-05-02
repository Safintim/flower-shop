<template>
  <MiniCatalog />
  <!-- <section>
    <h1>Букеты</h1>
    <ul>
      <li
        v-for="bouquet of 5"
        :key="bouquet"
      >
        <a href="#" @click.prevent="openBouquet(bouquet)">Букет {{ bouquet }}</a>
      </li>
    </ul>
  </section> -->
</template>

<script>

import MiniCatalog from '~/components/MiniCatalog'

export default {
  async fetch ({ store }) {
    await store.dispatch('bouquets/fetch')
  },
  components: {
    MiniCatalog
  }
  // methods: {
  //   openBouquet (bouquet) {
  //     this.$router.push('/bouquets/' + bouquet)
  //   }
  // }
}
</script>
