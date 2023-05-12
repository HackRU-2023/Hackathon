import React, { useEffect, useState } from "react";
import axios from "axios";

const PickSimulation = ({ onSelect, setSimulationConfig, setView }) => {
  const [simulationTemplates, setSimulationTemplates] = useState([]);
  const [activeTemplate, setActiveTemplate] = useState(null);

  useEffect(() => {
    const fetchSimulationTemplates = async () => {
      try {
        const response = await axios.get("/api/skills_template");
        setSimulationTemplates(response.data);
      } catch (error) {
        console.error("Error fetching simulation templates:", error);
      }
    };

    fetchSimulationTemplates();
  }, []);

  const handleSelect = (template) => {
    onSelect(template);
    setActiveTemplate(activeTemplate === template ? null : template);
  };

  const handleStart = () => {
    if (activeTemplate) {
      setSimulationConfig(activeTemplate);
      setView("simulator");
    }
  };

  return (
    <div className="p-4 bg-white rounded-md shadow-lg">
      <h3 className="text-xl font-semibold mb-4">Pick a Simulation Template</h3>
      <ul className="space-y-4">
        {simulationTemplates.map((template, index) => (
          <li key={index} className="flex flex-col items-start mb-4">
            <button
              className="bg-blue-600 text-white px-4 py-2 rounded-md mb-2 w-full"
              onClick={() => handleSelect(template)}
            >
              {template.subject}
            </button>
            {activeTemplate === template && (
              <div className="flex space-x-4">
                <div>
                  <h4 className="mb-2 font-semibold">Emotion:</h4>
                  <table className="table-auto">
                    <tbody>
                      {Object.entries(template.emotion).map(([key, value]) => (
                        <tr key={key}>
                          <td className="border px-4 py-2">{key}</td>
                          <td className="border px-4 py-2">{value}</td>
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </div>
                <div>
                  <h4 className="mb-2 font-semibold">Personal:</h4>
                  <table className="table-auto">
                    <tbody>
                      {Object.entries(template.personal).map(([key, value]) => (
                        <tr key={key}>
                          <td className="border px-4 py-2">{key}</td>
                          <td className="border px-4 py-2">{value}</td>
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </div>
                <button
                  className="bg-green-600 text-white px-4 py-2 rounded-md mt-4"
                  onClick={handleStart}
                >
                  Start
                </button>
              </div>
            )}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default PickSimulation;
