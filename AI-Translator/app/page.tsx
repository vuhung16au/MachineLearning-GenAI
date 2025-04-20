'use client';

import React, { useState, useEffect } from 'react';
import Cookies from 'js-cookie';
import LanguageSelector from './components/LanguageSelector';
import TextArea from './components/TextArea';
import Button from './components/Button';
import HistoryList from './components/HistoryList';
import SavedList from './components/SavedList';

export default function TranslatorPage() {
  // States for source and target languages, texts
  const [sourceLanguage, setSourceLanguage] = useState('English');
  const [targetLanguage, setTargetLanguage] = useState('Vietnamese');
  const [sourceText, setSourceText] = useState('');
  const [translation, setTranslation] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState('');
  const [theme, setTheme] = useState('light');

  // States for history and saved translations
  const [history, setHistory] = useState([]);
  const [savedTranslations, setSavedTranslations] = useState([]);
  const [showHistory, setShowHistory] = useState(false);
  const [showSaved, setShowSaved] = useState(false);

  // List of supported languages
  const languages = [
    'English', 'Japanese', 'Korean', 'Arabic', 'Bahasa Indonesia', 'Bengali', 'Bulgarian',
    'Chinese (Simplified)', 'Chinese (Traditional)', 'Croatian', 'Czech', 'Danish', 'Dutch',
    'Estonian', 'Farsi', 'Finnish', 'French', 'German', 'Gujarati', 'Greek', 'Hebrew', 'Hindi',
    'Hungarian', 'Italian', 'Kannada', 'Latvian', 'Lithuanian', 'Malayalam', 'Marathi', 'Norwegian',
    'Polish', 'Portuguese', 'Romanian', 'Russian', 'Serbian', 'Slovak', 'Slovenian', 'Spanish',
    'Swahili', 'Swedish', 'Tamil', 'Telugu', 'Thai', 'Turkish', 'Ukrainian', 'Urdu', 'Vietnamese'
  ];

  // Load history, saved translations, and theme preference on mount
  useEffect(() => {
    // Load translation history
    const savedHistory = Cookies.get('translationHistory');
    if (savedHistory) {
      try {
        setHistory(JSON.parse(savedHistory));
      } catch (e) {
        console.error('Failed to parse translation history:', e);
      }
    }

    // Load saved translations
    const savedTranslationsCookie = Cookies.get('savedTranslations');
    if (savedTranslationsCookie) {
      try {
        setSavedTranslations(JSON.parse(savedTranslationsCookie));
      } catch (e) {
        console.error('Failed to parse saved translations:', e);
      }
    }

    // Load language preferences
    const savedSourceLanguage = Cookies.get('sourceLanguage');
    if (savedSourceLanguage) {
      setSourceLanguage(savedSourceLanguage);
    }

    const savedTargetLanguage = Cookies.get('targetLanguage');
    if (savedTargetLanguage) {
      setTargetLanguage(savedTargetLanguage);
    }

    // Load theme preference
    const savedTheme = localStorage.getItem('theme') || 'dark';
    setTheme(savedTheme);
    document.documentElement.classList.toggle('dark', savedTheme === 'dark');
  }, []);

  // Update theme in localStorage and apply class when theme changes
  useEffect(() => {
    localStorage.setItem('theme', theme);
    document.documentElement.classList.toggle('dark', theme === 'dark');
  }, [theme]);

  // Handle translation
  const handleTranslate = async () => {
    if (!sourceText.trim()) return;
    
    setIsLoading(true);
    setError('');

    try {
      const response = await fetch('/api/translate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ sourceText, sourceLanguage, targetLanguage }),
      });

      const data = await response.json();
      
      if (!response.ok) {
        throw new Error(data.error || 'Translation failed');
      }

      // Update to use data.translatedText instead of data.translation
      if (data.translatedText) {
        setTranslation(data.translatedText);
        
        // Add to history
        const newHistoryItem = {
          sourceText,
          sourceLanguage,
          targetLanguage,
          translation: data.translatedText,
          timestamp: new Date().toISOString(),
        };
        
        const newHistory = [newHistoryItem, ...history].slice(0, 10);
        setHistory(newHistory);
        Cookies.set('translationHistory', JSON.stringify(newHistory), { expires: 7 });
      }
    } catch (err) {
      console.error('Translation error:', err);
      setError(err.message || 'Failed to translate. Please try again.');
    } finally {
      setIsLoading(false);
    }
  };

  // Handle reset (clear both text areas)
  const handleReset = () => {
    setSourceText('');
    setTranslation('');
    setError('');
  };

  // Handle language swap
  const handleSwap = () => {
    setSourceLanguage(targetLanguage);
    setTargetLanguage(sourceLanguage);
    setSourceText(translation);
    setTranslation(sourceText);
  };

  // Handle saving a translation
  const handleSave = () => {
    if (!translation) return;
    
    const newSavedItem = {
      sourceText,
      sourceLanguage,
      targetLanguage,
      translation,
      timestamp: new Date().toISOString(),
    };
    
    const newSaved = [newSavedItem, ...savedTranslations].slice(0, 10);
    setSavedTranslations(newSaved);
    Cookies.set('savedTranslations', JSON.stringify(newSaved), { expires: 7 });
  };

  // Load a history or saved item
  const handleLoadItem = (item) => {
    setSourceLanguage(item.sourceLanguage);
    setTargetLanguage(item.targetLanguage);
    setSourceText(item.sourceText);
    setTranslation(item.translation);
  };

  // Toggle theme
  const toggleTheme = () => {
    setTheme(theme === 'light' ? 'dark' : 'light');
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-50 to-gray-100 dark:from-gray-900 dark:to-gray-800 transition-colors duration-300">
      <div className="container mx-auto px-4 py-8 max-w-6xl">
        <header className="flex justify-between items-center mb-10 bg-white dark:bg-gray-800 p-4 rounded-xl shadow-md">
          <h1 className="text-3xl font-bold bg-gradient-to-r from-indigo-600 to-purple-600 dark:from-indigo-400 dark:to-purple-400 bg-clip-text text-transparent">
            AI Translator
          </h1>
          <Button 
            onClick={toggleTheme} 
            variant="outline"
            className="transition-all duration-300 hover:scale-105"
          >
            {theme === 'light' ? '🌙 Dark Mode' : '☀️ Light Mode'}
          </Button>
        </header>

        <main className="bg-white dark:bg-gray-800 rounded-2xl shadow-lg p-6 mb-10 transition-all duration-300">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-8 mb-8">
            <div className="transition-all duration-300 hover:shadow-md rounded-xl p-4">
              <div className="flex justify-between items-center mb-3">
                <LanguageSelector 
                  languages={languages}
                  value={sourceLanguage}
                  onChange={setSourceLanguage}
                  label="Translate from"
                />
              </div>
              <TextArea
                value={sourceText}
                onChange={setSourceText}
                placeholder="Enter text to translate (max 5000 characters)"
                maxLength={5000}
                className="border-2 border-indigo-100 focus:border-indigo-300 dark:border-gray-700 dark:focus:border-indigo-600 rounded-lg transition-all duration-200"
              />
            </div>
            
            <div className="transition-all duration-300 hover:shadow-md rounded-xl p-4">
              <div className="flex justify-between items-center mb-3">
                <LanguageSelector 
                  languages={languages}
                  value={targetLanguage}
                  onChange={setTargetLanguage}
                  label="Translate to"
                />
              </div>
              <TextArea
                value={translation}
                onChange={setTranslation}
                placeholder="Translation will appear here"
                readOnly
                className="border-2 border-indigo-100 focus:border-indigo-300 dark:border-gray-700 dark:focus:border-indigo-600 rounded-lg transition-all duration-200 bg-gray-50 dark:bg-gray-900"
              />
            </div>
          </div>

          {error && (
            <div className="bg-red-100 dark:bg-red-900/50 border border-red-400 text-red-700 dark:text-red-200 px-5 py-4 rounded-lg mb-6 animate-pulse">
              {error}
            </div>
          )}

          <div className="flex flex-wrap justify-center gap-4 mb-10">
            <Button 
              onClick={handleTranslate} 
              disabled={isLoading || !sourceText.trim()}
              className="bg-gradient-to-r from-indigo-600 to-purple-600 hover:from-indigo-700 hover:to-purple-700 text-white py-3 px-6 rounded-lg transition-all duration-300 transform hover:scale-105 disabled:opacity-50 disabled:hover:scale-100 shadow-md"
            >
              {isLoading ? (
                <span className="flex items-center">
                  <svg className="animate-spin -ml-1 mr-2 h-4 w-4 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                    <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                    <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                  </svg>
                  Translating...
                </span>
              ) : 'Translate'}
            </Button>
            <Button 
              onClick={handleSwap} 
              variant="secondary" 
              disabled={isLoading || !translation}
              className="py-3 px-6 rounded-lg transition-all duration-300 hover:scale-105 disabled:opacity-50 disabled:hover:scale-100 shadow-md"
            >
              <span className="flex items-center">
                <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M8 7h12m0 0l-4-4m4 4l-4 4m0 6H4m0 0l4 4m-4-4l4-4" />
                </svg>
                Swap Languages
              </span>
            </Button>
            <Button 
              onClick={handleReset} 
              variant="secondary" 
              disabled={isLoading || (!sourceText && !translation)}
              className="py-3 px-6 rounded-lg transition-all duration-300 hover:scale-105 disabled:opacity-50 disabled:hover:scale-100 shadow-md"
            >
              Reset
            </Button>
            <Button 
              onClick={handleSave} 
              variant="secondary" 
              disabled={isLoading || !translation}
              className="py-3 px-6 rounded-lg transition-all duration-300 hover:scale-105 disabled:opacity-50 disabled:hover:scale-100 shadow-md"
            >
              <span className="flex items-center">
                <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M8 7H5a2 2 0 00-2 2v9a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2h-3m-1 4l-3 3m0 0l-3-3m3 3V4" />
                </svg>
                Save Translation
              </span>
            </Button>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
            <div className="bg-gray-50 dark:bg-gray-900 rounded-xl p-5 shadow-md transition-all duration-300">
              <Button 
                onClick={() => setShowHistory(!showHistory)} 
                variant="outline" 
                className="w-full mb-4 py-3 border-2 border-indigo-200 dark:border-indigo-800 hover:bg-indigo-50 dark:hover:bg-indigo-900/30 rounded-lg transition-all duration-200"
              >
                <span className="flex items-center justify-center">
                  <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
                  </svg>
                  {showHistory ? 'Hide History' : 'Show History'} ({history.length}/10)
                </span>
              </Button>
              
              {showHistory && (
                <div className="overflow-hidden transition-all duration-500 max-h-[500px] overflow-y-auto">
                  <HistoryList 
                    history={history}
                    onSelect={handleLoadItem}
                  />
                </div>
              )}
            </div>
            
            <div className="bg-gray-50 dark:bg-gray-900 rounded-xl p-5 shadow-md transition-all duration-300">
              <Button 
                onClick={() => setShowSaved(!showSaved)} 
                variant="outline" 
                className="w-full mb-4 py-3 border-2 border-indigo-200 dark:border-indigo-800 hover:bg-indigo-50 dark:hover:bg-indigo-900/30 rounded-lg transition-all duration-200"
              >
                <span className="flex items-center justify-center">
                  <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 5a2 2 0 012-2h10a2 2 0 012 2v16l-7-3.5L5 21V5z" />
                  </svg>
                  {showSaved ? 'Hide Saved' : 'Show Saved'} ({savedTranslations.length}/10)
                </span>
              </Button>
              
              {showSaved && (
                <div className="overflow-hidden transition-all duration-500 max-h-[500px] overflow-y-auto">
                  <SavedList 
                    savedTranslations={savedTranslations}
                    onSelect={handleLoadItem}
                    onRemove={(index) => {
                      const newSaved = [...savedTranslations];
                      newSaved.splice(index, 1);
                      setSavedTranslations(newSaved);
                      Cookies.set('savedTranslations', JSON.stringify(newSaved), { expires: 7 });
                    }}
                  />
                </div>
              )}
            </div>
          </div>
        </main>

        <footer className="mt-12 text-center text-gray-500 dark:text-gray-400 bg-white dark:bg-gray-800 p-6 rounded-xl shadow-md">
          <p className="text-lg font-medium">© {new Date().getFullYear()} AI Translator</p>
          <p className="text-sm mt-2 flex items-center justify-center">
            <span className="bg-gradient-to-r from-indigo-600 to-purple-600 bg-clip-text text-transparent font-medium">Powered by Google Gemini API</span>
            <svg className="ml-2 h-5 w-5 text-indigo-500" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 10V3L4 14h7v7l9-11h-7z" />
            </svg>
          </p>
          <div className="mt-4 p-3 bg-gray-100 dark:bg-gray-700 rounded-lg text-xs text-gray-600 dark:text-gray-300">
            <p><strong>Disclaimer:</strong> This application does not store any of your data. Translations are processed in real-time and are not saved on our servers. However, please exercise caution when translating sensitive information, as this application utilizes the Google Gemini API and is therefore subject to Google's terms of service.</p>
          </div>
          <div className="mt-4 flex justify-center space-x-4">
            <a href="https://ai-translator-self.vercel.app/" target="_blank" rel="noopener noreferrer" className="text-indigo-500 hover:text-indigo-700 dark:text-indigo-400 dark:hover:text-indigo-300 transition-colors">
              Live Demo
            </a>
            <a href="https://github.com/vuhung16au/MachineLearning-GenAI/tree/main/AI-Translator" target="_blank" rel="noopener noreferrer" className="text-indigo-500 hover:text-indigo-700 dark:text-indigo-400 dark:hover:text-indigo-300 transition-colors">
              GitHub Repository
            </a>
          </div>
        </footer>
      </div>
    </div>
  );
}