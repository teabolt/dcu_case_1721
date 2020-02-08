import React from 'react';
import { Redirect } from 'react-router-dom';
import { Button, FormGroup, FormControl, FormLabel, FormCheck } from "react-bootstrap";
import './appSignup.css';
import { server_uri } from '../../vars';


// A sign-up form based on:
// - https://gist.github.com/joelgriffith/43a4a8195c9fd237a222fe84c2b2e2b4
// - https://serverless-stack.com/chapters/create-a-login-page.html


class AppSignUp extends React.Component {

    constructor(props) {
        super(props)
        this.state = {
          email : "",
          password: "",
          password_re: "",
          error: "",
          checkboxChecked: false,
          redirect: false,
        };      
      }

    dismissError = () => {
        this.setState({ error: '' });
    }

    validateForm = () => {
        if (this.state.email.length === 0) {
            this.setState({ error: 'Email is required' });
            return false;
        } else if (this.state.password.length === 0) {
            this.setState({ error: 'Password is required' });
            return false;
        } else if (this.state.password !== this.state.password_re) { 
            this.setState({ error: 'Passwords must match!'});
            return false;
        } else if (!this.state.checkboxChecked) {
            this.setState({ error: 'You must agree to our terms!'});
            return false;
        } else {
            this.setState({ error: ''});
            return true;
        }
    }

    handleSubmit = (event) => {
        event.preventDefault();
        if (this.validateForm()) {
            let opts = { 
                'email': this.state.email, 
                'password': this.state.password, 
            };
            fetch(server_uri + '/signup', {
                method: 'post',
                headers: new Headers({'content-type': 'application/json'}),
                body: JSON.stringify(opts)
            }).then(res => {
                console.log('signed up!');
                this.setState({'redirect': true});
            }).catch(err => {
                console.log('sign up error');
                console.log(err);
                this.setState({'error': err});
            });
        }
    }

    render() {
        if (this.state.redirect) {
            return (
                <Redirect to={{'pathname': '/'}} />
            );
        } else {  
            return (
                <div className="AppSignUp">
                    <h1>Sign Up</h1>
                    <form onSubmit={this.handleSubmit}>
                        {
                            this.state.error &&
                            <div className="AppSignUp-error">
                                <p onClick={this.dismissError}>
                                    <button onClick={this.dismissError}>✖</button>
                                    {this.state.error}
                                </p>
                            </div>
                        }
                        <FormGroup controlId="email" bsSize="large">
                            <FormLabel>Email</FormLabel>
                            <FormControl
                                autoFocus
                                type="email"
                                value={this.state.email}
                                onChange={evt => this.setState({"email": evt.target.value})}
                            />
                        </FormGroup>
                        <FormGroup controlId="password" bsSize="large">
                            <FormLabel>Password</FormLabel>
                            <FormControl
                                value={this.state.password}
                                onChange={evt => this.setState({"password": evt.target.value})}
                                type="password"
                            />
                        </FormGroup>
                        <FormGroup controlId="password-re" bsSize="large">
                            <FormLabel>Confirm password</FormLabel>
                            <FormControl
                                value={this.state.password_re}
                                onChange={evt => this.setState({"password_re": evt.target.value})}
                                type="password"
                            />
                        </FormGroup>
                        <FormGroup controlId="formBasicCheckbox">
                            <FormCheck 
                            type="checkbox"
                            label="I promise not to do any evil things with this app." 
                            checked={this.state.checkboxChecked}
                            onChange={evt => this.setState({"checkboxChecked": !this.state.checkboxChecked})}
                            />
                        </FormGroup>
                        <Button block bsSize="large" type="submit">
                            Sign Up
                        </Button>
                    </form>
                </div>
            );
        }
    }
}


export default AppSignUp;