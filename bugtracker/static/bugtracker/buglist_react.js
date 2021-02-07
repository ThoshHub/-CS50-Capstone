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
            loading: true,
            raw: null,
        };
    }

    async componentDidMount() {
        const url = '/bugtracker/buglistmessages';
        const response = await fetch(url);
        const data = await response.json();
        this.setState({raw: data, loading: false});
        // console.log(data[0].fields.title); //log the first one
        console.log(this.state.raw); //log the first one
    }

    toTitleCase(str) {
        return str.replace(
          /\w\S*/g,
          function(txt) {
            return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();
          }
        );
      }

    render() {

        // https://reactjs.org/docs/lists-and-keys.html

        if(this.state.loading){
            return <div>Loading...</div>;
        }

        if(this.state.raw.length == 0){
            return <div><h1>There are no bugs!</h1></div>
        }

        return (
            <div>
                {/* {this.state.raw} */}
                {this.state.raw.map((bug, i) => (
                    <div class="bugbox">
                        <div><strong>Title: </strong> {bug.fields.title}</div>
                        <div><strong>Severity: </strong> {this.toTitleCase(bug.fields.severity)}</div>
                        <div><strong>Type: </strong> {this.toTitleCase(bug.fields.type)}</div>
                    </div>
                ))}
            </div>
        );
    }	
}


ReactDOM.render(<Header />, document.querySelector('#header'));
ReactDOM.render(<Buglist />, document.querySelector('#bugs'));
// ReactDOM.render(<Buglist />, document.querySelector('#bugs')); // Second one does not render, but initalize is called twice