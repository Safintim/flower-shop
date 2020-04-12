import React, { Component } from 'react';
import Navigation from './Navigation';
import Info from './Info';

class Header extends Component {
  render() {
    return (
      <div>
          <Navigation />
          <Info />
      </div>
    );
  }
}

export default Header;