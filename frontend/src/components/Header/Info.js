import React from 'react';
import { Container, Row, Col } from 'react-bootstrap'
import { LogoHeader, Search } from '../Common'
import City from './City'
import Cart from './Cart'
import Contact from './Contact'

const Info = (props) =>{
  return (<>
    <Container>
      <Row className="align-items-center">
        <Col md={3} lg={2}>
          <LogoHeader />
        </Col>
        <Col md={3} lg={2}>
          <City />
        </Col>
        <Col md={4} lg={4}>
          <Search />
        </Col>
        <Col md={2} lg={2}><Cart /></Col>
        <Col md={12} lg={2}><Contact /></Col>
      </Row>
    </Container>
  </>);
}

export default Info;