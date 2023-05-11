import React, { useRef } from "react";
import { Link, useNavigate } from "react-router-dom";
import useUser from "../hooks/useUser";
import { MdOutlineDeliveryDining } from "react-icons/md";
import { RiCustomerService2Fill } from "React-icons/ri";
import DropDown from "./DropDown";
import NavHeaders from "./NavHeaders";

const NavBar = () => {
  const { user } = useUser();
  const registeredUserNavLinks = [
    { name: "Simulation", path: "/simulator" },
    // { name: "Shop", path: "/shop" },
    // { name: "Chart", path: "/chart" },
  ];
  const unRegisteredUserNavLinks = [
    { name: "How To", path: "/guide" },
    // { name: "Shop", path: "/shop" },
  ];
  const registeredDropDownLinks = [
    { name: "My Profile", path: "/profile" },
    { name: "Basic Info", path: "/info" },
    { name: "Team Info", path: "/team" },
    { name: "Friends", path: "/friends" },
    { name: "Statistics", path: "/statistics" },
    { name: "Achievements", path: "/achievements" },
    { name: "Settings", path: "/settings" },
  ];
  const unRegisteredDropDownLinks = [{ name: "Settings", path: "/settings" }];

  return (
    <nav className="bg-bg-navbar-custom border-b-4 border-black fixed top-0 w-full">
      <div className="flex justify-between items-center px-4 py-3 md:px-10 md:py-5">
        <div className="flex items-center">
          <Link
            to="/"
            className="text-gray-200 hover:animate-pulse hover:bg-gray-700 hover:text-white px-3 rounded-md text-sm font-medium"
          >
            <RiCustomerService2Fill size={48} />
          </Link>
        </div>
        <div className="flex">
          {user ? (
            <NavHeaders navBarLinks={registeredUserNavLinks} />
          ) : (
            <NavHeaders navBarLinks={unRegisteredUserNavLinks} />
          )}
          {user ? (
            <DropDown
              dropDownLinks={registeredDropDownLinks}
              navBarLinks={registeredUserNavLinks}
              user={user}
            />
          ) : (
            <DropDown
              dropDownLinks={unRegisteredDropDownLinks}
              navBarLinks={unRegisteredUserNavLinks}
              user={user}
            />
          )}
        </div>
      </div>
    </nav>
  );
};

export default NavBar;
