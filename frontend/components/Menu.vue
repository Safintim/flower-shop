<template>
  <b-container fluid>
    <div class="menu py-2">
      <b-navbar toggleable="sm" class="py-0">
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
  </b-container>
</template>

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
