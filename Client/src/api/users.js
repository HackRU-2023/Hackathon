import axios from "axios";

export const addNewUserToDb = async (user) => {
  const uid = user.uid;
  console.log(user.uid);
  const response = await axios.get(`/api/users/${uid}`);
  console.log("user retrieved");
};
