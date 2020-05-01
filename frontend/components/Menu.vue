<template>
  <b-container fluid>
    <div class="menu py-2">
      <b-navbar toggleable="sm" class="py-0">
        <b-navbar-toggle target="nav-collapse2" />
        <b-collapse id="nav-collapse2" is-nav>
          <b-navbar-nav>
            <b-nav-item-dropdown v-for="category in categories" :key="category.id" class="mr-2" v-bind:text="category.title">
              <b-dropdown-item v-for="child in category.children" :key="child.id" href="#">{{ child.title }}</b-dropdown-item>
              <b-dropdown-divider />
              <b-dropdown-item class="mr-2" href="#">Все</b-dropdown-item>
            </b-nav-item-dropdown>
          </b-navbar-nav>
        </b-collapse>
      </b-navbar>
    </div>
  </b-container>
</template>

<script>
export default {
  computed: {
    categories () {
      return this.$store.getters['categories/categories']
    }
  }
}
</script>

<style lang="scss" scoped>
.menu {
  border-bottom: 1px solid $lightgrey;
}
::v-deep .nav-link {
  color: $darkgrey !important;
  font-size: 16px;
}
@media (max-width: 768px) {
  .container {
    width: 100%;
    max-width: none;
  }
}
</style>
