<template>
  <b-container>
    <b-row class="justify-content-between">
      <b-col cols="3" md="3" lg="3" class="box text-uppercase">
        <b-nav-item-dropdown size="md" id="dropdown-form" text="Цена" ref="dropdown" class="m-2">
          <b-dropdown-form>
            <b-form-group class="text-capitalize">
              <b-form-radio name="price" value="0,2000" class="mb-3" @change="changePrice">до 2000</b-form-radio>
              <b-form-radio name="price" value="2000,3500" class="mb-3" @change="changePrice">2000 - 3500</b-form-radio>
              <b-form-radio name="price" value="3500,5000" class="mb-3" @change="changePrice">3500 - 5000</b-form-radio>
              <b-form-radio name="price" value="5000,1000000" @change="changePrice">от 5000</b-form-radio>
            </b-form-group>
          </b-dropdown-form>
        </b-nav-item-dropdown>
      </b-col>
      <b-col cols="3" md="3" lg="3" class="box text-uppercase">
        <b-nav-item-dropdown id="dropdown-form" size="md" text="Повод" ref="dropdown" class="m-2">
          <b-dropdown-form>
            <b-form-group class="text-capitalize">
              <b-form-checkbox name="category" class="mb-3">до 2000</b-form-checkbox>
              <b-form-checkbox name="category" class="mb-3">2000 - 3500</b-form-checkbox>
              <b-form-checkbox name="category" class="mb-3">3500 - 5000</b-form-checkbox>
              <b-form-checkbox name="category">от 5000</b-form-checkbox>
            </b-form-group>
          </b-dropdown-form>
        </b-nav-item-dropdown>
      </b-col>
      <b-col cols="3" md="3" lg="3" class="box text-uppercase">
        <b-nav-item-dropdown size="md" id="dropdown-form" text="Цвет" ref="dropdown" class="m-2">
          <b-dropdown-form class="text-capitalize">
            <b-form-group>
              <b-form-checkbox name="color" class="mb-3" value="SOFT" @change="changeColor">Нежный</b-form-checkbox>
              <b-form-checkbox name="color" class="mb-3" value="BRIGHT" @change="changeColor">Яркий</b-form-checkbox>
            </b-form-group>
          </b-dropdown-form>
        </b-nav-item-dropdown>
      </b-col>
      <b-col cols="3" md="3" lg="3" class="box text-uppercase">
        <b-nav-item-dropdown size="md" id="dropdown-form" text="Букет с" ref="dropdown" class="m-2">
          <b-dropdown-form class="text-capitalize">
            <b-form-group>
              <b-form-checkbox name="bouquets__flowers__id" class="mb-3">до 2000</b-form-checkbox>
              <b-form-checkbox name="bouquets__flowers__id" class="mb-3">2000 - 3500</b-form-checkbox>
              <b-form-checkbox name="bouquets__flowers__id" class="mb-3">3500 - 5000</b-form-checkbox>
              <b-form-checkbox name="bouquets__flowers__id">от 5000</b-form-checkbox>
            </b-form-group>
          </b-dropdown-form>
        </b-nav-item-dropdown>
      </b-col>
    </b-row>
  </b-container>
</template>
<script>
export default {
  methods: {
    changePrice (target) {
      this.$store.dispatch('bouquets/filterByPrice', target)
    },
    changeColor (target) {
      this.$store.dispatch('bouquets/filterByColor', target)
      console.log(target)
    }
  }
}
</script>
<style lang="scss" scoped>
.row {
  background-color: $lightgrey;
  border-radius: 8px;
}
.box {
  cursor: pointer;
  font-size: 16px;
  letter-spacing: .5px;
  border-right:1px solid white;
  position: relative;
}

::v-deep .nav-link {
  color: $grey !important;
  font-size: 12px;
}
.dropdown-toggle::after {
  position: absolute;
  top: 50%;
  right: 0px;
}
</style>
