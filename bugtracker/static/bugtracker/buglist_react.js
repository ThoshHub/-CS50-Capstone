// import React, { Component } from 'react';

// TODO how to call a function in react? on pageload
// function()

// async function intialize() {        
//         const res = await fetch('/bugtracker/buglistmessages'); // fetching the data from api, before the page loaded
//         const buglist_json = await res.json();
//         // buglist_json.forEach(element => { console.log(element) });
//         console.log(buglist_json)
//         return buglist_json;
// }

class Header extends React.Component {
    render() {
        return (
            <div>
                <h2 id="index_header" >List of Bugs:</h2>
            </div>
        );
    }
}

class Buglist extends React.Component {
    
    constructor(props) {
        super(props);
        this.state = {
            raw: null,
            title: "title",
            description: "description",
            severity: "severity",
            type: "type",
            estimate: 0,
            owner: "owner"
        };
    }

    async componentDidMount() {
        const url = '/bugtracker/buglistmessages';
        const response = await fetch(url);
        const data = await response.json();
        this.setState({raw: data[0]});
        console.log(data[0]);
    }

    render() {
        // TODO return json from initialize method and store it in a variable
        // once it is stored, you need to loop through it (it is a list of JSONs)
        // and for each json, set the state and display it 
        // as of writing this, not sure how to display additional fields in react but 
        // https://reactjs.org/docs/lists-and-keys.html

        return (
            <div>
                <h2 id="index_header" >Buglist goes here:</h2>
            </div>
        );
    }	
}


ReactDOM.render(<Header />, document.querySelector('#header'));
ReactDOM.render(<Buglist />, document.querySelector('#bugs'));
// ReactDOM.render(<Buglist />, document.querySelector('#bugs')); // Second one does not render, but initalize is called twice