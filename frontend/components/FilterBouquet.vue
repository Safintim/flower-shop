<template>
  <b-container>
    <b-row class="justify-content-between">
      <b-col cols="3" md="3" lg="3" class="box text-uppercase">
        <b-nav-item-dropdown size="md" id="dropdown-form" text="Цена" ref="dropdown" class="m-2">
          <b-dropdown-form>
            <b-form-group>
              <b-form-radio name="price" class="mb-3">до 2000</b-form-radio>
              <b-form-radio name="price" class="mb-3">2000 - 3500</b-form-radio>
              <b-form-radio name="price" class="mb-3">3500 - 5000</b-form-radio>
              <b-form-radio name="price">от 5000</b-form-radio>
            </b-form-group>
          </b-dropdown-form>
        </b-nav-item-dropdown>
      </b-col>
      <b-col cols="3" md="3" lg="3" class="box text-uppercase">
        <b-nav-item-dropdown id="dropdown-form" size="md" text="Цена" ref="dropdown" class="m-2">
          <b-dropdown-form>
            <b-form-group>
              <b-form-radio name="price" class="mb-3">до 2000</b-form-radio>
              <b-form-radio name="price" class="mb-3">2000 - 3500</b-form-radio>
              <b-form-radio name="price" class="mb-3">3500 - 5000</b-form-radio>
              <b-form-radio name="price">от 5000</b-form-radio>
            </b-form-group>
          </b-dropdown-form>
        </b-nav-item-dropdown>
      </b-col>
      <b-col cols="3" md="3" lg="3" class="box text-uppercase">
        <b-nav-item-dropdown size="md" id="dropdown-form" text="Цена" ref="dropdown" class="m-2">
          <b-dropdown-form>
            <b-form-group>
              <b-form-radio name="price" class="mb-3">до 2000</b-form-radio>
              <b-form-radio name="price" class="mb-3">2000 - 3500</b-form-radio>
              <b-form-radio name="price" class="mb-3">3500 - 5000</b-form-radio>
              <b-form-radio name="price">от 5000</b-form-radio>
            </b-form-group>
          </b-dropdown-form>
        </b-nav-item-dropdown>
      </b-col>
      <b-col cols="3" md="3" lg="3" class="box text-uppercase">
        <b-nav-item-dropdown size="md" id="dropdown-form" text="Цена" ref="dropdown" class="m-2">
          <b-dropdown-form>
            <b-form-group>
              <b-form-radio name="price" class="mb-3">до 2000</b-form-radio>
              <b-form-radio name="price" class="mb-3">2000 - 3500</b-form-radio>
              <b-form-radio name="price" class="mb-3">3500 - 5000</b-form-radio>
              <b-form-radio name="price">от 5000</b-form-radio>
            </b-form-group>
          </b-dropdown-form>
        </b-nav-item-dropdown>
      </b-col>
    </b-row>
  </b-container>
</template>

<style lang="scss" scoped>
.row {
  background-color: $lightlightpink;
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
  font-size: 16px;
}
.dropdown-toggle::after {
  position: absolute;
  top: 50%;
  right: 0px;
}
</style>
