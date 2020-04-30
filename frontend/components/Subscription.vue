<template>
  <b-container>
    <b-row>
      <b-col xs="12" lg="12" class="title text-center">
        <h3>Подпишитесь на скидки и акции</h3>
        <b-form inline class="d-inline-flex">
          <b-input
            type="text"
            size="lg"
            class="mb-2 mr-sm-2 mb-sm-0"
            placeholder="Имя"
          />
          <b-input
            type="email"
            size="lg"
            class="mb-2 mr-sm-2 mb-sm-0"
            placeholder="Email"
          />
          <button>Подписаться</button>
        </b-form>
      </b-col>
    </b-row>
  </b-container>
</template>

<style lang="scss" scoped>
.title {
    padding: 30px 0px ;
    h3 {
      color: $darkgrey;
      text-transform: uppercase;
      margin-bottom: 20px;
    }
}
input {
  font-size: 14px;
}
button {
  vertical-align: top;
  position: relative;
  display: inline-block;
  margin: 20px auto;
  padding: 12px 32px;
  background-color: $pink;
  color: #ffffff;
  text-align: center;
  text-decoration: none;
  font-size: 20px;
  line-height: 0.8;
  border: none;
  border-radius: 5px;
}
</style>
