const Twit = require('twit');
const vars = require('../../vars');


// Twitter service
// Provides authentication


function getTwitterServiceProvider() {
    return new Twit({
        consumer_key:         vars.twitterConsumerKey,
        consumer_secret:      vars.twitterConsumerSecret,
        access_token:         vars.twitterAccessToken,
        access_token_secret:  vars.twitterAccessTokenSecret,
    });    
}


module.exports = {
    getTwitterServiceProvider,
}