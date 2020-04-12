import React, { useState } from 'react';
import { Button, Modal } from 'react-bootstrap';
import { Search } from '../Common'

const City = (props) => {
  const [show, setShow] = useState(false);

  const handleClose = () => setShow(false);
  const handleShow = () => setShow(true);  
  return (<>
    <Button variant="primary" onClick={handleShow}>
      Launch demo modal
    </Button>

    <Modal show={show} onHide={handleClose} animation={false}>
      <Modal.Header closeButton>
        <Modal.Title>Выберите город</Modal.Title>
      </Modal.Header>
      <Modal.Body>
        <Search />
        <ul className="list">
          <li className="col1">Test 1</li>
          <li className="col1">Test 2</li>
          <li className="col1">Test 3</li>
          <li className="col1">Test 4</li>

          <li className="col2">Test 5</li>
          <li className="col2">Test 6</li>
          <li className="col2">Test 7</li>
          <li className="col2">Test 8</li>

          <li className="col3">Test 9</li>
          <li className="col3">Test 10</li>
          <li className="col3">Test 11</li>
          <li className="col3">Test 12</li>
        </ul>

      </Modal.Body>
    </Modal>
  </>);
}

export default City;
