import React from 'react';
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
  const handleChange = (language: string) => {
    onChange(language);
    
    // Save language preference to cookies
    if (label.includes('from')) {
      Cookies.set('sourceLanguage', language, { expires: 30 });
    } else if (label.includes('to')) {
      Cookies.set('targetLanguage', language, { expires: 30 });
    }
  };

  return (
    <div className="flex flex-col">
      <label className="mb-1 text-sm font-medium text-gray-700 dark:text-gray-300">
        {label}
      </label>
      <select
        className="bg-white dark:bg-gray-800 border border-gray-300 dark:border-gray-700 text-gray-900 dark:text-gray-100 rounded-md px-3 py-2 focus:outline-none focus:ring-2 focus:ring-indigo-500"
        value={value}
        onChange={(e) => handleChange(e.target.value)}
      >
        {languages.map((language) => (
          <option key={language} value={language}>
            {language}
          </option>
        ))}
      </select>
    </div>
  );
};

export default LanguageSelector;