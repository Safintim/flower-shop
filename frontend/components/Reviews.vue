<template>
  <b-container>
    <b-row>
      <b-col cols="12" lg="12" class="title text-center my-4 py-1">
        <h3>Фото счастливых клиентов</h3>
      </b-col>
      <b-row class="justify-content-center">
        <ReviewCard v-for="photo of 10" :key="photo" cols="6" md="3" />
      </b-row>
    </b-row>
  </b-container>
</template>

<script>
import ReviewCard from '~/components/ReviewCard'

export default {
  components: {
    ReviewCard
  }
}
</script>

<style lang="scss" scoped>
h3 {
  color: $darkgrey;
  text-transform: uppercase;
}
</style>
