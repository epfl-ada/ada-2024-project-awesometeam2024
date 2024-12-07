import React from "react";
import { useNavigate } from "react-router-dom";
import { motion } from "framer-motion";
import heroBackground from "../assets/movie-bg.jpg"; // Movie-related background image

const HeroSection: React.FC = () => {
    const navigate = useNavigate();

    // Animation Variants
    const fadeIn = {
        hidden: { opacity: 0, y: -20 },
        visible: { opacity: 1, y: 0 },
    };

    const grow = {
        hidden: { opacity: 0, scale: 0.8 },
        visible: { opacity: 1, scale: 1 },
    };

    return (
        <section className="relative h-screen flex flex-col items-center justify-center bg-gradient-to-br from-gray-900 via-black to-gray-800 text-white">
            {/* Main Title */}
            <motion.h1
                className="text-4xl md:text-6xl font-extrabold mb-4 text-center"
                initial="hidden"
                animate="visible"
                variants={fadeIn}
                transition={{ duration: 0.6 }}
            >
                Lights, Camera, <span className="text-accent">Data!</span>
            </motion.h1>

            {/* Subtitle */}
            <motion.p
                className="text-lg md:text-xl text-center max-w-3xl mx-auto mb-8"
                initial="hidden"
                animate="visible"
                variants={fadeIn}
                transition={{ duration: 0.8, delay: 0.2 }}
            >
                Discover the secrets behind box office success and predict the future of cinema through advanced data analysis.
            </motion.p>

            {/* Interactive Box */}
            <motion.div
                className="relative w-3/4 md:w-1/2 h-48 md:h-64 bg-cover bg-center cursor-pointer shadow-lg rounded-lg overflow-hidden transform transition-transform hover:scale-105"
                style={{ backgroundImage: `url(${heroBackground})` }}
                onClick={() => navigate("/project-overview")}
                initial="hidden"
                animate="visible"
                variants={grow}
                transition={{ duration: 0.8, delay: 0.4 }}
                aria-label="Start the Journey"
            >
                {/* Overlay Text */}
                <div className="absolute inset-0 bg-black bg-opacity-50 flex items-center justify-center">
                    <h2 className="text-2xl md:text-3xl font-bold text-white">
                        Start the Journey
                    </h2>
                </div>
            </motion.div>
        </section>
    );
};

export default HeroSection;
