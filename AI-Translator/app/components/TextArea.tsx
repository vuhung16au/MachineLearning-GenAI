import React from 'react';

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
  return (
    <div className="w-full h-full">
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