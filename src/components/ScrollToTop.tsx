import { useEffect } from "react";
import { useLocation } from "react-router-dom";

/**
 * ScrollToTop Component
 * Ensures the page scrolls to the top whenever the route changes.
 */
const ScrollToTop: React.FC = () => {
    const { pathname } = useLocation();

    useEffect(() => {
        // Scroll to the top of the page on route change
        window.scrollTo({
            top: 0,
            left: 0,
            behavior: "smooth", // Smooth scrolling for better UX
        });
    }, [pathname]); // Dependency ensures this runs only on route changes

    return null; // Component renders nothing visually
};

export default ScrollToTop;
