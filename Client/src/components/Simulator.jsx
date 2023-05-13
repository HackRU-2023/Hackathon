import React, { useState, useRef } from "react";
import {
  SpeechConfig,
  AudioConfig,
  SpeechRecognizer,
} from "microsoft-cognitiveservices-speech-sdk";
import { exchangeTranscript } from "../api/agents";
import axios from "axios";

const Simulator = ({ simulatorConfig, setView, setResults }) => {
  const [isListening, setIsListening] = useState(false);
  const [mp3Urls, setMp3Urls] = useState([]);
  const [finish, setFinish] = useState(false);
  const [speaker, setSpeaker] = useState(null); // New state variable

  //   const [isSimulationRunning, setIsSimulationRunning] = useState(false);
  console.log(simulatorConfig);
  //   const handleButtonClick = () => {
  //     setIsSimulationRunning(!isSimulationRunning);
  //   };

  const debounce = (func, wait) => {
    let timeout;
    return (...args) => {
      const context = this;
      clearTimeout(timeout);
      timeout = setTimeout(() => {
        timeout = null;
        func.apply(context, args);
      }, wait);
    };
  };
  const handleTranscriptReady = async (transcript) => {
    const mp3Blob = await exchangeTranscript(transcript);
    if (mp3Blob == "") {
      return;
    }
    setSpeaker("robot"); // Set the speaker

    const newMp3Url = URL.createObjectURL(mp3Blob);
    setMp3Urls((prevUrls) => [...prevUrls, newMp3Url]);
  };
  const debouncedHandleTranscriptReady = debounce(handleTranscriptReady, 2000);
  const recognizerRef = useRef(null);

  const startListening = () => {
    setIsListening(true);

    // Set up your Azure Speech API key and region
    const speechConfig = SpeechConfig.fromSubscription(
      "<secret_key>",
      "<region>"
    );

    // Configure the audio input to use the default microphone
    const audioConfig = AudioConfig.fromDefaultMicrophoneInput();

    // Create the speech recognizer with the given configurations
    const recognizer = new SpeechRecognizer(speechConfig, audioConfig);
    recognizerRef.current = recognizer;

    // Whenever speech is recognized, set the speaker to "person"
    recognizer.recognized = (s, e) => {
      if (e.result.reason === 3) {
        if (e.result.text == "") {
          return;
        }
        setSpeaker("person"); // Set the speaker
        debouncedHandleTranscriptReady(e.result.text);
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

  const stopListening = async () => {
    if (recognizerRef.current) {
      recognizerRef.current.stopContinuousRecognitionAsync();
    }
    setIsListening(false);
    const response = await axios.get("/api/get_review", {});
    console.log(response.data);
    setResults(response.data);
    setView("results");
  };

  return (
    <div className="min-h-screen pt-20 flex flex-col items-center justify-center bg-gray-100">
      <div className="relative w-3/4 h-1/4 md:w-2/5 md:h-1/4 bg-white flex items-center justify-center shadow-xl rounded-lg overflow-hidden">
        <div
          className={`w-1/2 h-full bg-white flex items-center justify-center border-r-2 border-black ${
            speaker === "robot" ? "border-blue-500 border-4" : ""
          }`}
        >
          <img
            src="../robot.jpg"
            alt="Robot Image"
            className="max-h-full max-w-full object-contain pr-4"
          />
        </div>
        <div className="w-px h-full bg-black"></div>
        <div
          className={`w-1/2 h-full bg-white flex items-center justify-center ${
            speaker === "person" ? "border-blue-500 border-4" : ""
          }`}
        >
          <img
            src="../person.png"
            alt="Profile Image"
            className="max-h-full max-w-full object-contain rounded           w-full pl-4"
          />
        </div>
      </div>
      {/* <button
        className={`mt-8 px-6 py-3 rounded-md ${
          isSimulationRunning ? "bg-red-600" : "bg-green-600"
        } text-white`}
        onClick={handleButtonClick}
      >
        {isSimulationRunning ? "Stop Simulation" : "Start Simulation"}
      </button> */}

      <div>
        {isListening ? (
          <button
            className="mt-8 px-6 py-3 rounded-md bg-red-400 hover:bg-red-600"
            onClick={stopListening}
          >
            Stop Listening
          </button>
        ) : (
          <button
            className="mt-8 px-6 py-3 rounded-md bg-green-400 hover:bg-green-600"
            onClick={startListening}
          >
            Start Listening
          </button>
        )}
      </div>

      <div className="mt-6">
        {mp3Urls.map((url, index) => (
          <div key={index} className="mb-4">
            <h3>AI Response {index + 1}:</h3>
            <audio src={url} controls autoPlay />
          </div>
        ))}
      </div>
    </div>
  );
};

export default Simulator;
