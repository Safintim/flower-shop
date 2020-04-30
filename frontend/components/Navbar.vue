<template>
  <b-container fluid class="container-navbar py-2">
    <b-navbar toggleable="sm" class="py-0">
      <b-navbar-toggle target="nav-collapse" />
      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <li class="nav-item">
            <nuxt-link exact no-prefetch active-class="active" class="nav-link" to="/">Главная</nuxt-link>
          </li>
          <li class="nav-item">
            <nuxt-link exact no-prefetch active-class="active" class="nav-link" to="/about">О магазине</nuxt-link>
          </li>
          <li class="nav-item">
            <nuxt-link exact no-prefetch active-class="active" class="nav-link" to="/delivery">Доставка</nuxt-link>
          </li>
          <li class="nav-item">
            <nuxt-link exact no-prefetch active-class="active" class="nav-link" to="/contacts">Контакты</nuxt-link>
          </li>
          <li class="nav-item">
            <nuxt-link exact no-prefetch active-class="active" class="nav-link" to="/bouquets">Букеты</nuxt-link>
          </li>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </b-container>
</template>

<style lang="scss" scoped>
.container-navbar {
  background-color: $lightgrey;
  .nav-link {
    color: $grey;
    font-size: 14px;
  }
}
</style>
