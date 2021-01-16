import React from 'react';
import '../styles/Search.css';
import Particles from 'react-particles-js';
import Button from 'react-bootstrap/Button';
import {
	Link
  } from "react-router-dom";

class Search extends  React.Component {
	constructor( props ) {
		super( props );
		this.state = {
			query: '',
            results: {},
            loading: false,
            message: '',
		};
	}

	handleOnInputChange = (event) => {
		const query = event.target.value;
		console.log(query)
		this.setState({ query, loading: true, message: event.target.value  } );
	};

	render() {
		return (
            <div className="container_welcome">
                <div className="title_container" >
                    <h1 className="title">Start your search!</h1>
                    <p className="description">Take your regular searches and make them more targeted, helping you to find the results you need quickly.</p>
                    <Link to="/search"><Button  variant="primary" size="lg" href="/search">Start now ></Button> </Link>
                </div>
                <Particles className="particles_js"
                params={{
                    particles: {
                        number: {
                            value: 150,
                            density: {
                                value_area: 10000
                            }
                        },
                        color: {
                            value: '#fff'
                        },
                        opacity: {
                            value: 0.8,
                            anim: {
                                enable: true
                            }
                        },
                        size: {
                            value: 7,
                            random: true,
                            anim: {
                                enable: true,
                                speed: 5
                            }
                        },
                        line_linked: {
                            enable: true
                        },
                        move: {
                            speed: 0.5
                        }
                    }    
                }}    
            />
        </div>
			)
	}
}
export default Search;