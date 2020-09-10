import React from "react";
import { Link } from "react-router-dom";

function Sidebar({ pages }) {
  return (
    <div className="sidebar">
      <ul className="listOfRoutes">
        {pages.map((name, i) => (
          <li key={i}>
            <Link to={name.label}>
              <button className="menuButtons">{name.label}</button>
            </Link>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Sidebar;
