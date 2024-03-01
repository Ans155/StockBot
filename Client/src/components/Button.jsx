import React from "react";

const Button = ({ text, handleClick }) => {
  return (
    <button id="loginButton" onClick={handleClick} label="Ask me Anything">
      {text}
    </button>
  );
};

export default Button;
