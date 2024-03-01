import React from "react";

const Avatar = ({ children, bg, className }) => {
  return (
    <div id="avatar">
      <div className={className}>{children}</div>
    </div>
  );
};

export default Avatar;
