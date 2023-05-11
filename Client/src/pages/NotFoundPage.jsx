import React from "react";

const NotFoundPage = () => {
  return (
    <div className="w-full pt-10 md:pt-20 bg-gradient-to-r from-gray-100 via-gray-200 to-gray-300 flex flex-col items-center justify-center overflow-hidden bg-fixed ">
      <div className="bg-white p-8 rounded-lg shadow-md w-full max-w-md">
        <h1 className="text-4xl font-bold text-red-500 mb-6">404</h1>
        <h2 className="text-2xl font-semibold text-gray-700 mb-4">
          Page Not Found
        </h2>
        <p className="text-gray-500">
          The page you are looking for does not exist. Please check the URL and
          try again.
        </p>
        <p className="text-gray-500 mt-4 ">
          you can also click on the headphones on the top..
        </p>
      </div>
    </div>
  );
};

export default NotFoundPage;
