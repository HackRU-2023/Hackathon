import React, { useEffect, useState } from "react";
import axios from "axios";

const PickSimulation = ({ onSelect }) => {
  const [simulationTemplates, setSimulationTemplates] = useState([]);

  useEffect(() => {
    const fetchSimulationTemplates = async () => {
      try {
        const response = await axios.get("/api/simulations/templates");
        setSimulationTemplates(response.data);
      } catch (error) {
        console.error("Error fetching simulation templates:", error);
      }
    };

    fetchSimulationTemplates();
  }, []);

  return (
    <div className="p-4 bg-white rounded-md shadow-lg">
      <h3 className="text-xl font-semibold mb-4">Pick a Simulation Template</h3>
      <ul className="space-y-4">
        {simulationTemplates.map((template, index) => (
          <li key={index} className="flex items-center">
            <button
              className="bg-blue-600 text-white px-4 py-2 rounded-md"
              onClick={() => onSelect(template)}
            >
              {template.name}
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default PickSimulation;
