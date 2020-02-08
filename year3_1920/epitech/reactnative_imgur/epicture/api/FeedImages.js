import { clientId } from '../Config';
import { imgur_feed_images, imgur_search_images_base } from './Constants';


export async function getFeedImages(search) {
  try {
    let uri;
    if (search === "") {
      uri = imgur_feed_images;
    } else {
      uri = imgur_search_images_base + 'q?=' + search;
    }
    let response = await fetch(uri, {
      headers: {
        'Authorization': 'Client-ID ' + clientId
      }
    });
    let responseJson = await response.json();
    return responseJson;
  } catch (error) {
    console.error(error);
  }
}
