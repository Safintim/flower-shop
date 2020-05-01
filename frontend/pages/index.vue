<template>
  <section>
    <Menu />
    <MiniCatalog :bouquets="bouquets" />
    <CompanyInfo />
    <Reviews />
    <Subscription />
  </section>
</template>

<script>
import Menu from '~/components/Menu'
import MiniCatalog from '~/components/MiniCatalog'
import CompanyInfo from '~/components/CompanyInfo'
import Reviews from '~/components/Reviews'
import Subscription from '~/components/Subscription'

const bouquetsUrl = 'http://127.0.0.1:8000/api/bouquets/'

export default {
  components: {
    Menu,
    MiniCatalog,
    CompanyInfo,
    Reviews,
    Subscription
  },
  async asyncData ({ $axios }) {
    const response = await $axios.get(bouquetsUrl)
    const bouquets = response.data
    return { bouquets }
  }
}
</script>

<style scoped>

</style>
