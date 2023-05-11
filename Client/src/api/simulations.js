import axios from "axios";

export const getSimulations = async () => {
  const response = await axios.get("/api/data", {});
  console.log("simulations recieved");
};
