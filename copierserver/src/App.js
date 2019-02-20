import React, { Component } from 'react';
import './App.css';

import PrinterCard from './cards'


class App extends Component {
  render() {
    return (
      <div className="App">
        <h1>Copier Queue Manager</h1>
        <PrinterCard />
      </div>
    );
  }
}

export default App;
