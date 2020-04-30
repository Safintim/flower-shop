<template>
  <b-row class="no-gutters">
    <b-col xs="12" lg="12" class="title text-center">
      <h3>Познакомимся ближе</h3>
    </b-col>
    <b-col lg="6" sm="12">
      <div class="about__text">
        <p>
          Создавая интернет магазин цветов, мы хотели, чтобы любимые люди, даже находясь на огромном расстоянии друг от друга, всегда имели возможность порадовать того, кто дорог, заставить близкого человека улыбнуться и почувствовать себя значимым и нужным.
        </p>
        <p>Наш сервис позволяет быстро, удобно, недорого и просто обрадовать близкого человека. Оформить заказ через интернет на нашем сайте вы можете круглосуточно 7 дней в неделю. На оформление уйдет не более 5 минут. Мы сделаем, все возможное, чтобы обрадовать ваших близких.</p>
        <p>Каждый день мы получаем более 330 улыбок и радостных слов благодарности. Это самое лучшее вознаграждение за непростую, но очень приятную работу.</p>
      </div>
    </b-col>
    <b-col lg="6" sm="12">
      <div class="about_img">
        <b-img-lazy src="~/assets/images/flower_about.jpg" alt="flower_about.jpg" />
      </div>
    </b-col>
    <b-col xs="12" lg="12" class="title text-center">
      <h1>Почему выбирают наc</h1>
      <b-row>
        <b-col xs="12" lg="4">
          <div class="icon">
            <i class="fa fa-shopping-cart" aria-hidden="true" />
          </div>
          <div class="icon_text text-left">
            <h3>Большой ассортимент</h3>
            <p>Цветы на любой вкус и текст</p>
          </div>
        </b-col>
        <b-col xs="12" lg="4">
          <div class="icon">
            <i class="fa fa-truck" aria-hidden="true" />
          </div>
          <div class="icon_text text-left">
            <h3>Оперативная доставка</h3>
            <p>Найдем курьера за 5 минут</p>
          </div>
        </b-col>
        <b-col xs="12" lg="4">
          <div class="icon">
            <i class="fa fa-trophy" aria-hidden="true" />
          </div>
          <div class="icon_text text-left">
            <h3>Гарантия качества</h3>
            <p>Множество счастливых клиентов</p>
          </div>
        </b-col>
      </b-row>
    </b-col>
  </b-row>
</template>

<style lang="scss">
.title {
    padding: 30px 0px;
    h3 {
      color: $darkgrey;
      text-transform: uppercase;
    }
}
.about__text {
  height: 100%;
  padding: 40px 60px;
  color: $darkgrey;
  border: 1px solid $lightgrey;

}
.icon {
  vertical-align: middle;
  width: 20%;
  display: inline-block;
  font-size: 3.5em;
  color: $pink;
}
.icon_text {
  margin-top: 18px;
  display: inline-block;
  width: 75%;
  vertical-align: -webkit-baseline-middle;
  h3 {
    font-size: 1em;
    text-align: left;
    padding: 0;
    margin-bottom: 2px;
    font-weight: 700;
  }
}
</style>
