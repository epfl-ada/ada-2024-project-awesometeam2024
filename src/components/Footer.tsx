import React from "react";
import { FaGithub } from "react-icons/fa";
import { motion } from "framer-motion";

const Footer: React.FC = () => {
    const currentYear = new Date().getFullYear();

    // Smooth scroll to the top of the page
    const handleScrollToTop = () => {
        window.scrollTo({ top: 0, behavior: "smooth" });
    };

    return (
        <footer className="relative bg-dark py-8 text-center text-gray-400">
            {/* Gradient Overlay */}
            <div className="absolute inset-0 bg-gradient-to-tr from-dark via-neutral to-dark opacity-20 pointer-events-none"></div>

            {/* Tagline */}
            <motion.p
                className="text-lg md:text-xl font-semibold text-white mb-4"
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.6, ease: "easeOut" }}
            >
                Lights, Camera, <span className="text-primary">Data</span>
            </motion.p>

            {/* Social Media Icons */}
            <div className="flex justify-center space-x-6 mb-6">
                <motion.a
                    href="https://github.com/epfl-ada/ada-2024-project-awesometeam2024.git"
                    target="_blank"
                    rel="noopener noreferrer"
                    className="text-gray-400 hover:text-primary transition-all duration-300"
                    aria-label="GitHub Repository"
                    whileHover={{ scale: 1.15 }}
                    whileTap={{ scale: 0.95 }}
                >
                    <FaGithub size={28} />
                </motion.a>
            </div>

            {/* Divider */}
            <motion.div
                className="border-t border-gray-600 w-2/3 mx-auto mb-6"
                initial={{ width: "0%" }}
                animate={{ width: "66%" }}
                transition={{ duration: 0.6, ease: "easeInOut" }}
            ></motion.div>

            {/* Copyright */}
            <div className="mb-4">
                <motion.p
                    className="text-sm md:text-base"
                    initial={{ opacity: 0, x: -20 }}
                    animate={{ opacity: 1, x: 0 }}
                    transition={{ duration: 0.6, ease: "easeOut", delay: 0.2 }}
                >
                    © {currentYear} Lights, Camera, Data. All Rights Reserved.
                </motion.p>
                <motion.p
                    className="text-xs md:text-sm"
                    initial={{ opacity: 0, x: 20 }}
                    animate={{ opacity: 1, x: 0 }}
                    transition={{ duration: 0.6, ease: "easeOut", delay: 0.4 }}
                >
                    Built with <span className="text-red-500">❤️</span> by the Team
                </motion.p>
            </div>

            {/* Back to Top Button */}
            <motion.button
                onClick={handleScrollToTop}
                className="mt-4 px-6 py-3 bg-primary text-white rounded-lg shadow-lg hover:shadow-xl hover:scale-105 transition-transform transform duration-300"
                whileHover={{ y: -3 }}
                whileTap={{ y: 0 }}
            >
                Back to Top
            </motion.button>
        </footer>
    );
};

export default Footer;
