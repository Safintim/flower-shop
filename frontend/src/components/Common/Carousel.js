import React, { useState } from 'react';
import { Carousel, Container } from 'react-bootstrap';
import flow3 from './../../images/flow3-slider.jpg'

const ControlledCarousel = (props) => {
  const [index, setIndex] = useState(0);

  const handleSelect = (selectedIndex, e) => {
    setIndex(selectedIndex);
  };

  return (
    <Container>
      <Carousel activeIndex={index} onSelect={handleSelect}>
        <Carousel.Item>
          <img
            className="d-block w-100"
            src={flow3}
            alt="First slide"
          />
          <Carousel.Caption>
            <h3>Бесплатная быстрая доставка</h3>
            <p>Бесплатная быстрая доставка</p>
          </Carousel.Caption>
        </Carousel.Item>
        <Carousel.Item>
          <img
            className="d-block w-100"
            src={flow3}
            alt="Second slide"
          />

          <Carousel.Caption>
            <h3>Бесплатная быстрая доставка</h3>
            <p>Бесплатная быстрая доставка</p>
          </Carousel.Caption>
        </Carousel.Item>
        <Carousel.Item>
          <img
            className="d-block w-100"
            src={flow3}
            alt="Third slide"
          />

          <Carousel.Caption>
            <h3>Бесплатная быстрая доставка</h3>
            <p>Бесплатная быстрая доставка</p>
          </Carousel.Caption>
        </Carousel.Item>
      </Carousel>
    </Container>
  );
}

export default ControlledCarousel;