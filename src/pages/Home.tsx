import React from "react";
import HeroSection from "../components/HeroSection";
import ProjectIntroduction from "../components/ProjectIntroduction";
import PageWrapper from "../components/PageWrapper";

const Home: React.FC = () => {
    return (
        <PageWrapper>
            {/* Hero Section */}
            <HeroSection />

            {/* Project Introduction */}
            <ProjectIntroduction />
        </PageWrapper>
    );
};

export default Home;
