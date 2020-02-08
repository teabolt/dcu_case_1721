// Twitter user tweets service


function getUserTweets(serviceProvider, screenName, callback) {
    // serviceProvider: twitterServiceProvider object
    // screenName: twitter user screen name for which to retrieve the tweets
    //             we use screen_name and not user_id for usability purposes
    // callback: function callback (json)
    serviceProvider.get(
        'statuses/user_timeline',
        { screen_name: screenName, },
        function (err, data, response) {
            callback(data);
        });
}


module.exports = {
    getUserTweets,
}