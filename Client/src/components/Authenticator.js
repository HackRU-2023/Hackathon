import {
  signInWithEmailAndPassword,
  signOut,
  createUserWithEmailAndPassword,
} from "firebase/auth";
import { auth } from "./FireBaseAuth";
import { addNewUserToDb } from "../api/users";

export function login(email, password) {
  try {
    return signInWithEmailAndPassword(auth, email, password)
      .then((userCredential) => {
        console.log("logged in");
        return userCredential.user;
      })
      .catch((error) => {
        console.log("Error in login caught" + error);
      });
  } catch (error) {
    console.log("Error in login caught" + error);
  }
}

export async function logout() {
  try {
    await signOut(auth);
    console.log("Logged out");
  } catch (error) {
    console.log("Error in logout caught" + error);
  }
}

export async function signUp(auth, email, password) {
  try {
    const userCredential = await createUserWithEmailAndPassword(
      auth,
      email,
      password
    );
    const user = userCredential.user;
    console.log(user);
    addNewUserToDb(user);
    return { status: true };
  } catch (e) {
    return { status: false, message: e.message };
  }
}
