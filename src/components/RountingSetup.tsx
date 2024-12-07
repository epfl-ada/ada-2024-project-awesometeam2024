import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import HeroSection from "./HeroSection";
import ProjectOverview from "./ProjectOverview";

const App: React.FC = () => {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<HeroSection />} />
                <Route path="/project-overview" element={<ProjectOverview />} />
            </Routes>
        </Router>
    );
};

export default App;
