import React from 'react';
import { TiShoppingCart } from "react-icons/ti";
import { Badge } from 'react-bootstrap';

const Cart = (props) => {
  return (<>
    <a href="/" className="header-cart">
      <span class="cart">
        <span class="icon"><TiShoppingCart /></span>
        <Badge className="cart-total">4</Badge>
      </span>      
      <span class="price">100 ₽</span>
    </a>
  </>);
}

export default Cart;
