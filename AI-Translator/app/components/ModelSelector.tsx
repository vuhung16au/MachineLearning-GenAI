import React from 'react';

interface ModelSelectorProps {
  models: { id: string; name: string }[];
  value: string;
  onChange: (value: string) => void;
  label: string;
}

const ModelSelector: React.FC<ModelSelectorProps> = ({ models, value, onChange, label }) => {
  return (
    <div className="flex flex-col">
      <label className="mb-2 text-sm font-medium text-gray-700 dark:text-gray-300">
        {label}
      </label>
      <select
        value={value}
        onChange={(e) => onChange(e.target.value)}
        className="bg-gray-50 dark:bg-gray-900 border border-gray-300 dark:border-gray-700 text-gray-900 dark:text-gray-100 text-sm rounded-lg focus:ring-indigo-500 focus:border-indigo-500 block w-full p-2.5 transition-colors duration-200"
      >
        {models.map((model) => (
          <option key={model.id} value={model.id}>
            {model.name}
          </option>
        ))}
      </select>
    </div>
  );
};

export default ModelSelector;