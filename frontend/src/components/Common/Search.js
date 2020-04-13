import React from 'react';
import { Form, FormControl, Button } from 'react-bootstrap'

const Search = (props) => {
  const placeholder = props.placeholder ? props.placeholder : 'Поиск букетов и подарков';
  return (<>
    <div className="header-search">
      <Form>
        <FormControl type="text" placeholder={placeholder} className="mr-sm-2" />
        <Button variant="hidden"></Button>
      </Form>
    </div>
  </>);
}

export default Search;
