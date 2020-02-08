const dotenv = require('dotenv');
const result = dotenv.config()
if (result.error) {
  throw result.error
}
console.log(result.parsed)


let mongodbHost = process.env.MONGODB_HOST;
let mongodbPort = process.env.MONGODB_PORT;
let mongodbDb = process.env.MONGODB_DB;
let mongodbUri = `mongodb://${mongodbHost}:${mongodbPort}/${mongodbDb}`;


module.exports = {
    hostname: process.env.SERVER_HOST,
    port: process.env.SERVER_PORT,
    twitterConsumerKey: process.env.TWITTER_CONSUMER_KEY,
    twitterConsumerSecret: process.env.TWITTER_CONSUMER_SECRET,
    twitterAccessToken: process.env.TWITTER_ACCESS_TOKEN,
    twitterAccessTokenSecret: process.env.TWITTER_ACCESS_TOKEN_SECRET,
    mongodbHost: mongodbHost,
    mongodbPort: mongodbPort,
    mongodbDb: mongodbDb,
    mongodbUri: mongodbUri,
};