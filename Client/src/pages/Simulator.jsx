import React, { useState } from "react";
import { AiOutlinePlus } from "react-icons/ai";
import { AiFillEdit } from "react-icons/ai";
import { getSimulations } from "../api/simulations";
import useUser from "../hooks/useUser";
import EditSimulation from "../components/editSimulation";
const SimulatorPage = () => {
  const [simulations, setSimulations] = useState([]);
  const { user } = useUser();
  const [showEditSimulation, setShowEditSimulation] = useState(false);
  const [simulationConfig, setSimulationConfig] = useState(null);
  const fetchSimulations = () => {
    const response = getSimulations();
    console.log(response);
    setSimulations(response);
  };

  // Toggle the visibility of the EditSimulation component
  const toggleEditSimulation = () => {
    setShowEditSimulation(!showEditSimulation);
  };

  return (
    <div className="w-full pt-10 md:pt-20 bg-gradient-to-r from-gray-100 via-gray-200 to-gray-300 flex flex-col items-center justify-center overflow-hidden bg-fixed ">
      <div className="bg-white p-8 rounded-lg shadow-md w-full max-w-2xl">
        <h1 className="text-4xl font-bold text-gray-800 mb-6 flex justify-center">
          Welcome{user ? `${user.name || ""}` : ""}, Happy Simulation!
        </h1>

        <div className="flex-col">
          <div className="flex w-full  ">
            <button
              className="w-full  bg-indigo-600 hover:bg-indigo-800 text-white font-bold py-8 px-4 rounded-tl-md relative border-r-2 border-black"
              onClick={fetchSimulations}
            >
              Start Simulation
            </button>
            <button
              className="bg-indigo-600 rounded-tr-md py-8 px-2 hover:bg-blue-800"
              onClick={toggleEditSimulation}
            >
              <AiFillEdit
                size={42}
                className=" text-white  text-2xl cursor-pointer "
              />
            </button>
          </div>
          {showEditSimulation && (
            <EditSimulation
              mainSimulationConfig={simulationConfig}
              editSimulation={setSimulationConfig}
              setShowEditSimulation={setShowEditSimulation}
            />
          )}
          {!showEditSimulation && (
            <div className="flex border-l-2 border-b-2 border-r-2 border-green-600 w-full rounded-b-md ">
              <button className="flex bg-green-300 justify-center w-full py-2 px-4 hover:bg-green-800  ">
                <span className="text-black font-semibold mr-2 ">
                  Create New Simulation
                </span>
                <AiOutlinePlus className="text-black hover:text-green-800 text-2xl cursor-pointer" />
              </button>
            </div>
          )}
          <div className="flex justify-center border-t-2 border-gray w-full mt-4">
            <span className="my-4 text-xl">Or</span>
          </div>
          <div className="flex bg-indigo-700 w-full">
            <button className="flex justify-center w-full py-2 px-4 rounded-br-md hover:bg-indigo-800">
              <span className="text-white font-semibold mr-2 ">
                Pick a simulation from our templates
              </span>
            </button>
          </div>
        </div>
        <div>{simulations}</div>
      </div>
    </div>
  );
};

export default SimulatorPage;
