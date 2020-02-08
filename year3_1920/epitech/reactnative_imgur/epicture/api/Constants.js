// var joinPath = require('path.join');

// 
// URI's and other constants for interaction with the Imgur API
// 


// base URI for Imgur API endpoints
export const imgur_base_uri = 'https://api.imgur.com/3/'

// base URI for Imgur user authentication endpoint
export const imgur_auth_uri = 'https://api.imgur.com/oauth2/authorize'

// base URI for app-defined authentication callback
export const auth_callback_uri = 'https://www.getpostman.com/oauth2/callback'


// URI for the currently authenticated user's images
export const imgur_account_my_images = imgur_base_uri + 'account/me/images';

// URI for images in the gallery
export const imgur_feed_images = imgur_base_uri + 'gallery/hot/viral/0/';

// base URI to search for images in the gallery
export const imgur_search_images_base = imgur_base_uri + 'gallery/search';