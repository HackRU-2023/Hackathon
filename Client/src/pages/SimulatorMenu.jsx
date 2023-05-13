import React, { useState, useEffect } from "react";
import { AiOutlinePlus } from "react-icons/ai";
import { AiFillEdit } from "react-icons/ai";
import { getSimulations } from "../api/simulations";
import useUser from "../hooks/useUser";
import EditSimulation from "../components/editSimulation";
import PickSimulation from "../components/PickSimulation";
import Simulator from "../components/Simulator";
import Results from "../components/Results";
import axios from "axios";
const SimulatorMenu = () => {
  const [simulations, setSimulations] = useState([]);
  const { user } = useUser();
  const [showEditSimulation, setShowEditSimulation] = useState(false);
  const [simulationConfig, setSimulationConfig] = useState(null);
  const [selectedTemplate, setSelectedTemplate] = useState(null);
  const [showTemplateSimulations, setShowTemplateSimulations] = useState();
  const [view, setView] = useState("menu");
  const [results, setResults] = useState(null);
  const handleTemplateSelect = (template) => {
    setSelectedTemplate(template);
  };
  const [userFromDbData, setUserFromDbData] = useState(null);

  const fetchSimulations = () => {
    const response = getSimulations();
    console.log(response);
    setSimulations(response);
  };

  const handleStartFromEasyButton = async () => {
    try {
      const response = await axios({
        method: "get",
        url: "/api/get_agent",
        params: {
          agent_id: user.uid,
        },
      });
      console.log("REs");
      console.log(response.data);
      console.log(response.data[0].position);
      console.log("REs");

      setUserFromDbData(response.data);

      const simulationData = response.data;
      simulationData[0].situation_description = response.data[0].position;

      // setSimulationConfig(response.data);
      const newResponse = await axios.post(
        "/api/situation_description",
        {
          emotions: response.data[0].emotions,
        },
        {
          responseType: "blob",
        }
      );
    } catch (error) {
      console.error("Error fetching agent:", error);
    }
    setView("simulator");
  };

  const renderView = () => {
    switch (view) {
      case "menu":
        return (
          <>
            <div className="w-full h-screen max-w-xl content-center justify-center">
              <div className="flex w-full ">
                <button
                  className="w-full  bg-indigo-600 hover:bg-indigo-800 text-white font-bold py-8 px-4 rounded-tl-md relative border-r-2 border-black"
                  onClick={handleStartFromEasyButton}
                >
                  Start Simulation
                </button>
                <button
                  className="bg-indigo-600 rounded-tr-md py-8 px-2 hover:bg-blue-800"
                  onClick={() => setShowEditSimulation(!showEditSimulation)}
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
                  setView={setView}
                />
              )}

              {!showEditSimulation && (
                <div>
                  <div className="flex justify-center border-t-2 border-gray w-full mt-4">
                    <span className="my-4 text-xl">Or</span>
                  </div>
                  {!showTemplateSimulations ? (
                    <div className="flex bg-indigo-700 w-full">
                      <button
                        className="flex justify-center w-full py-2 px-4 rounded-br-md hover:bg-indigo-800 text-white font-semibold mr-2 "
                        onClick={() => setShowTemplateSimulations(true)}
                      >
                        Pick a simulation from our templates
                      </button>
                    </div>
                  ) : (
                    <PickSimulation
                      onSelect={setSelectedTemplate}
                      setSimulationConfig={setSimulationConfig}
                      setView={setView}
                    />
                  )}
                </div>
              )}
            </div>
          </>
        );
      case "simulator":
        return (
          <Simulator
            // onStopSimulation={() => {
            //   setView("menu");
            // }}
            simulatorConfig={simulationConfig}
            setResults={setResults}
            setView={setView}
          />
        );
      case "results":
        return <Results results={results} />;
      default:
        return null;
    }
  };

  // Toggle the visibility of the EditSimulation component
  const toggleEditSimulation = () => {
    setShowEditSimulation(!showEditSimulation);
  };

  return (
    <div className="w-full h-full  bg-gradient-to-r from-gray-100 via-gray-200 to-gray-300 flex flex-col items-center justify-center  bg-fixed ">
      <div className="bg-white h-screen pt-14 rounded-lg  w-full ">
        <h1 className="text-4xl font-bold text-gray-800 mb-6 flex justify-center">
          Welcome{user ? `${user.name || ""}` : ""}, Happy Simulation!
        </h1>
        <div className="flex flex-col justify-center items-center ">
          {renderView()}
        </div>
      </div>
    </div>
  );
};

export default SimulatorMenu;
