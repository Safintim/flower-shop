<template>
  <section class="catalog">
    <b-container>
      <b-row class="justify-content-center">
        <b-col cols="12" lg="12" class="title text-center my-4 py-1">
          <h3>{{ title }}</h3>
        </b-col>
        <b-col v-for="bouquet of bouquets" :key="bouquet.id" sm="6" md="6" lg="4">
          <FlowCard :bouquet="bouquet" />
        </b-col>
        <b-col md="12" class="text-center">
          <b-button
            v-if="isShowLinkToCatalog"
            class="catalog__go text-decoration-none my-4 py-2 px-4"
            no-prefetch
            to="/bouquets"
          >Перейти в каталог</b-button>
        </b-col>
      </b-row>
    </b-container>
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
    },
    title: {
      type: String,
      default () {
        return 'Каталог'
      }
    },
    isShowLinkToCatalog: {
      type: Boolean,
      default () {
        return false
      }
    }
  }
}
</script>

<style lang="scss">
h3 {
  color: $darkgrey;
  text-transform: uppercase;
}
.catalog__go {
  font-size: 20px;
  color: white;
  text-align: center;
  border-radius: 5px;
  border: none;
  background-color: $pink;
}
</style>
