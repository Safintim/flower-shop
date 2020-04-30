<template>
  <b-container>
    <b-row>
      <b-col xs="12" lg="12" class="title text-center">
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
.title {
  padding: 30px 0px;
  h3 {
    color: $darkgrey;
    text-transform: uppercase;
  }
}
</style>
