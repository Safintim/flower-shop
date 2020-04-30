<template>
  <footer>
    <b-container>
      <b-row class="justify-content-center">
        <b-col class="logo text-center" xs="12" sm="12" md="3">
          <b-img-lazy src="~/assets/images/logo_footer.png" alt="logo_footer.png" />
          <div class="copyright">© Служба доставки цветов Flow-service, 2019</div>
        </b-col>
        <b-col class="menu text-right" xs="12" sm="12" md="3">
          <div v-for="item of 5" :key="item">
            Цветы
          </div>
        </b-col>
        <b-col class="nav-footer text-left" right xs="12" sm="12" md="3">
          <div>О магазине</div>
          <div>Доставка</div>
          <div>Контакты</div>
        </b-col>
        <b-col class="info text-right" xs="12" sm="12" md="3">
          <div class="contacts__title">
            Бесплатный звонок 24/7
            Главный офис
          </div>
          <div class="contacts__phone">8-800-555-35-35</div>
        </b-col>
      </b-row>
    </b-container>
  </footer>
</template>

<style lang="scss" scoped>
footer {
  background-color: $pink;
  padding: 50px;
  color: white;
}
.logo {
  img {
    max-width: 100%;
    vertical-align: middle;
  }
}
.copyright {
  font-size: 11px;
}
.contacts__title {
    font-size: 14px;
    color: $grey;
    text-align: right;
  }
  .contacts__phone {
    font-size: 20px;
    color: white;
    text-align: right;
  }
</style>
