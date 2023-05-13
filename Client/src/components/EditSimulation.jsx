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
      // console.log(response.data[0]);
      const skillsArray = Object.values(response.data[0].personal);
      console.log(skillsArray);
      const simulationData = {
        personality: skillsArray,
        emotions: "ANGRY",
        situation_description: response.data[0].position,
      };
      setSimulationConfig(simulationData);
      // console.log(skillsArray);
      const emotionsArray = Object.values(response.data[0].emotion);
      setSkills(skillsArray);
      setEmotions(emotionsArray);
    };
    fetchSkills();
  }, []);

  // const saveHandler = () => {
  //   editSimulation(simulationConfig);
  //   setShowEditSimulation(false);
  //   console.log(simulationConfig);
  // };
  const startHandler = async () => {
    editSimulation(simulationConfig);
    const newResponse = await axios.post("/api/situation_description", {
      emotions: simulationConfig.emotions,
      personality: simulationConfig.personality,
      situation_description: "simulationConfig.situation_description",
    });
    setView("simulator");
  };

  const handleEmotionChange = (event) => {
    setSelectedEmotion(event.target.value);
  };

  return (
    <div className="p-8 bg-white rounded-md shadow-lg">
      <h3 className="text-xl font-semibold mb-4">
        Edit Simulation Configuration
      </h3>
      <ul className="space-y-4">
        {skills.map((skill, index) => (
          <li key={index} className="flex items-center space-x-4">
            <label htmlFor={`skill-${index}`} className="w-1/3 text-gray-700">
              {skill}
            </label>
            <input
              type="range"
              id={`skill-${index}`}
              className="mr-2 w-1/2"
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
            <span className="text-gray-600">{simulationConfig[skill]}</span>{" "}
          </li>
        ))}
      </ul>
      <div className="mt-8">
        <div className="mt-4 flex flex-wrap justify-center items-center">
          <h4 className=" text-lg text-gray-700 w-full text-center border-b-2 border-black mb-3">
            Select Emotion:
          </h4>
          {emotions.map((emotion, index) => (
            <div key={index} className="flex items-center space-x-2 m-2">
              <input
                type="radio"
                id={`emotion-${index}`}
                name="emotion"
                value={emotion}
                className="form-radio text-blue-500 font-bold"
                checked={selectedEmotion === emotion}
                onChange={handleEmotionChange}
              />
              <label htmlFor={`emotion-${index}`} className="text-gray-700">
                {emotion}
              </label>
            </div>
          ))}
        </div>
      </div>

      <div className="flex justify-center items-center mt-6 space-x-4">
        {/* <button
          className="bg-blue-600 hover:bg-blue-700 text-white rounded-md p-3 transition-colors duration-200"
          onClick={saveHandler}
        >
          Save Configuration
        </button> */}
        <button
          className="bg-blue-600 hover:bg-blue-700 text-white rounded-md p-3 transition-colors duration-200"
          onClick={startHandler}
        >
          Start With Configuration
        </button>
      </div>
    </div>
  );
};

export default EditSimulation;
