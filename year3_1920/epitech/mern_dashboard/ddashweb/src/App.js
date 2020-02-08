import React from 'react';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';
import AppLogin from './components/auth/appLogin';
import AppSignUp from './components/auth/appSignup';
import Home from './components/home/home';


class App extends React.Component {

  constructor(props) {
    super(props);
    this.state = { text: "" };
  }

  render() {
    return (
      <Router>
        <div className="App">
          <nav className="App-navbar">
            <ul>
              <li>
                <Link to="/">Home</Link>
              </li>
              <li>
                <Link to="/login">Login</Link>
              </li>
              <li>
                <Link to="/signup">Sign Up</Link>
              </li>
            </ul>
          </nav>

          {/* <UserTweets /> */}

          <Switch>
              <Route path="/login">
                <AppLogin />
              </Route>
              <Route path="/signup">
                <AppSignUp />
              </Route>
              <Route path="/">
                <Home />
              </Route>
          </Switch>
        </div>
      </Router>
    );
  }
}


export default App;