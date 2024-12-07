import React from "react";
import TeamMemberCard from "../components/TeamMemberCard";
import aliceImage from "../assets/alice.jpg";
import bobImage from "../assets/bob.jpg";
import charlieImage from "../assets/charlie.jpg";
import dianaImage from "../assets/diana.jpg";
import eveImage from "../assets/eve.jpg";
import { motion } from "framer-motion";
import PageWrapper from "../components/PageWrapper";

const TeamSection: React.FC = () => {
    const teamMembers = [
        {
            name: "Alice",
            role: "Data Analyst",
            image: aliceImage,
            citation: "“Numbers tell a story; I make them sing.”",
            socialLinks: {
                linkedin: "https://linkedin.com/in/alice",
                github: "https://github.com/alice",
            },
        },
        {
            name: "Bob",
            role: "ML Engineer",
            image: bobImage,
            citation: "“Turning data into decisions with AI.”",
            socialLinks: {
                linkedin: "https://linkedin.com/in/bob",
                github: "https://github.com/bob",
            },
        },
        {
            name: "Charlie",
            role: "Frontend Developer",
            image: charlieImage,
            citation: "“Designing experiences, one pixel at a time.”",
        },
        {
            name: "Diana",
            role: "Designer",
            image: dianaImage,
            citation: "“Creativity meets functionality in my designs.”",
        },
        {
            name: "Eve",
            role: "Project Manager",
            image: eveImage,
            citation: "“Bringing order to chaos and success to vision.”",
            socialLinks: {
                linkedin: "https://linkedin.com/in/eve",
            },
        },
    ];

    return (
        <PageWrapper>
            <section
                id="team"
                className="py-16 bg-gray-900 text-white relative overflow-hidden"
            >
                {/* Animated Background */}
                <div className="absolute inset-0 bg-hero-gradient opacity-10 pointer-events-none"></div>

                {/* Section Title */}
                <motion.h2
                    className="text-3xl lg:text-4xl font-bold text-center mb-12"
                    initial={{ opacity: 0, y: -20 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    viewport={{ once: true }}
                    transition={{ duration: 0.6, ease: "easeOut" }}
                >
                    Meet Our Team
                </motion.h2>

                {/* Team Grid */}
                <motion.div
                    className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-12 px-6 md:px-12"
                    initial={{ opacity: 0 }}
                    whileInView={{ opacity: 1 }}
                    viewport={{ once: true }}
                    transition={{ duration: 0.8, ease: "easeOut", delayChildren: 0.2 }}
                >
                    {teamMembers.map((member) => (
                        <TeamMemberCard
                            key={member.name}
                            name={member.name}
                            role={member.role}
                            image={member.image}
                            citation={member.citation}
                            socialLinks={member.socialLinks}
                        />
                    ))}
                </motion.div>
            </section>
        </PageWrapper>
    );
};

export default TeamSection;
