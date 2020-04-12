import React from 'react';
import { TiShoppingCart } from "react-icons/ti";
import { Badge } from 'react-bootstrap';

const Cart = (props) => {
  return (<>
    <a href="/">
      <TiShoppingCart />
      <Badge color="secondary">4</Badge>
      <span> 100 ₽</span>
    </a>
  </>);
}

export default Cart;
