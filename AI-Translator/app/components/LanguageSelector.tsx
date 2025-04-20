import React, { useState, useRef, useEffect } from 'react';
import Cookies from 'js-cookie';

interface LanguageSelectorProps {
  languages: string[];
  value: string;
  onChange: (language: string) => void;
  label: string;
}

const LanguageSelector: React.FC<LanguageSelectorProps> = ({
  languages,
  value,
  onChange,
  label
}) => {
  const [isOpen, setIsOpen] = useState(false);
  const [searchTerm, setSearchTerm] = useState('');
  const dropdownRef = useRef<HTMLDivElement>(null);
  
  // Filter languages based on search term
  const filteredLanguages = languages.filter(language => 
    language.toLowerCase().includes(searchTerm.toLowerCase())
  );

  const handleChange = (language: string) => {
    onChange(language);
    setIsOpen(false);
    setSearchTerm('');
    
    // Save language preference to cookies
    if (label.includes('from')) {
      Cookies.set('sourceLanguage', language, { expires: 30 });
    } else if (label.includes('to')) {
      Cookies.set('targetLanguage', language, { expires: 30 });
    }
  };

  // Close dropdown when clicking outside
  useEffect(() => {
    const handleClickOutside = (event: MouseEvent) => {
      if (dropdownRef.current && !dropdownRef.current.contains(event.target as Node)) {
        setIsOpen(false);
      }
    };

    document.addEventListener('mousedown', handleClickOutside);
    return () => {
      document.removeEventListener('mousedown', handleClickOutside);
    };
  }, []);

  return (
    <div className="flex flex-col sm:flex-row sm:items-center space-y-2 sm:space-y-0 sm:space-x-3 relative" ref={dropdownRef}>
      <label className="text-sm font-medium text-gray-700 dark:text-gray-300 whitespace-nowrap">
        {label}
      </label>
      
      {/* Custom dropdown trigger */}
      <div className="relative w-full sm:w-64">
        <button
          type="button"
          className="w-full bg-white dark:bg-gray-800 border border-gray-300 dark:border-gray-700 text-gray-900 dark:text-gray-100 rounded-md px-3 py-2 text-left flex justify-between items-center focus:outline-none focus:ring-2 focus:ring-indigo-500"
          onClick={() => setIsOpen(!isOpen)}
        >
          <span>{value}</span>
          <svg xmlns="http://www.w3.org/2000/svg" className={`h-5 w-5 transition-transform duration-200 ${isOpen ? 'transform rotate-180' : ''}`} fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
          </svg>
        </button>

        {/* Dropdown panel */}
        {isOpen && (
          <div className="absolute z-10 mt-1 w-full max-h-60 overflow-auto bg-white dark:bg-gray-800 border border-gray-300 dark:border-gray-700 rounded-md shadow-lg">
            {/* Search input */}
            <div className="sticky top-0 p-2 bg-white dark:bg-gray-800 border-b border-gray-200 dark:border-gray-700">
              <input 
                type="text"
                className="w-full p-2 border border-gray-300 dark:border-gray-700 dark:bg-gray-700 dark:text-white rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500"
                placeholder="Search language..."
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
                onClick={(e) => e.stopPropagation()}
                autoFocus
              />
            </div>

            {/* Language options */}
            <div className="py-1">
              {filteredLanguages.length > 0 ? (
                filteredLanguages.map((language) => (
                  <button
                    key={language}
                    className={`w-full text-left px-4 py-2 hover:bg-indigo-100 dark:hover:bg-indigo-900/30 ${language === value ? 'bg-indigo-50 dark:bg-indigo-900/20 text-indigo-700 dark:text-indigo-300' : 'text-gray-900 dark:text-gray-100'}`}
                    onClick={() => handleChange(language)}
                  >
                    {language}
                  </button>
                ))
              ) : (
                <div className="px-4 py-2 text-gray-500 dark:text-gray-400">No languages found</div>
              )}
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default LanguageSelector;