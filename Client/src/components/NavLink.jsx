import React, { useContext } from "react";
import { Link } from "react-router-dom";

const NavLinks = ({ svg, link, text, setChatLog }) => {

  const handleClick = async (text) => {
    if (text === "Clear Conversations") setChatLog([]);
   
  };

  return (
    <Link
      to={link}
      target={link && "_blank"}
      rel="noreferrer"
      style={{ textDecoration: "none" }}
      onClick={() => handleClick(text)}
    >
      <div className="navPrompt">
        {svg}
        <p>{text}</p>
      </div>
    </Link>
  );
};

export default NavLinks;
