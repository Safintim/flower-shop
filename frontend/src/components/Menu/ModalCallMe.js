import React, {useState} from 'react';
import { Row, Col, Modal, Form, Button } from 'react-bootstrap';
import callMe from './../../images/call.png';
import InputMask from "react-input-mask";


const ModalCallMe = (props) => {
    const [show, setShow] = useState(false);

    const handleClose = () => setShow(false);
    const handleShow = () => setShow(true);
    return (<>
        <a href="#" className="menu-btn call-me" title="Заказать звонок" onClick={handleShow}>
            <img src={callMe} alt="Заказать звонок"/>
        </a>

        <Modal dialogClassName="modal-sm" show={show} onHide={handleClose}>
            <Modal.Body className="p-5">
                <Row>
                    <Col lg={12} className="text-center">
                        <div className="modal-call-me-title">Быстрый заказ</div>
                    </Col>
                </Row>
                <Row>
                    <Col lg={12} className="text-center">
                        <div className="modal-call-me-form">
                            <Form>
                                <Form.Group>
                                    <InputMask className="form-control" mask="+7 (999) - 999 - 99 -99" placeholder="Ваш телефон"/>

                                    <Button variant="danger">Отправить</Button>
                                </Form.Group>
                            </Form>
                        </div>
                    </Col>
                </Row>
            </Modal.Body>
        </Modal>
        {/*<input type="text" className="form-control" id="phone" name="phone"*/}
        {/*       data-inputmask="'mask': '+33 9 99 99 99 99'">*/}
    </>);
};

export default ModalCallMe;
