const mongoose = require('mongoose');
const vars = require('../vars');


// TODO: retry connection for a number of times
mongoose.connect(vars.mongodbUri).then(
    () => { console.log('Connected to Mongo')},
    err => {
         console.log('error connecting to Mongo: ')
         console.log(err);
        }
    );


module.exports = mongoose.connection