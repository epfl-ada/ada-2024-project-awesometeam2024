import React from "react";
import { motion } from "framer-motion"; // For animations
import { FaLinkedin, FaGithub } from "react-icons/fa";

interface TeamMemberCardProps {
    name: string;
    role: string;
    image: string;
    citation: string;
    socialLinks?: {
        linkedin?: string;
        github?: string;
    };
}

const TeamMemberCard: React.FC<TeamMemberCardProps> = ({
    name,
    role,
    image,
    citation,
    socialLinks,
}) => {
    return (
        <motion.div
            className="flex flex-col items-center text-center bg-gray-800 p-6 rounded-lg shadow-lg transform transition-all duration-300 hover:shadow-2xl"
            initial={{ opacity: 0, y: 50 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true, amount: 0.3 }}
            transition={{ duration: 0.6, ease: "easeOut" }}
            whileHover={{ scale: 1.05 }} // Hover animation
        >
            {/* Team Member Image */}
            <motion.img
                src={image}
                alt={name}
                className="w-32 h-32 md:w-36 md:h-36 rounded-full border-4 border-accent shadow-lg mb-4 transition-transform duration-300 hover:scale-110"
                whileHover={{ rotate: 5 }} // Slight rotation on hover
            />

            {/* Name and Role */}
            <h3 className="text-xl md:text-2xl font-semibold text-white">{name}</h3>
            <p className="text-gray-400 text-sm md:text-base mb-4">{role}</p>

            {/* Citation */}
            <blockquote className="italic text-gray-300 text-sm md:text-base border-l-4 border-blue-500 pl-4">
                {citation}
            </blockquote>

            {/* Social Links */}
            {socialLinks && (
                <div className="flex space-x-4 mt-4">
                    {socialLinks.linkedin && (
                        <a
                            href={socialLinks.linkedin}
                            target="_blank"
                            rel="noopener noreferrer"
                            className="text-blue-400 hover:text-blue-600 transition"
                            aria-label={`${name}'s LinkedIn`}
                        >
                            <FaLinkedin size={24} />
                        </a>
                    )}
                    {socialLinks.github && (
                        <a
                            href={socialLinks.github}
                            target="_blank"
                            rel="noopener noreferrer"
                            className="text-gray-400 hover:text-gray-600 transition"
                            aria-label={`${name}'s GitHub`}
                        >
                            <FaGithub size={24} />
                        </a>
                    )}
                </div>
            )}
        </motion.div>
    );
};

export default TeamMemberCard;
