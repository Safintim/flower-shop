<template>
  <section class="catalog">
    <b-row class="justify-content-center">
      <b-col xs="12" lg="12" class="title text-center">
        <h3>Доставка цветов</h3>
      </b-col>
      <b-col v-for="bouquet of bouquets" :key="bouquet.id" lg="4">
        <FlowCard :bouquet="bouquet" />
      </b-col>
      <b-col md="12" class="text-center">
        <b-button class="catalog__go text-decoration-none" no-prefetch to="/catalog">Перейти в каталог</b-button>
      </b-col>
    </b-row>
  </section>
</template>
<script>

import FlowCard from '~/components/FlowCard'

export default {
  components: {
    FlowCard
  },
  props: {
    bouquets: {
      type: Array,
      default () {}
    }
  }
}
</script>

<style lang="scss">
  .title {
    padding: 30px 0px;
    h3 {
      color: $darkgrey;
      text-transform: uppercase;
    }
  }
  .catalog__go {
    margin: 30px 0px;
    font-size: 20px;
    color: white;
    text-align: center;
    border-radius: 5px;
    border: none;
    background-color: $pink;
    padding: 12px 32px;
  }
  .btn-secondary:hover, .btn-secondary:focus, .btn-secondary:active, .btn-secondary.active, .open>.dropdown-toggle.btn-secondary {
    color: #fff;
    background-color: $pink;
    border: none;
}
</style>
