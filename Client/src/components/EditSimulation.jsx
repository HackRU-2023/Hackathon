import React, { useState, useEffect } from "react";
import axios from "axios";

const EditSimulation = ({
  mainSimulationConfig,
  editSimulation,
  setShowEditSimulation,
  setView,
}) => {
  const [skills, setSkills] = useState([]);
  const [emotions, setEmotions] = useState([]);
  const [simulationConfig, setSimulationConfig] = useState({});
  const [selectedEmotion, setSelectedEmotion] = useState("");

  useEffect(() => {
    const fetchSkills = async () => {
      const response = await axios.get("/api/skills_fill");
      const skillsArray = Object.values(response.data.personal);
      const emotionsArray = Object.values(response.data.emotion);
      setSkills(skillsArray);
      setEmotions(emotionsArray);
      setSimulationConfig(
        skillsArray.reduce((acc, skill) => {
          acc[skill] = 0;
          return acc;
        }, {})
      );
    };
    fetchSkills();
  }, []);

  const saveHandler = () => {
    editSimulation(simulationConfig);
    setShowEditSimulation(false);
    console.log(simulationConfig);
  };
  const startHandler = () => {
    editSimulation(simulationConfig);
    setView("simulator");
  };

  const handleEmotionChange = (event) => {
    setSelectedEmotion(event.target.value);
  };

  return (
    <div className="p-4 bg-white rounded-md shadow-lg">
      <h3 className="text-xl font-semibold mb-4">
        Edit Simulation Configuration
      </h3>
      <ul className="space-y-4">
        {skills.map((skill, index) => (
          <li key={index} className="flex items-center">
            <label htmlFor={`skill-${index}`} className="mr-2 w-1/3">
              {skill}
            </label>
            <input
              type="range"
              id={`skill-${index}`}
              className="mr-2 w-2/3"
              min="0"
              max="100"
              value={simulationConfig[skill]}
              onChange={(e) => {
                setSimulationConfig({
                  ...simulationConfig,
                  [skill]: e.target.value,
                });
              }}
            />
            <span className="ml-2">{simulationConfig[skill]}</span>{" "}
          </li>
        ))}
      </ul>
      <div className="mt-4">
        <h4 className="mb-2">Select Emotion:</h4>
        {emotions.map((emotion, index) => (
          <div key={index}>
            <input
              type="radio"
              id={`emotion-${index}`}
              name="emotion"
              value={emotion}
              checked={selectedEmotion === emotion}
              onChange={handleEmotionChange}
            />
            <label htmlFor={`emotion-${index}`} className="ml-2">
              {emotion}
            </label>
          </div>
        ))}
      </div>
      <div className="flex justify-center items-center mt-4 space-x-4">
        <button
          className="bg-blue-600 hover:bg-blue-700 text-white rounded-md mr-4 p-3"
          onClick={saveHandler}
        >
          Save Configuration
        </button>
        <button
          className="bg-blue-600 hover:bg-blue-700 text-white rounded-md ml-4 p-3"
          onClick={startHandler}
        >
          Start With Configuration
        </button>
      </div>
    </div>
  );
};

export default EditSimulation;
