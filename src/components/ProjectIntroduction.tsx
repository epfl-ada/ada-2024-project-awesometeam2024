import React from "react";
import { motion } from "framer-motion";

const ProjectIntroduction: React.FC = () => {
    return (
        <section className="py-16 bg-gray-900 text-white">
            <div className="container mx-auto px-6 md:px-12">
                {/* Section Title */}
                <motion.h2
                    className="text-3xl md:text-4xl font-bold text-center mb-6"
                    initial={{ opacity: 0 }}
                    whileInView={{ opacity: 1 }}
                    viewport={{ once: true }}
                    transition={{ duration: 0.6 }}
                >
                    Welcome to Our Box Office Analysis Journey
                </motion.h2>

                {/* Description */}
                <motion.p
                    className="text-lg md:text-xl leading-relaxed max-w-4xl mx-auto text-center"
                    initial={{ opacity: 0, y: 50 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    viewport={{ once: true }}
                    transition={{ duration: 0.6, delay: 0.3 }}
                >
                    The movie industry is a realm of creativity, innovation, and intense competition.
                    Our project explores what makes a movie a financial success. Is it the genre,
                    the star-studded cast, or perhaps the runtime? Dive into our data-driven journey
                    and uncover the story behind the silver screen.
                </motion.p>

                {/* Interactive Graph Placeholder */}
                <motion.div
                    className="mt-16"
                    initial={{ opacity: 0, scale: 0.8 }}
                    animate={{ opacity: 1, scale: 1 }}
                    transition={{ duration: 1, delay: 0.3 }}
                >
                    <div className="w-full h-64 bg-gray-800 rounded-lg flex items-center justify-center">
                        <p className="text-gray-500">Interactive Graphs Coming Soon...</p>
                    </div>
                </motion.div>
            </div>
        </section>
    );
};

export default ProjectIntroduction;
