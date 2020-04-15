import React from 'react';
import Navigation from './Navigation';
import Info from './Info';

const Header = (props) => {
  return(<>
      <header>
          <Navigation />
          <Info />
      </header>
  </>);
}

export default Header;