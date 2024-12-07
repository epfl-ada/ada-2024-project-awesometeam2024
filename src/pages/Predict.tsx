import React from "react";
import PageWrapper from "../components/PageWrapper";

const Predict: React.FC = () => {
    return (
        <PageWrapper>
            <div className="flex items-center justify-center h-screen bg-gray-900 text-white">
                <h1 className="text-4xl md:text-6xl font-bold text-center">
                    Incoming... <span className="text-yellow-500">🔮</span>
                </h1>
            </div>
        </PageWrapper>
    );
};

export default Predict;
