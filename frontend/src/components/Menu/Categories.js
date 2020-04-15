import React from 'react';
import { Navbar, Nav, NavDropdown } from 'react-bootstrap';

const Categories = (props) => {
    return (<>
    <Navbar className="float-left" expand="lg">
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
            <Nav className="mr-auto">
                <NavDropdown title="Цветы" id="basic-nav-dropdown">
                    <NavDropdown.Item href="#action/3.1">Гвоздики</NavDropdown.Item>
                    <NavDropdown.Item href="#action/3.2">Розы</NavDropdown.Item>
                    <NavDropdown.Item href="#action/3.3">Герберы</NavDropdown.Item>
                    <NavDropdown.Divider />
                    <NavDropdown.Item href="#action/3.4">Все цветы</NavDropdown.Item>
                </NavDropdown>
                <NavDropdown title="Композиции" id="basic-nav-dropdown">
                    <NavDropdown.Item href="#action/3.1">Корзины с цветами</NavDropdown.Item>
                    <NavDropdown.Item href="#action/3.2">Коробочки с цветами</NavDropdown.Item>
                    <NavDropdown.Item href="#action/3.3">Все композиции</NavDropdown.Item>
                    <NavDropdown.Divider />
                    <NavDropdown.Item href="#action/3.4">Separated link</NavDropdown.Item>
                </NavDropdown>
                <NavDropdown title="Тип букета" id="basic-nav-dropdown">
                    <NavDropdown.Item href="#action/3.1">В формце сердца</NavDropdown.Item>
                    <NavDropdown.Item href="#action/3.2">В шляпной коробке</NavDropdown.Item>
                    <NavDropdown.Divider />
                    <NavDropdown.Item href="#action/3.4">Все букеты</NavDropdown.Item>
                </NavDropdown>
                <NavDropdown title="Повод" id="basic-nav-dropdown">
                    <NavDropdown.Item href="#action/3.1">8 марта</NavDropdown.Item>
                    <NavDropdown.Item href="#action/3.2">День рождение</NavDropdown.Item>
                    <NavDropdown.Divider />
                    <NavDropdown.Item href="#action/3.4">Все поводы</NavDropdown.Item>
                </NavDropdown>
                <NavDropdown title="Подарки" id="basic-nav-dropdown">
                    <NavDropdown.Item href="#action/3.1">Сладости</NavDropdown.Item>
                    <NavDropdown.Item href="#action/3.2">Фруктовые корзины</NavDropdown.Item>
                    <NavDropdown.Item href="#action/3.3">Открытки</NavDropdown.Item>
                    <NavDropdown.Divider />
                    <NavDropdown.Item href="#action/3.4">Все подарки</NavDropdown.Item>
                </NavDropdown>
            </Nav>
        </Navbar.Collapse>
    </Navbar>
    </>);
};

export default Categories;
