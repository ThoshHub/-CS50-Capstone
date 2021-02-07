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

    severityStyleConditional(severity) {
        if(severity == 'CRITICAL') {
            return {color: 'crimson', 'font-weight': 'bold'}
        } else if (severity == 'HIGH') {
            return {color: 'red', 'font-weight': 'bold'}
        } else if (severity == 'MEDIUM') {
            return {color: 'orange'}
        } else { // severity == low is the only other option
            return {color: 'green'}
        }
    }

    typeStyleConditional(type) { // leave it black for the time being
        if(type == 'FUNCTIONAL') {
            return {color: 'black'}
        } else if(type == 'PERFORMANCE') {
            return {color: 'black'}
        } else if(type == 'USABILITY') {
            return {color: 'black'}
        } else if(type == 'COMPATABILITY') {
            return {color: 'black'}
        } else if(type == 'SECURITY') {
            return {color: 'black'}
        } else  { // type = other is the only other option
            return {color: 'black'}
        } 
    }

    render() {

        // https://reactjs.org/docs/lists-and-keys.html

        if(this.state.loading){
            return <div>Loading...</div>;
        }

        if(this.state.raw.length == 0){
            return <div><h1>There are no bugs!</h1></div>
        }

        let detailsStyle = {
            'margin-bottom': '5px',
            'margin-top': '5px',
        }

        return (
            <div>
                {/* {this.state.raw} */}
                {this.state.raw.map((bug, i) => (
                    <div key={`bug-num-${i}`} id={`bug-num-${i}`} class="bugbox">
                        <div><strong>Title: </strong> {bug.fields.title}</div>
                        {/* Here the bug.fields.severity var is being passed into the function severityStyleConditional() where it returns a CSS style that is rendered in the style tag in the <span> element */}
                        <div><strong>Severity: </strong> <span style={this.severityStyleConditional(bug.fields.severity)}>{this.toTitleCase(bug.fields.severity)}</span></div>
                        <div><strong>Type: </strong> <span>{this.toTitleCase(bug.fields.type)}</span></div>

                        {/* The action attribute is failing, need to figure out how to route urls between react and django */}
                        <a href="/bugtracker" class="btn btn-primary" style={detailsStyle}>Details</a>
                    </div>
                ))}
            </div>
        );
    }	
}


ReactDOM.render(<Header />, document.querySelector('#header'));
ReactDOM.render(<Buglist />, document.querySelector('#bugs'));
// ReactDOM.render(<Buglist />, document.querySelector('#bugs')); // Second one does not render, but initalize is called twice