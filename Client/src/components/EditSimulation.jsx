import React, { useState } from "react";

const EditSimulation = ({
  mainSimulationConfig,
  editSimulation,
  setShowEditSimulation,
}) => {
  const skills = [
    "empathy",
    "patience",
    "product knowledge",
    "problem solving",
    "time-management",
    "multi-tasking",
    "active listening",
    "conflict resolution",
    "non-verbal communication",
    "verbal communication",
    "emotional intelligence",
  ];
  const [simulationConfig, setSimulationConfig] = useState(
    mainSimulationConfig ||
      skills.reduce((acc, skill) => {
        acc[skill] = 0;
        return acc;
      }, {})
  );

  const saveHandler = () => {
    editSimulation(simulationConfig);
    setShowEditSimulation(false);
    console.log(simulationConfig);
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
      <button
        className="mt-4 bg-blue-600 text-white px-4 py-2 rounded-md"
        onClick={saveHandler}
      >
        Save Configuration
      </button>
    </div>
  );
};

export default EditSimulation;
