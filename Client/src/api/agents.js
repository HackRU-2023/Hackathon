import axios from "axios";

export const exchangeTranscript = async (transcript) => {
  console.log(transcript);
  const response = await axios.post(
    "/api/transcription_exchange",
    {
      transcript: transcript,
    },
    {
      responseType: "blob",
    }
  );
  console.log("transcript received:" + transcript);

  return response.data;
};
