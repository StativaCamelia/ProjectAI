import React from 'react';
import '../styles/Search.css';
import Particles from 'react-particles-js';
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import axios from 'axios';


import {
	Link
  } from "react-router-dom";

class Search extends  React.Component {
    constructor(props) {
        super(props);
        this.state = {question: ''};
        this.response = ''
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({question: event.target.value});
  }

    async handleSubmit(event){
        event.preventDefault();
        const requestOptions = {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text: this.state.question })
    };
        const response = await fetch('http://127.0.0.1:5000/',requestOptions).then(response => response.json())
        console.log(response)
        this.setState({response : response.response})
  }

	render() {
		return (
            <div className="container_welcome">
                <div className="action_container">
                    <div className="search_container">
                        <form onSubmit={this.handleSubmit}>
                              <input className="input_container" type="text" value={this.state.question} onChange={this.handleChange} />
                               <Button type="submit" value="Submit">Submit</Button>
                         </form>
                    </div>
                    <div className="response_container">
                         <input className="input_container" type="text" value={this.state.response} onChange={e=>this.setState({response: e.target.value})}/>
                    </div>
                </div>
        </div>
			)
	}
}
export default Search;