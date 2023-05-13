import React from "react";

const Results = ({ results }) => {
  const renderResults = () => {
    if (results && results) {
      const parts = results.split(" - ");
      return parts.map((part, index) => {
        const lines = part.split("\n").map((line, lineIndex) => (
          <React.Fragment key={lineIndex}>
            {line}
            <br />
          </React.Fragment>
        ));
        return (
          <p key={index} className="mb-4 text-lg text-black font-semibold">
            {lines}
          </p>
        );
      });
    }
    return null;
  };

  return (
    <div className="container bg-gray-400 mx-auto px-4 py-6 space-y-6  shadow-lg rounded-md">
      <h1 className="text-4xl font-bold text-black">Results</h1>
      {renderResults()}
    </div>
  );
};

export default Results;
