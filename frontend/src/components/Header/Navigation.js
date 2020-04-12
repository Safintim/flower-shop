import React from 'react';
import { Navbar, Nav, Container, Row, Col } from 'react-bootstrap'


const Navigation = () => {
  return (<>
    <Container fluid>
      <Row>
        <Col lg={12}>
          <Navbar bg="light" expand="lg">
            <Navbar.Toggle aria-controls="basic-navbar-nav" />
            <Navbar.Collapse id="basic-navbar-nav">
              <Nav className="mr-auto">
                <Nav.Link href="#home">О магазине</Nav.Link>
                <Nav.Link href="#link">Доставка</Nav.Link>
                <Nav.Link href="#link">Контакты</Nav.Link>
              </Nav>
            </Navbar.Collapse>
          </Navbar>
        </Col>
      </Row>
    </Container>
  </>);
};

export default Navigation;
