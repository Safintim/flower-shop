import React from 'react';
import { Container, Row, Col } from 'react-bootstrap';
import Categories from './Categories';
import ModalCallMe from './ModalCallMe';


const Menu = (props) => {
    return (<>
        <div className="menu">
            <Container>
                <Row>
                    <Col lg={12}>
                        <Categories />
                        <div className="menu-right-block">
                            <ModalCallMe />
                        </div>
                    </Col>
                </Row>
            </Container>
        </div>
    </>);
};

export default Menu;
