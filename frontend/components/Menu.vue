<template>
  <div class="menu">
    <b-navbar toggleable="lg">
      <b-navbar-toggle target="nav-collapse2" />
      <b-collapse id="nav-collapse2" is-nav>
        <b-navbar-nav>
          <b-nav-item-dropdown class="mr-2" text="Цветы">
            <b-dropdown-item href="#">EN</b-dropdown-item>
            <b-dropdown-divider />
            <b-dropdown-item class="mr-2" href="#">EN</b-dropdown-item>
          </b-nav-item-dropdown>
          <b-nav-item-dropdown class="mr-2" text="Композиции">
            <b-dropdown-item href="#">EN</b-dropdown-item>
            <b-dropdown-divider />
            <b-dropdown-item href="#">EN</b-dropdown-item>
          </b-nav-item-dropdown>
          <b-nav-item-dropdown class="mr-2" text="Повод">
            <b-dropdown-item href="#">EN</b-dropdown-item>
            <b-dropdown-divider />
            <b-dropdown-item href="#">EN</b-dropdown-item>
          </b-nav-item-dropdown>
          <b-nav-item-dropdown class="mr-2" text="Подарки">
            <b-dropdown-item href="#">EN</b-dropdown-item>
            <b-dropdown-divider />
            <b-dropdown-item href="#">EN</b-dropdown-item>
          </b-nav-item-dropdown>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>

<style lang="scss" scoped>
  .menu {
    padding: 6px 0;
    border-bottom: 1px solid $lightgrey;
    .navbar {
      padding: 0 1rem;
    }
  }
  ::v-deep .nav-link {
   color: $darkgrey!important;
   font-size: 16px;
}
</style>
