import React from 'react';
import { server_uri } from '../../../vars';
import './userTweets.css';
import TweetsList from './tweetsList';


let timeoutDuration = 450; // time to give between seaching for the person, in milliseconds


class UserTweets extends React.Component {

    constructor(props) {
        super(props)
        this.state = {
            screenName: "elonmusk",
            tweets: [],
            timeout: null,
            isTyping: false,
        }
    }

    fetchTweets = () => {
        fetch(server_uri + `/api/twitter/user-tweets?screen_name=${this.state.screenName}`)
            .then(res => res.json())
            .then(res => this.setState({ tweets: res }))
            .catch(err => console.log(err));
    }

    componentDidMount() {
        this.fetchTweets();
    }

    handleNameUpdate = (event) => {
        this.isTyping = true;
        this.setState({screenName: event.target.value, isTyping: true});
        if (this.timeout) {
            clearTimeout(this.timeout);
        }

        this.timeout = setTimeout(() => {
            this.setState({isTyping: false})
            this.fetchTweets();
        }, timeoutDuration);
    }

    getTweets = () => {
        return this.state.tweets;
    }

    render() {
        console.log('parent')
        console.log(this.state.tweets);
        let search = (
                        <input className="UserTweets-search"
                            type="text" 
                            name="user"
                            id="user" 
                            value={this.state.screenName} 
                            onChange={this.handleNameUpdate} 
                        />
                      );
        if (!this.state.isTyping) {
            return (
                <div className="UserTweets">
                    {search}
                    <TweetsList 
                        className="UserTweets-list" 
                        getTweetsCallback={this.getTweets}
                        height={this.props.height} />
                </div>
            );    
        } else {
            return (
                <div className="UserTweets-root">
                    {search}
                    <p>Loading...</p>
                </div>
            );
        }
    }
}


UserTweets.defaultProps = {
    height: 400,
}


export default UserTweets;


// TODO's:
// - Fix wiget sometimes showing wrong tweets - unmounting problem?
// - Load more tweets at the end of scroll
// - UI to set height and width, parameters 
// - Get tweets as logged in user
// - No tweets UI
// - Tweets list loading UI
// - Typing rolling circle UI ? (instead of 'Loading' text)