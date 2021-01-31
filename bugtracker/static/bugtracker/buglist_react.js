import React, { Component } from 'react';

async function  componentDidMount() {
    try {
        // TODO query buglistmessages here
      const res = await fetch('http://127.0.0.1:8000/api/'); // fetching the data from api, before the page loaded
      const todos = await res.json();
      this.setState({
        todos
      });
    } catch (e) {
      console.log(e);
    }
  }

class App extends React.Component {

    render() {
        return (
            <div>
                <h2 id="index_header" >List of Bugs:</h2>
            </div>
        );
    }	
}

ReactDOM.render(<App />, document.querySelector('#app'));