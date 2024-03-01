import "./normal.css";
import "./App.css";
import Home from "./pages/Home";
import {Route, Routes } from "react-router-dom";

function App() {


  return (
    <div className="App">
      <Routes>
        <Route path="/" element={<Home />} />
      </Routes>
    </div>
  );
}

export default App;
