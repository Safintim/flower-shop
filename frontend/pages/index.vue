<template>
  <section>
    <Menu />
    <MiniCatalog />
    <CompanyInfo />
  </section>
</template>

<script>
import Menu from '~/components/Menu'
import MiniCatalog from '~/components/MiniCatalog'
import CompanyInfo from '~/components/CompanyInfo'

export default {
  components: {
    Menu,
    MiniCatalog,
    CompanyInfo
  }
}
</script>

<style scoped>

</style>
