import { secureGet } from './SecureStorage';

// User-account related utilities


// return a boolean indicating whether someone is logged onto the app
export async function checkIsLoggedIn() {
  let isLoggedIn = await secureGet('accessToken') != null;
  console.log(isLoggedIn);
  return isLoggedIn;
}
