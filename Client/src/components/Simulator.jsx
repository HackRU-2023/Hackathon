import React, { useState } from "react";
import {
  SpeechConfig,
  AudioConfig,
  SpeechRecognizer,
} from "microsoft-cognitiveservices-speech-sdk";
import { exchangeTranscript } from "../api/agents";

const Simulator = (simulatorConfig) => {
  const [isListening, setIsListening] = useState(false);
  const [mp3Urls, setMp3Urls] = useState([]);

  const [isSimulationRunning, setIsSimulationRunning] = useState(false);
  console.log(simulatorConfig);
  const handleButtonClick = () => {
    setIsSimulationRunning(!isSimulationRunning);
  };

  const startListening = () => {
    setIsListening(true);

    // Set up your Azure Speech API key and region
    const speechConfig = SpeechConfig.fromSubscription(
      "f7d8cf826d7644f2bbbb73e3a04e00c6",
      "eastus"
    );

    // Configure the audio input to use the default microphone
    const audioConfig = AudioConfig.fromDefaultMicrophoneInput();

    // Create the speech recognizer with the given configurations
    const recognizer = new SpeechRecognizer(speechConfig, audioConfig);

    recognizer.recognized = (s, e) => {
      if (e.result.reason === 3) {
        console.log(e.result.text);
        handleTranscriptReady(e.result.text);
        console.log(`RECOGNIZED: Text=${e.result.text}`);
      }
    };

    recognizer.canceled = (s, e) => {
      console.log(`CANCELED: Reason=${e.reason}`);

      if (e.reason === 1) {
        recognizer.stopContinuousRecognitionAsync();
      }
    };

    recognizer.sessionStopped = (s, e) => {
      console.log("Session stopped");
      recognizer.stopContinuousRecognitionAsync();
      setIsListening(false);
    };

    // Start the continuous recognition
    recognizer.startContinuousRecognitionAsync();
  };
  const stopListening = () => {
    setIsListening(false);
  };

  const handleTranscriptReady = async (transcript) => {
    const mp3Blob = await exchangeTranscript(transcript);
    const newMp3Url = URL.createObjectURL(mp3Blob);
    setMp3Urls((prevUrls) => [...prevUrls, newMp3Url]);
  };

  return (
    <div className="min-h-screen pt-20 flex flex-col items-center justify-center bg-gray-100">
      <div className="relative w-3/4 h-1/4 md:w-2/5 md:h-1/4 bg-white flex items-center justify-center shadow-xl rounded-lg overflow-hidden">
        <div className="w-1/2 h-full bg-white flex items-center justify-center border-r-2 border-black">
          <img
            src="../robot.jpg"
            alt="Robot Image"
            className="max-h-full max-w-full object-contain pr-4"
          />
        </div>
        <div className="w-px h-full bg-black"></div>
        <div className="w-1/2 h-full bg-white flex items-center justify-center">
          <img
            src="../person.png"
            alt="Profile Image"
            className="max-h-full max-w-full object-contain rounded-full pl-4"
          />
        </div>
      </div>
      <button
        className={`mt-8 px-6 py-3 rounded-md ${
          isSimulationRunning ? "bg-red-600" : "bg-green-600"
        } text-white`}
        onClick={handleButtonClick}
      >
        {isSimulationRunning ? "Stop Simulation" : "Start Simulation"}
      </button>

      <div>
        {isListening ? (
          <button onClick={stopListening}>Stop Listening</button>
        ) : (
          <button onClick={startListening}>Start Listening</button>
        )}
      </div>

      <div className="mt-6">
        {mp3Urls.map((url, index) => (
          <div key={index} className="mb-4">
            <h3>AI Response {index + 1}:</h3>
            <audio src={url} controls />
          </div>
        ))}
      </div>
    </div>
  );
};

export default Simulator;
