<template>
  <MiniCatalog :bouquets="bouquets" />
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

const bouquetsUrl = 'http://127.0.0.1:8000/api/bouquets/'

export default {
  components: {
    MiniCatalog
  },
  async asyncData ({ $axios }) {
    const bouquets = await $axios.$get(bouquetsUrl)
    return { bouquets }
  }
  // methods: {
  //   openBouquet (bouquet) {
  //     this.$router.push('/bouquets/' + bouquet)
  //   }
  // }
}
</script>
