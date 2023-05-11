import React from "react";
import { Link } from "react-router-dom";
import useUser from "../hooks/useUser";
import { AiOutlineCustomerService } from "react-icons/ai";
import { FaHeadset } from "react-icons/fa";
import { IoIosPeople } from "react-icons/io";

const HomePage = () => {
  const { user } = useUser();

  return (
    <div className="h-full pt-10 md:pt-32 bg-gradient-to-r from-gray-100 via-gray-200 to-gray-300 flex flex-col overflow-hidden bg-fixed">
      <div className="text-center mb-12 md:mb-24">
        <h1 className="text-4xl sm:text-5xl md:text-7xl font-bold text-gray-800 mb-8">
          Customer Service Simulator
        </h1>
        <p className="text-lg sm:text-xl md:text-2xl text-gray-700 mb-8">
          Improve your customer service skills and manage a successful support
          team with our interactive simulator!
        </p>
        <Link
          to={user ? "/simulator" : "/login"}
          className="bg-indigo-600 hover:bg-indigo-800 text-white font-bold py-3 px-24 rounded-full text-lg sm:text-xl md:text-2xl"
        >
          Get Started
        </Link>
      </div>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-8 md:gap-12">
        <div className="text-center">
          <AiOutlineCustomerService className="text-6xl mx-auto mb-4 text-indigo-600" />
          <h2 className="text-2xl font-semibold mb-4">Enhance Your Skills</h2>
          <p className="text-gray-700">
            Develop your communication, empathy, and problem-solving skills to
            excel in any customer service role.
          </p>
        </div>
        <div className="text-center">
          <FaHeadset className="text-6xl mx-auto mb-4 text-indigo-600" />
          <h2 className="text-2xl font-semibold mb-4">Realistic Scenarios</h2>
          <p className="text-gray-700">
            Engage with simulated customers in various scenarios to gain
            practical experience and boost your confidence.
          </p>
        </div>
        <div className="flex-col justify-center text-center">
          <IoIosPeople className="text-6xl mx-auto mb-4 text-indigo-600" />
          <h2 className="text-2xl font-semibold mb-4">Lead Your Team</h2>
          <p className="text-gray-700">
            Learn how to manage and motivate a customer service team, optimize
            workflow, and track performance metrics.
          </p>
        </div>
      </div>
    </div>
  );
};

export default HomePage;
