<template>
  <div class="catalog-item text-center">
    <b-overlay :show="show" rounded="sm">
      <a href="/">
        <img class="catalog-item__image img-fluid" :src="bouquet.photoUrl" :alt="bouquet.title">
      </a>
      <template v-slot:overlay>
        <div class="text-center">{{ bouquet.description }}</div>
      </template>
    </b-overlay>
    <div class="catalog-item__info text-center p-2">
      <div class="catalog-item__info_mark d-flex flex-column align-items-end">
        <div v-if="bouquet.isHit" class="catalog-item__info_mark_hit">Хит</div>
        <div v-if="bouquet.isNew" class="catalog-item__info_mark_new">Новинка</div>
      </div>
      <div class="catalog-item__info_title">
        <a href="https://floristan.ru/catalog/product/259">{{ bouquet.title }}</a>
      </div>

      <div class="catalog-item__info_price">от {{ bouquet.minPrice }} Р</div>
      <div class="catalog-item__info_buttons d-flex flex-wrap align-items-center justify-content-center">
        <button class="catalog-item__info_buttons_add_to_cart py-3 px-4 px-xs-5 mr-2 mb-2">в корзину</button>

        <button class="catalog-item__info_buttons_more py-3 px-4 mb-2" @click="show = !show">подробнее</button>
        <span>
          <b-link class="catalog-item__info_buttons_buy">купить в один клик</b-link>
        </span>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  props: {
    bouquet: {
      type: Object,
      default () {}
    }
  },
  data () {
    return {
      show: false
    }
  }
}
</script>
<style lang="scss" scoped>
.catalog-item {
  position: relative;
  margin-bottom: 16px;
  padding: 16px 0;
  box-shadow: 0 0 8px 0 $whiteshadow;
  border: 1px solid $lightgrey;
  border-radius: 4px;
  &__info_mark {
    position: absolute;
    top: 45px;
    right: -8px;
    &_hit,
    &_new {
      background: $new;
      border-radius: 100px;
      color: #fff;
      font-size: 12px;
      font-weight: 700;
      line-height: 29px;
      padding: 0 20px;
      text-transform: uppercase;
      margin-bottom: 10px;
      display: inline-block;
    }
    &_hit {
      background: $hit;
    }
  }
  &__info_title {
    text-align: center;
    margin: 10px 0;
    a {
      text-decoration: none;
      line-height: 0.8;
      font-size: 20px;
      color: $pink;
      font-weight: bold;
    }
    a:hover {
      color: $pink;
      text-decoration: none;
    }
  }
  &__info_price {
    margin: 10px 0;
    text-align: center;
    line-height: 0.8;
    font-size: 20px;
    color: rgb(68, 68, 68);
  }
  &__info_buttons {
    &_more,
    &_add_to_cart {
      vertical-align: top;
      position: relative;
      display: inline-block;
      background-color: $pink;
      color: #ffffff;
      text-align: center;
      text-decoration: none;
      font-size: 20px;
      line-height: 0.8;
      border: none;
      border-radius: 5px;
    }

    &_more {
      background-color: #ffffff;
      color: rgb(225, 225, 225);
      border: 1px solid $lightgrey;
      border-radius: 5px;
    }
    span {
      display: inline-block;
      border-bottom: 2px dotted $darkgrey;
    }
    &_buy {
      text-decoration: none;
      color: $darkgrey;
    }
    &_buy:hover {
      color: $darkgrey;
    }
  }
}
</style>
