<template>
  <header class="d-sm-block d-md-block py-4 px-0">
    <b-container fluid>
      <b-row class="align-items-center">
        <b-col class="logo text-center" md="3" lg="2">
          <b-img-lazy src="~/assets/images/logo.png" alt="logo.png" class="img-fluid" />
        </b-col>
        <b-col class="city text-center" md="3" lg="2">
          <div class="city__title mb-1">Город доставки</div>
          <b-modal id="modal-1" size="md" title="Выберите город" :hide-footer="true">
            <b-container>
              <b-row class="justify-content-left align-items-center">
                <b-col
                  v-for="city of cities"
                  :key="city.id"
                  cols="6"
                  sm="6"
                  md="6"
                  lg="4"
                  class="city-modal p-1 text-sm-center text-md-center text-xs-center"
                  @click="selectCity(city)"
                >
                  <span class="p-2">{{ city.title }}</span>
                </b-col>
              </b-row>
            </b-container>
          </b-modal>
          <div :key="currentCity.title" v-b-modal.modal-1 class="city__current">
            <span>{{ currentCity.title }}</span>
          </div>
        </b-col>
        <b-col class="search justify-content-center" md="4" lg="4">
          <b-form>
            <b-form-input size="sm" type="search" placeholder="Поиск цветов и букетов" />
          </b-form>
        </b-col>
        <b-col class="cart text-center" md="2" lg="2">
          <div class="cart__icon">
            <nuxt-link no-prefetch active-class="active" to="/cart">
              Корзина
              <b-badge variant="dark">4</b-badge>
            </nuxt-link>
          </div>
        </b-col>
        <b-col class="contacts text-right" md="12" lg="2">
          <div class="contacts__title">
            Бесплатный звонок 24/7
            Главный офис
          </div>
          <div class="contacts__phone">8-800-555-35-35</div>
        </b-col>
      </b-row>
    </b-container>
  </header>
</template>
<script>
export default {
  computed: {
    cities () {
      return this.$store.getters['cities/cities']
    },
    currentCity () {
      return this.$store.getters['cities/currentCity']
    }
  },
  methods: {
    selectCity (city) {
      this.$bvModal.hide('modal-1')
      this.$store.commit('cities/setCurrentCity', city)
    }
  }
}
</script>
<style lang="scss" scoped>
header {
  border: 1px solid $lightgrey;
}
.row {
  margin-right: 0;
}
.city__title {
  color: $grey;
  font-size: 14px;
}
.city__current {
  color: $darkgrey;
  font-size: 16px;
  cursor: pointer;
  span {
    border-bottom: 1px dotted $darkgrey;
  }
}
.city-modal {
  color: $darkgrey;
  font-size: 16px;
  span:hover {
    background-color: $lightgrey;
    border-radius: 5px;
    cursor: pointer;
  }
}
.search {
  input {
    font-size: 14px;
  }
}
.cart__icon {
  border: 1px solid $darkgrey;
}
.contacts__title {
  font-size: 14px;
  color: $grey;
}
.contacts__phone {
  font-size: 20px;
  color: $darkgrey;
}
</style>
