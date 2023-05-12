import React, { useState, useEffect } from "react";
import axios from "axios";

const Results = (results) => {
  const [callGrades, setCallGrades] = useState([]);
  const [userGrades, setUserGrades] = useState([]);

  useEffect(() => {
    const fetchCallGrades = async () => {
      const response = await axios.get("/api/call-grades");
      setCallGrades(response.data);
    };

    const fetchUserGrades = async () => {
      const response = await axios.get("/api/user-grades");
      setUserGrades(response.data);
    };

    fetchCallGrades();
    fetchUserGrades();
  }, []);

  const renderBars = (grades, color) => {
    return grades.map((grade, index) => (
      <div
        key={index}
        className={`bg-${color}-500 h-4 w-${grade * 10}`}
        style={{ width: `${grade * 10}%` }}
      ></div>
    ));
  };

  return (
    <div className="container mx-auto px-4">
      <h1 className="text-2xl font-bold mb-4">Results</h1>
      <div className="grid grid-cols-2 gap-8">
        <div>
          <h2 className="text-xl font-semibold mb-2">Call Grades</h2>
          <div className="space-y-2">{renderBars(callGrades, "blue")}</div>
        </div>
        <div>
          <h2 className="text-xl font-semibold mb-2">User Grades</h2>
          <div className="space-y-2">{renderBars(userGrades, "green")}</div>
        </div>
      </div>
    </div>
  );
};

export default Results;
