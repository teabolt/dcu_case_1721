const mongoose = require('mongoose');


// define user schema
const userSchema = new mongoose.Schema({
	email: { type: String, unique: true, required: true },
	password: { type: String, unique: false, required: true }
});


const UserModel = mongoose.model('User', userSchema);
module.exports = UserModel