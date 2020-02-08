import * as SecureStore from 'expo-secure-store';


/**
* Blocking functions for Secure Storage of key-value pairs.
**/


// alternative inline pattern:
// (async() => await SecureStore.setItemAsync(key, value)();
export async function secureSet(key, value) {
  try {
    await SecureStore.setItemAsync(key, value);
  } catch (error) {
    console.error(error);
  }
}


// note that this function must be used inside an async function, with await in front of it
export async function secureGet(key) {
  try {
    let value = await SecureStore.getItemAsync(key);
    return value;
  } catch (error) {
    console.error(error);
  }
}


export async function secureDel(key) {
  try {
    await SecureStore.deleteItemAsync(key);
  } catch (error) {
    console.error(error);
  }
}