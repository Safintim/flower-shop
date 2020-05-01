<template>
  <b-container>
    <b-row>
      <b-col xs="12" lg="12" class="title text-center my-5 py-1">
        <h3>Подпишитесь на скидки и акции</h3>
        <b-form inline class="d-inline-flex d-sm-block">
          <b-input type="text" size="lg" class="mb-2 mr-sm-2 mb-sm-0" placeholder="Имя" />
          <b-input type="email" size="lg" class="mb-2 mr-sm-2 mb-sm-0" placeholder="Email" />
          <button class="py-2 px-3 my-sm-3 mx-auto">Подписаться</button>
        </b-form>
      </b-col>
    </b-row>
  </b-container>
</template>

<style lang="scss" scoped>
h3 {
  color: $darkgrey;
  text-transform: uppercase;
}

input {
  font-size: 14px;
  vertical-align: middle;
}
button {
  vertical-align: top;
  position: relative;
  display: inline-block;
  background-color: $pink;
  color: #ffffff;
  text-align: center;
  text-decoration: none;
  vertical-align: middle;
  font-size: 20px;
  line-height: 1.5;
  border: none;
  border-radius: 5px;
}
</style>
