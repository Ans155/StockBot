import React from "react";
import PulseLoader from "react-spinners/PulseLoader";

const Loading = () => {
  return (
    <div style={{ display: "flex", alignItems: "center", justifyContent: "center" }}>
      <p style={{ color: "#FFD580", fontWeight: "bold", fontSize: "14px", marginRight: "10px" }}>StockBot is thinking</p>
      <PulseLoader
        color={"#FFD580"}
        loading={true}
        size={5}
        aria-label="Loading Spinner"
        data-testid="loader"
      />
    </div>
  );
};

export default Loading;
