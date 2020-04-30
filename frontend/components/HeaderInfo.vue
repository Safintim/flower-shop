<template>
  <header class="d-none d-md-block">
    <div>
      <b-row class="align-items-center">
        <b-col class="logo text-center" md="3" lg="2">
          <b-img-lazy src="~/assets/images/logo.png" alt="logo.png" />
        </b-col>
        <b-col class="city text-center" md="3" lg="2">
          <div class="city__title">Город доставки</div>
          <div class="city__current">Астана</div>
        </b-col>
        <b-col class="search justify-content-center" md="4" lg="4">
          <b-form>
            <b-form-input size="sm" type="search" placeholder="Поиск цветов и букетов" />
          </b-form>
        </b-col>
        <b-col class="cart text-center" md="2" lg="2">
          <div class="cart__icon">
            <nuxt-link no-prefetch active-class="active" to="/cart">
              Корзина <b-badge variant="dark">4</b-badge>
            </nuxt-link>
          </div>
        </b-col>
        <b-col class="contacts" md="12" lg="2">
          <div class="contacts__title">
            Бесплатный звонок 24/7
            Главный офис
          </div>
          <div class="contacts__phone">8-800-555-35-35</div>

        </b-col>
      </b-row>
    </div>
  </header>
</template>

<style lang="scss" scoped>
  header {
        padding: 20px 0;
        border: 1px solid $lightgrey;
  }
  .row {
    margin-right: 0;
  }
  .logo {
    img {
      max-width: 200px;
    }
  }
  .city__title {
    color: $grey;
    font-size: 14px;
  }
  .city__current {
    color: $darkgrey;
    font-size: 16px;
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
    text-align: right;
  }
  .contacts__phone {
    font-size: 20px;
    color: $darkgrey;
    text-align: right;
  }
</style>
