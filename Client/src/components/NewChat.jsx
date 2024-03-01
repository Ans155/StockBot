import React from "react";

const NewChat = ({ setChatLog, setShowMenu }) => {
  return (
    <div
      className="sideMenuButton"
      onClick={() => {
        setChatLog([]);
        setShowMenu(false);
      }}
    >
      <span>+</span>
      <span>
      New chat
      </span>
      
    </div>
  );
};

export default NewChat;
