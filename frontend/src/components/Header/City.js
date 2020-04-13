import React, { useState } from 'react';
import { Button, Modal } from 'react-bootstrap';
import { Search } from '../Common'

const City = (props) => {
  const [show, setShow] = useState(false);

  const handleClose = () => setShow(false);
  const handleShow = () => setShow(true);
  props = {
    ...props,
    placeholder: "Введите название"
  }
  return (<>
    <div className="header-city-title">
      Город доставки
    </div>
    <div className="header-city-current" onClick={handleShow}>
      <span>Казань</span>
    </div>

    <Modal show={show} onHide={handleClose}>
      <Modal.Header closeButton>
        <Modal.Title>Выберите город</Modal.Title>
      </Modal.Header>
      <Modal.Body>
        <Search {...props}/>
        <ul className="list">
          <li><a href="/">Test 1</a></li>
          <li><a href="/">Test 1</a></li>
          <li><a href="/">Test 1</a></li>
          <li><a href="/">Test 1</a></li>
          <li><a href="/">Test 1</a></li>
          <li><a href="/">Test 1</a></li>
          <li><a href="/">Test 1</a></li>
          <li><a href="/">Test 1</a></li>
          <li><a href="/">Test 1</a></li>
          <li><a href="/">Test 1</a></li>
          <li><a href="/">Test 1</a></li>
          <li><a href="/">Test 1</a></li>
          <li><a href="/">Test 1</a></li>
          <li><a href="/">Test 1</a></li>
          <li><a href="/">Test 1</a></li>
          <li><a href="/">Test 1</a></li>
          <li><a href="/">Test 1</a></li>
          <li><a href="/">Test 1</a></li>
          <li><a href="/">Test 1</a></li>
          <li><a href="/">Test 1</a></li>
          <li><a href="/">Test 1</a></li>
          <li><a href="/">Test 1</a></li>
          <li><a href="/">Test 1</a></li>
          <li><a href="/">Test 1</a></li>
          <li><a href="/">Test 1</a></li>
          <li><a href="/">Test 1</a></li>
          <li><a href="/">Test 1</a></li>
          <li><a href="/">Test 1</a></li>
        </ul>

      </Modal.Body>
    </Modal>
  </>);
}

export default City;
