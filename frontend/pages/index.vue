<template>
  <section>
    <Menu />
    <MiniCatalog :bouquets="bouquets" :title="title" :isShowLinkToCatalog="isShowLinkToCatalog" :isMainPage="true" />
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

export default {
  components: {
    Menu,
    MiniCatalog,
    CompanyInfo,
    Reviews,
    Subscription
  },
  async fetch ({ store }) {
    if (store.getters['bouquets/mainBouquets'].length === 0) {
      await store.dispatch('bouquets/fetchMainBouquets')
    }
  },
  data () {
    return {
      title: 'Доставка цветов',
      isShowLinkToCatalog: true
    }
  },
  computed: {
    bouquets () {
      return this.$store.getters['bouquets/mainBouquets']
    }
  }
}
</script>

<style scoped>

</style>
