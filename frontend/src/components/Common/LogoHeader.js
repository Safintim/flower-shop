import React from 'react';
import Image from 'react-bootstrap/Image'
import logo from './../../images/logo.png'

const LogoHeader = (props) => {
  return (<>
    <a href='/'>
      <Image 
        src={logo}
        width={171}
        alt="171x180"
      />
    </a>
  </>);
}

export default LogoHeader;