import React, { Component } from 'react';
import './App.css';

import PrinterCard from './cards'
import TopBar from './title'

const urls = {
  'Engineering Room': '10.99.21.243',
};

class App extends Component {

  state = {
    location: 'Engineering Room',
    status: 'Printing',
  }
  /*
  for (links in urls) {
    console.log(links)
  }
  */
  render() {
    return (
      <div className="App">
        <TopBar />
        <h4>Printers</h4>
        <div class='Cards'>
          <PrinterCard location={this.state.location} status={this.state.status}/>
        </div>
      </div>
    );
  }
}

export default App;
