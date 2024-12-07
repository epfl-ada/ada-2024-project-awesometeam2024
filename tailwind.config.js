const plugin = require("tailwindcss/plugin");

module.exports = {
  // File paths where Tailwind will be used
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
    "./public/index.html",
  ],
  theme: {
    extend: {
      // 1. Colors
      colors: {
        primary: "#00bcd4", // Cyan
        secondary: "#ff5722", // Orange
        accent: "#4caf50", // Green
        neutral: "#2d3748", // Grayish blue
        dark: "#1a202c", // Background dark
        light: "#f7fafc", // Light background
        info: "#3182ce", // Info blue
        danger: "#e53e3e", // Error red
      },

      // 2. Typography
      fontFamily: {
        sans: ["Poppins", "sans-serif"], // Global font
        serif: ["Merriweather", "serif"], // Optional serif font
        mono: ["Fira Code", "monospace"], // For code snippets
      },

      // 3. Spacing
      spacing: {
        72: "18rem",
        84: "21rem",
        96: "24rem",
        128: "32rem", // New extended spacing
      },

      // 4. Box Shadows
      boxShadow: {
        glow: "0 4px 15px rgba(0, 188, 212, 0.4)", // Glow effect
        strong: "0 10px 20px rgba(0, 0, 0, 0.25)", // Strong shadow for cards
        subtle: "0 2px 4px rgba(0, 0, 0, 0.1)", // Light shadow
      },

      // 5. Gradients
      backgroundImage: {
        "hero-gradient":
          "linear-gradient(to right, #1a202c, #2d3748, #4a5568)", // Hero section
        "card-gradient":
          "linear-gradient(to bottom, rgba(0, 188, 212, 0.8), rgba(0, 188, 212, 0))",
        "glossy-gradient":
          "linear-gradient(135deg, #e3f2fd, #90caf9, #42a5f5)", // Glossy gradient
      },

      // 6. Animations
      animation: {
        fadeIn: "fadeIn 1s ease-in-out",
        slideUp: "slideUp 0.8s ease-out",
        pulseGlow: "pulseGlow 2s infinite",
        rotateSlow: "rotateSlow 3s linear infinite",
      },

      // 7. Keyframes
      keyframes: {
        fadeIn: {
          from: { opacity: 0 },
          to: { opacity: 1 },
        },
        slideUp: {
          from: { transform: "translateY(20px)", opacity: 0 },
          to: { transform: "translateY(0)", opacity: 1 },
        },
        pulseGlow: {
          "0%, 100%": { boxShadow: "0 0 15px rgba(0, 188, 212, 0.4)" },
          "50%": { boxShadow: "0 0 25px rgba(0, 188, 212, 0.6)" },
        },
        rotateSlow: {
          from: { transform: "rotate(0deg)" },
          to: { transform: "rotate(360deg)" },
        },
      },

      // 8. Breakpoints
      screens: {
        xs: "480px", // Extra small screens
        sm: "640px",
        md: "768px",
        lg: "1024px",
        xl: "1280px",
        "2xl": "1536px",
      },
    },
  },
  plugins: [
    require("@tailwindcss/typography"), // Advanced text utilities
    require("@tailwindcss/forms"), // Better form styling
    require("@tailwindcss/aspect-ratio"), // Aspect ratio utilities
    require("@tailwindcss/line-clamp"), // Line clamping for truncating text
    plugin(function ({ addUtilities }) {
      // Custom utility for hover glow effects
      addUtilities({
        ".hover-glow": {
          transition: "all 0.3s ease-in-out",
          boxShadow: "0 0 15px rgba(0, 188, 212, 0.4)",
        },
        ".hover-glow:hover": {
          boxShadow: "0 0 25px rgba(0, 188, 212, 0.6)",
        },
      });

      // Custom utility for text shadow
      addUtilities({
        ".text-glow": {
          textShadow: "0 2px 8px rgba(255, 255, 255, 0.5)",
        },
      });
    }),
  ],
};
