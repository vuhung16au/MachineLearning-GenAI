import React, { useState } from 'react';

interface TextAreaProps {
  value: string;
  onChange: (value: string) => void;
  placeholder?: string;
  maxLength?: number;
  readOnly?: boolean;
  className?: string;
}

const TextArea: React.FC<TextAreaProps> = ({
  value,
  onChange,
  placeholder = '',
  maxLength,
  readOnly = false,
  className = ''
}) => {
  const [copied, setCopied] = useState(false);
  
  const handleCopy = async () => {
    try {
      await navigator.clipboard.writeText(value);
      setCopied(true);
      
      // Reset copied state after 2 seconds
      setTimeout(() => {
        setCopied(false);
      }, 2000);
    } catch (err) {
      console.error('Failed to copy text: ', err);
    }
  };

  return (
    <div className="w-full h-full">
      <div className="relative">
        <textarea
          className={`w-full min-h-[240px] p-4 rounded-lg resize-none
            transition-all duration-200 ease-in-out
            shadow-sm focus:shadow-md
            focus:outline-none focus:ring-2 focus:ring-opacity-50 focus:ring-indigo-500
            ${readOnly 
              ? 'bg-gray-50 dark:bg-gray-800 cursor-default' 
              : 'bg-white dark:bg-gray-700'} 
            border border-gray-200 dark:border-gray-600
            text-gray-900 dark:text-gray-100
            placeholder-gray-400 dark:placeholder-gray-500
            ${className}`}
          value={value}
          onChange={(e) => onChange(e.target.value)}
          placeholder={placeholder}
          maxLength={maxLength}
          readOnly={readOnly}
          style={{ fontFamily: 'inherit' }}
        />
        {value && (
          <button
            onClick={handleCopy}
            className={`absolute top-3 right-3 p-2 rounded-md 
                       transition-all duration-200
                       border shadow-sm hover:shadow-md
                       ${copied 
                         ? 'bg-green-500 text-white border-green-600 dark:bg-green-600 dark:border-green-700' 
                         : 'bg-white dark:bg-gray-700 hover:bg-gray-100 dark:hover:bg-gray-600 text-gray-600 dark:text-gray-300 border-gray-200 dark:border-gray-600'}`}
            title={copied ? "Copied!" : "Copy to clipboard"}
            aria-label={copied ? "Copied!" : "Copy to clipboard"}
          >
            {copied ? (
              <div className="flex items-center">
                <svg 
                  xmlns="http://www.w3.org/2000/svg" 
                  fill="none" 
                  viewBox="0 0 24 24" 
                  stroke="currentColor" 
                  className="h-5 w-5 mr-1"
                >
                  <path 
                    strokeLinecap="round" 
                    strokeLinejoin="round" 
                    strokeWidth={2} 
                    d="M5 13l4 4L19 7" 
                  />
                </svg>
                <span className="text-xs font-medium">Copied!</span>
              </div>
            ) : (
              <svg 
                xmlns="http://www.w3.org/2000/svg" 
                fill="none" 
                viewBox="0 0 24 24" 
                stroke="currentColor" 
                className="h-5 w-5"
              >
                <path 
                  strokeLinecap="round" 
                  strokeLinejoin="round" 
                  strokeWidth={2} 
                  d="M8 5H6a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2v-1M8 5a2 2 0 002 2h2a2 2 0 002-2M8 5a2 2 0 012-2h2a2 2 0 012 2m0 0h2a2 2 0 012 2v3m2 4H10m0 0l3-3m-3 3l3 3" 
                />
              </svg>
            )}
          </button>
        )}
      </div>
      {maxLength && (
        <div className="flex justify-end mt-2 text-sm text-gray-500 dark:text-gray-400 font-medium">
          <span className={value.length > maxLength * 0.9 ? 'text-amber-500 dark:text-amber-400' : ''}>
            {value.length}
          </span>
          <span>/</span>
          <span>{maxLength}</span>
        </div>
      )}
    </div>
  );
};

export default TextArea;