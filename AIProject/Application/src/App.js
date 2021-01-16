import React from 'react';
import {
	BrowserRouter as Router,
	Switch,
	Route,
  } from "react-router-dom";
import SearchPage from "./SearchPage/SearchPage"
import Welcome from "./SearchPage/Welcome";
import "bootstrap/dist/css/bootstrap.min.css";
import './styles/Search.css';

class App extends React.Component {
	render() {
		return (
			<Router>
			<div className = "page">
				<Switch>
					<Route exact path="/" component={Welcome}/>
					<Route path="/search" component={SearchPage} />
          		</Switch>
			</div>
			</Router>
		);
	}
}
export default App;