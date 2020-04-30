<template>
  <footer class="px-5 pt-5 pb-4">
    <b-container>
      <b-row class="justify-content-center">
        <b-col class="logo text-center" cols="12" sm="12" md="3">
          <b-img-lazy
            src="~/assets/images/logo_footer.png"
            alt="logo_footer.png"
            class="img-fluid"
          />
          <div class="copyright">© Служба доставки цветов Flow-service, 2019</div>
        </b-col>
        <b-col class="menu text-left" cols="12" sm="12" md="1" offset-md="2">
          <div v-for="item of 5" :key="item">Цветы</div>
        </b-col>
        <b-col class="nav-footer text-left" cols="12" sm="12" md="3">
          <div>О магазине</div>
          <div>Доставка</div>
          <div>Контакты</div>
        </b-col>
        <b-col class="info text-right" cols="12" sm="12" md="3">
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
  color: white;
}
.copyright {
  font-size: 11px;
  color: $lightpink;
}
.contacts__title {
  font-size: 14px;
  color: $lightpink;
}
.contacts__phone {
  font-size: 20px;
  color: white;
}
</style>
