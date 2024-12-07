import React from "react";
import NavBar from "./NavBar";
import Footer from "./Footer";

interface PageWrapperProps {
    children: React.ReactNode;
    title?: string; // Optional title for the page
}

const PageWrapper: React.FC<PageWrapperProps> = ({ children, title }) => {
    return (
        <div className="flex flex-col min-h-screen bg-gradient-to-br from-gray-900 via-black to-gray-800 text-white">
            {/* Header/Navbar */}
            <NavBar />

            {/* Page Content */}
            <main className="flex-grow pt-20 px-4 sm:px-8 lg:px-16">
                {/* Optional Page Title */}
                {title && (
                    <h1 className="text-3xl md:text-4xl font-bold text-center mb-8">
                        {title}
                    </h1>
                )}
                {children}
            </main>

            {/* Footer */}
            <Footer />
        </div>
    );
};

export default PageWrapper;
