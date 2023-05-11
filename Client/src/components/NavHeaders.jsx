import React from "react";
import { Link, useNavigate } from "react-router-dom";
const NavHeaders = ({ navBarLinks }) => {
  const navigate = useNavigate();

  return (
    <div className="flex">
      {navBarLinks.map((link) => (
        <Link
          key={link.path}
          to={link.path}
          className="hidden sm:block text-gray-200 hover:bg-gray-700 hover:text-white px-3 py-2 rounded-md text-sm font-medium md:flex md:items-center md:px-4 md:py-3 md:text-base"
        >
          {link.name}
        </Link>
      ))}
    </div>
  );
};

export default NavHeaders;
