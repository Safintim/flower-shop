<template>
  <b-container>
    <b-row class="no-gutters">
      <b-col cols="12" lg="12" class="title text-center my-4 py-1">
        <h3>Познакомимся ближе</h3>
      </b-col>
      <b-col lg="6" sm="12">
        <div class="about__text pl-5 py-4 pr-0">
          <p>Создавая интернет магазин цветов, мы хотели, чтобы любимые люди, даже находясь на огромном расстоянии друг от друга, всегда имели возможность порадовать того, кто дорог, заставить близкого человека улыбнуться и почувствовать себя значимым и нужным.</p>
          <p>Наш сервис позволяет быстро, удобно, недорого и просто обрадовать близкого человека. Оформить заказ через интернет на нашем сайте вы можете круглосуточно 7 дней в неделю. На оформление уйдет не более 5 минут. Мы сделаем, все возможное, чтобы обрадовать ваших близких.</p>
          <p>Каждый день мы получаем более 330 улыбок и радостных слов благодарности. Это самое лучшее вознаграждение за непростую, но очень приятную работу.</p>
        </div>
      </b-col>
      <b-col lg="6" sm="12" class="align-self-center">
        <div class="about__img text-center">
          <b-img-lazy fluid src="~/assets/images/flower_about.jpg" alt="flower_about.jpg" />
        </div>
      </b-col>
      <b-col cols="12" lg="12" class="title text-center my-4 py-1">
        <h3>Почему выбирают наc</h3>
        <b-row>
          <b-col cols="12" lg="4">
            <div class="icon d-lg-inline-block d-sm-block mx-auto">
              <i class="fa fa-shopping-cart" aria-hidden="true" />
            </div>
            <div
              class="icon_text text-lg-left text-sm-center d-lg-inline-block d-sm-block mx-auto mt-3"
            >
              <h3 class="mb-0 p-0">Большой ассортимент</h3>
              <p>Цветы на любой вкус и текст</p>
            </div>
          </b-col>
          <b-col cols="12" lg="4">
            <div class="icon d-lg-inline-block d-sm-block mx-auto">
              <i class="fa fa-truck" aria-hidden="true" />
            </div>
            <div
              class="icon_text text-lg-left text-sm-center d-lg-inline-block d-sm-block mx-auto mt-3"
            >
              <h3 class="mb-0 p-0">Оперативная доставка</h3>
              <p>Найдем курьера за 5 минут</p>
            </div>
          </b-col>
          <b-col cols="12" lg="4">
            <div class="icon d-lg-inline-block d-sm-block mx-auto">
              <i class="fa fa-trophy" aria-hidden="true" />
            </div>
            <div
              class="icon_text text-lg-left text-sm-center d-lg-inline-block d-sm-block mx-auto mt-3"
            >
              <h3 class="mb-0 p-0">Гарантия качества</h3>
              <p>Множество счастливых клиентов</p>
            </div>
          </b-col>
        </b-row>
      </b-col>
    </b-row>
  </b-container>
</template>

<style lang="scss">
h3 {
  color: $darkgrey;
  text-transform: uppercase;
}

.about__text {
  height: 100%;
  color: $darkgrey;
  border: 1px solid $lightgrey;
}
.icon {
  vertical-align: middle;
  width: 20%;
  font-size: 3.5em;
  color: $pink;
}
.icon_text {
  width: 75%;
  vertical-align: -webkit-baseline-middle;
  h3 {
    font-size: 1em;
    font-weight: 700;
  }
}
</style>
