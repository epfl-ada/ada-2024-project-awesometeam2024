import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import React, { lazy, Suspense } from "react";
import "bootstrap/dist/css/bootstrap.min.css"; // Bootstrap styles

// Lazy-loaded Pages
const Home = lazy(() => import("./pages/Home"));
const TeamSection = lazy(() => import("./pages/TeamSection"));
const About = lazy(() => import("./pages/About"));
const Explore = lazy(() => import("./pages/Explore"));
const Predict = lazy(() => import("./pages/Predict"));

// Components
import ScrollToTop from "./components/ScrollToTop";

// Fallback Loader
const Loader = () => (
    <div className="flex items-center justify-center h-screen bg-neutral text-white">
        <p className="text-xl animate-pulse">Loading...</p>
    </div>
);

function App() {
    return (
        <Router>
            {/* Ensure smooth scrolling */}
            <ScrollToTop />

            {/* Suspense for lazy loading */}
            <Suspense fallback={<Loader />}>
                <Routes>
                    {/* Main Pages */}
                    <Route path="/" element={<DynamicTitle title="Home | Lights, Camera, Data!"><Home /></DynamicTitle>} />
                    <Route path="/team" element={<DynamicTitle title="Meet the Team"><TeamSection /></DynamicTitle>} />
                    <Route path="/about" element={<DynamicTitle title="About Us"><About /></DynamicTitle>} />
                    <Route path="/explore" element={<DynamicTitle title="Explore Data Insights"><Explore /></DynamicTitle>} />
                    <Route path="/predict" element={<DynamicTitle title="Predict Movie Success"><Predict /></DynamicTitle>} />
                </Routes>
            </Suspense>
        </Router>
    );
}

// DynamicTitle Wrapper Component for updating document.title
const DynamicTitle: React.FC<{ title: string; children: React.ReactNode }> = ({ title, children }) => {
    React.useEffect(() => {
        document.title = title;
    }, [title]);

    return <>{children}</>;
};

export default App;
