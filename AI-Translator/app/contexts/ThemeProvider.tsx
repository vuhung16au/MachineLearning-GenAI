"use client";

import { createContext, useContext, useEffect, useState } from "react";
import { setCookie, getCookie } from "cookies-next";

type Theme = "dark" | "light";

interface ThemeContextType {
  theme: Theme;
  toggleTheme: () => void;
}

const ThemeContext = createContext<ThemeContextType | undefined>(undefined);

export function ThemeProvider({ children }: { children: React.ReactNode }) {
  const [theme, setTheme] = useState<Theme>("dark"); // Set dark as default

  // Initialize theme from cookie or use default dark
  useEffect(() => {
    const savedTheme = getCookie("theme") as Theme | undefined;
    if (savedTheme) {
      setTheme(savedTheme);
    } else {
      // If no saved preference, set to dark mode as default
      setTheme("dark");
      setCookie("theme", "dark", { maxAge: 60 * 60 * 24 * 365 }); // 1 year expiry
    }
  }, []);

  // Apply theme class to HTML element and save to cookie when theme changes
  useEffect(() => {
    const root = document.documentElement;
    if (theme === "dark") {
      root.classList.add("dark");
    } else {
      root.classList.remove("dark");
    }
    
    // Save to cookie whenever theme changes
    setCookie("theme", theme, { maxAge: 60 * 60 * 24 * 365 });
  }, [theme]);

  // Toggle between light and dark themes
  const toggleTheme = () => {
    setTheme(prevTheme => prevTheme === "light" ? "dark" : "light");
  };

  return (
    <ThemeContext.Provider value={{ theme, toggleTheme }}>
      {children}
    </ThemeContext.Provider>
  );
}

// Custom hook to use the theme context
export function useTheme() {
  const context = useContext(ThemeContext);
  if (context === undefined) {
    throw new Error("useTheme must be used within a ThemeProvider");
  }
  return context;
}