import React from 'react';
import ReactList from 'react-list';
import { TwitterTweetEmbed } from 'react-twitter-embed';


class TweetsList extends React.Component {

    renderTweet = (index, key) => {
        return (
            <div key={key}>
                <TwitterTweetEmbed 
                    tweetId={this.props.getTweetsCallback()[index].id_str}
                    options={{height: 100}}
                />
            </div>
        );
    }

    render() {
        console.log('child')
        console.log(this.props.getTweetsCallback())
        return (
            <div style={{height: this.props.height, overflow: 'auto'}} >
                <ReactList 
                    itemRenderer={this.renderTweet}
                    length={this.props.getTweetsCallback().length}
                    type='simple' 
                    items={this.props.getTweetsCallback()}
                />
            </div>
        );
    }
}


export default TweetsList;