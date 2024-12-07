import React, { useState, useEffect } from "react";
import { Navbar, Nav, Container } from "react-bootstrap";
import { Link, useLocation } from "react-router-dom";
import { AiOutlineHome, AiOutlineFundProjectionScreen, AiOutlineUser } from "react-icons/ai";
import { CgFileDocument } from "react-icons/cg";
import { motion } from "framer-motion";

// Reusable NavItem Component
const NavItem: React.FC<{ path: string; label: string; icon: JSX.Element; isActive: boolean; onClick: () => void }> = ({
    path,
    label,
    icon,
    isActive,
    onClick,
}) => (
    <motion.div whileHover={{ scale: 1.1 }} whileTap={{ scale: 0.95 }} className="inline-block">
        <Nav.Item>
            <Nav.Link
                as={Link}
                to={path}
                onClick={onClick}
                className={`nav-link ${
                    isActive
                        ? "text-accent font-bold border-b-2 border-accent"
                        : "text-white"
                } transition duration-300 hover:text-accent`}
                aria-label={label}
            >
                <span className="inline-block mr-2">{icon}</span>
                {label}
            </Nav.Link>
        </Nav.Item>
    </motion.div>
);

function NavBar() {
    const [expanded, setExpanded] = useState(false);
    const [navColour, setNavColour] = useState(false);
    const location = useLocation();

    // Scroll Event Handler
    const handleScroll = () => setNavColour(window.scrollY >= 20);

    useEffect(() => {
        window.addEventListener("scroll", handleScroll);
        return () => window.removeEventListener("scroll", handleScroll);
    }, []);

    // Determine if the current route is active
    const isActive = (path: string) => location.pathname === path;

    // Navbar Items
    const navItems = [
        { path: "/", label: "Home", icon: <AiOutlineHome /> },
        { path: "/team", label: "Team", icon: <AiOutlineUser /> },
        { path: "/about", label: "About", icon: <AiOutlineUser /> },
        { path: "/explore", label: "Explore", icon: <AiOutlineFundProjectionScreen /> },
        { path: "/predict", label: "Predict", icon: <CgFileDocument /> },
    ];

    return (
        <Navbar
            expanded={expanded}
            fixed="top"
            expand="md"
            className={`transition-all duration-300 ${
                navColour ? "sticky bg-neutral shadow-md" : "bg-transparent"
            }`}
        >
            <Container>
                {/* Brand Name */}
                <motion.div
                    initial={{ opacity: 0, x: -50 }}
                    animate={{ opacity: 1, x: 0 }}
                    transition={{ duration: 0.5, ease: "easeOut" }}
                >
                    <Navbar.Brand
                        as={Link}
                        to="/"
                        className="d-flex align-items-center text-white text-lg font-bold hover:text-accent transition"
                        aria-label="Homepage"
                    >
                        🎥 Lights, Camera, Data!
                    </Navbar.Brand>
                </motion.div>

                {/* Hamburger Toggle */}
                <Navbar.Toggle
                    aria-controls="responsive-navbar-nav"
                    onClick={() => setExpanded((prev) => !prev)}
                    className="border-0"
                >
                    <span className="navbar-toggler-icon"></span>
                </Navbar.Toggle>

                {/* Nav Links */}
                <Navbar.Collapse id="responsive-navbar-nav">
                    <Nav className="ms-auto">
                        {navItems.map(({ path, label, icon }) => (
                            <NavItem
                                key={path}
                                path={path}
                                label={label}
                                icon={icon}
                                isActive={isActive(path)}
                                onClick={() => setExpanded(false)}
                            />
                        ))}
                    </Nav>
                </Navbar.Collapse>
            </Container>
        </Navbar>
    );
}

export default NavBar;
