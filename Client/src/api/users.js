import axios from "axios";

export const addNewUserToDb = async (user) => {
  const uid = user.uid;
  console.log(user.uid);
  // const response = await axios.post("/api/users/signUp", {
  //   uid: uid,
  // });
  console.log("used added with id:" + uid);
};
