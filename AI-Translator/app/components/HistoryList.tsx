import React from 'react';

interface HistoryItem {
  sourceText: string;
  sourceLanguage: string;
  targetLanguage: string;
  translation: string;
  timestamp: string;
}

interface HistoryListProps {
  history: HistoryItem[];
  onSelect: (item: HistoryItem) => void;
}

const HistoryList: React.FC<HistoryListProps> = ({ history, onSelect }) => {
  if (history.length === 0) {
    return (
      <div className="p-4 bg-gray-100 dark:bg-gray-800 rounded-md text-center text-gray-500 dark:text-gray-400">
        No translation history yet
      </div>
    );
  }

  // Format the timestamp to a readable format
  const formatTimestamp = (timestamp: string) => {
    const date = new Date(timestamp);
    return date.toLocaleString();
  };

  // Truncate text for display
  const truncateText = (text: string, maxLength: number = 50) => {
    return text.length > maxLength 
      ? `${text.substring(0, maxLength)}...` 
      : text;
  };

  return (
    <div className="bg-white dark:bg-gray-800 border border-gray-200 dark:border-gray-700 rounded-md overflow-hidden">
      <ul className="divide-y divide-gray-200 dark:divide-gray-700">
        {history.map((item, index) => (
          <li 
            key={index}
            className="p-4 hover:bg-gray-50 dark:hover:bg-gray-700 cursor-pointer transition-colors"
            onClick={() => onSelect(item)}
          >
            <div className="flex flex-col gap-1">
              <div className="flex justify-between">
                <span className="text-sm font-medium text-indigo-600 dark:text-indigo-400">
                  {item.sourceLanguage} → {item.targetLanguage}
                </span>
                <span className="text-xs text-gray-500 dark:text-gray-400">
                  {formatTimestamp(item.timestamp)}
                </span>
              </div>
              <p className="text-sm text-gray-800 dark:text-gray-200">
                {truncateText(item.sourceText)}
              </p>
              <p className="text-sm text-gray-600 dark:text-gray-300">
                {truncateText(item.translation)}
              </p>
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default HistoryList;