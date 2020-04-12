import React from 'react';
import Header from './components/Header'
import { ControlledCarousel } from './components/Common'

// class App extends Component {
//   state = {
//     todos: []
//   };

  // async componentDidMount() {
  //   try {
  //     const response = await fetch('http://127.0.0.1:8000/api/bouquets/');
  //     const todos = await response.json();
  //     this.setState({
  //       todos
  //     });
  //   } catch (e) {
  //     console.log(e);
  //   }
  // }

  // render() {
  //   return (
  //     <div>
  //       <Header />
  //     </div>
      // <div>
      //   {this.state.todos.map(item => (
      //     <div key={item.id}>
      //       <h1>{item.title}</h1>
      //       <span>{item.description}</span>
      //     </div>
      //   ))}
      // </div>
//     );
//   }
// }

const App = (props) => {
  return (<>
    <Header />
    <ControlledCarousel />
  </>
  );
};


export default App;