// import React, { Component } from 'react';

// TODO how to call a function in react? on pageload
// function()

async function intialize() {
    try {
        // TODO query buglistmessages here
        // const res = await fetch('http://127.0.0.1:8000/api/'); // fetching the data from api, before the page loaded
        
        const res = await fetch('/bugtracker/buglistmessages'); // fetching the data from api, before the page loaded
        console.log("Called Initialize Function");

        const buglist_json = await res.json();
        console.log("Returned: " + buglist_json);
        // this.setState({
        //     todos
        // });
    } catch (e) {
        console.log(e);
    }
}

class App extends React.Component {

    render() {
        intialize();
        
        return (
            <div>
                <h2 id="index_header" >List of Bugs:</h2>
            </div>
        );
    }	
}

ReactDOM.render(<App />, document.querySelector('#app'));