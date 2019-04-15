import React, { Component } from 'register'
  //code for getting information from print server
  for (links in urls) {
    console.log(links)
  }

  render() {
    return (
      <div className="App">
        <TopBar />
        <div class='Map'>
          <img src="">
        </div>
        <div class='Cards'>
          <PrinterCard location={this.state.location} />
        </div>
      </div>
    );
  }
}

export default App;
