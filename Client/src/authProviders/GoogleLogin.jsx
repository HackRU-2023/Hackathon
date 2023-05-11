import React from "react";
import { signInWithPopup, GoogleAuthProvider } from "firebase/auth";
import { addNewUserToDb } from "../api/users";
import { auth } from "../components/FireBaseAuth";
import { FcGoogle } from "react-icons/fc";

const GoogleLogin = () => {
  const provider = new GoogleAuthProvider();

  const signIn = async () => {
    try {
      const userCredential = await signInWithPopup(auth, provider);
      console.log(userCredential);
      // Check if the user is new and add to the database
      if (userCredential._tokenResponse.isNewUser) {
        const user = userCredential.user;

        await addNewUserToDb(user);
      }
      console.log("successfully logged in with google account");

      // Handle successful login
    } catch (error) {
      console.log("error with signing in with google provider", error);
    }
  };

  return (
    <FcGoogle
      onClick={signIn}
      className="w-12 h-12 cursor-pointer transition duration-200 ease-in-out hover:scale-110 border-2 border-gray-300 hover:border-black rounded-md"
    />
  );
};

export default GoogleLogin;
