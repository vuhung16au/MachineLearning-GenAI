import React from 'react';

interface ButtonProps {
  children: React.ReactNode;
  onClick?: () => void;
  disabled?: boolean;
  variant?: 'primary' | 'secondary' | 'outline';
  className?: string;
  type?: 'button' | 'submit' | 'reset';
}

const Button: React.FC<ButtonProps> = ({
  children,
  onClick,
  disabled = false,
  variant = 'primary',
  className = '',
  type = 'button'
}) => {
  const baseStyles = 'px-4 py-2 rounded-md font-medium focus:outline-none focus:ring-2 focus:ring-opacity-50 transition-all duration-200 shadow-sm hover-lift';
  
  const variantStyles = {
    primary: 'bg-gradient-to-r from-indigo-600 to-indigo-700 hover:from-indigo-700 hover:to-indigo-800 text-white focus:ring-indigo-400 disabled:opacity-60 disabled:cursor-not-allowed disabled:hover:transform-none shadow-indigo-200 dark:shadow-indigo-900/20',
    
    secondary: 'bg-white dark:bg-gray-800 text-gray-700 dark:text-gray-200 hover:bg-gray-50 dark:hover:bg-gray-700 border border-gray-300 dark:border-gray-600 focus:ring-gray-400 disabled:opacity-60 disabled:cursor-not-allowed disabled:hover:transform-none shadow-gray-200 dark:shadow-gray-900/10',
    
    outline: 'bg-transparent hover:bg-gray-50 dark:hover:bg-gray-800 text-indigo-600 dark:text-indigo-400 border border-indigo-400 dark:border-indigo-500 focus:ring-indigo-300 disabled:opacity-60 disabled:cursor-not-allowed disabled:hover:transform-none'
  };

  return (
    <button
      type={type}
      className={`${baseStyles} ${variantStyles[variant]} ${className}`}
      onClick={onClick}
      disabled={disabled}
    >
      {children}
    </button>
  );
};

export default Button;