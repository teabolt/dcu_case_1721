const path = require('path');
const express = require('express');
const bodyParser  = require('body-parser');
const cors = require('cors');
const passport = require('passport');
const Strategy = require('passport-local').Strategy;
const db = require('./db');
const UserModel = require('./db/models/user');
const { hostname, port } = require('./vars');
const TwitterService = require('./services/twitter/twitter');
const UserTweetsWidget = require('./services/twitter/userTweets');


// globals
const app = express();
var twitterService = TwitterService.getTwitterServiceProvider();


// passport authentication

// Configure the local strategy for use by Passport.
//
// The local strategy require a `verify` function which receives the credentials
// (`username` and `password`) submitted by the user.  The function must verify
// that the password is correct and then invoke `cb` with a user object, which
// will be set at `req.user` in route handlers after authentication.
passport.use(new Strategy({
    usernameField: 'email',
    passwordField: 'password',
  },
  function(username, password, cb) {
    console.log('Authenticating with: %s %s', username, password);
    UserModel.find({email : username}, function (err, docs) {
      if (err) { return cb(err); }
      if (docs.length) {
          cb('User with this username already exists', null);
      } else {
          // TODO: encrypt password
          const newUser = new UserModel({email: username, password: password});
          newUser.save((err, user) => {
            if (err) return console.error(err);
            cb(null, newUser);
          })
      }
    });
  }));

// Configure Passport authenticated session persistence.
//
// In order to restore authentication state across HTTP requests, Passport needs
// to serialize users into and deserialize users out of the session.  The
// typical implementation of this is as simple as supplying the user ID when
// serializing, and querying the user record by ID from the database when
// deserializing.user
passport.serializeUser(function(user, cb) {
  console.log("serializing: %s", user)
  cb(null, user.id);
});

passport.deserializeUser(function(id, cb) {
  console.log("deserializing: %s", id)
  UserModel.findById(id, (err, user) => {
    if (err) { return cb(err); }
    cb(null, user);
  });
});


//
// app config
//

// where to serve .html, .js, and image files from
// app.use(express.static(path.join(__dirname, 'public')));
// app.use(express.static(path.join(__dirname, 'client/build')));

// load templating engine to use
// app.set('view engine', 'ejs')

//configure body-parser as middle-ware.
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

// configure express-session as middleware
app.use(require('express-session')({ secret: 'keyboard cat', resave: false, saveUninitialized: false }));

// enable CORS for all routes
app.use(cors());

// Initialize Passport and restore authentication state, if any, from the
// session.
app.use(passport.initialize());
app.use(passport.session());


//
// routes
//

app.get('/api/ping', (req, res) => {
  res.send('pong');
});

app.get('/api/twitter/user-tweets', (req, res) => {
  let screenName = req.query.screen_name;
  console.log(`request for ${screenName}`);
  UserTweetsWidget.getUserTweets(
    twitterService,
    screenName,
    function(data) {
      res.send(JSON.stringify(data));
  });
});


app.post('/signup', 
  passport.authenticate('local', { failureRedirect: '/signup-fail' }),
  function(req, res) {
    res.send('OK');
});


app.get('/signup-fail')


// app.post('/signup', (req, res) => {
//   let email = req.body.email;
//   let password = req.body.password;
//   console.log(req.body);
//   console.log("Email = "+email+", password = "+password);
//   res.end("OK");
// });


// app.get('/', (req, res) => {
// 	res.sendFile(path.join(__dirname, 'client/build/index.html'));
//   // res.render('index.html.ejs', { screenName: screenName });
//   // UserTweetsWidget.getUserTweets(
//   //   twitterService,
//   //   screenName,
//   //   function(data) {
//   //     console.log(typeof data);
//   //     console.log(data);
//   //     res.render('index.html.ejs', { data: JSON.stringify(data) });
//   // });
// });


// app.post('/twitter/user-timeline', (req, res) => {
//   console.log("got");
// });


// app.get('/about.json', (req, res) => {
//   res.status(200);
//   console.log("fuck you");
//   res.send('TODO');
// });


// launch app
app.listen(port, () => console.log(`App running at http://${hostname}:${port}/`));