// Password Generator Script

document.addEventListener('DOMContentLoaded', function() {
  // DOM elements for basic features
  const passwordLengthSelect = document.getElementById('passwordLength');
  const includeNumbersCheck = document.getElementById('includeNumbers');
  const includeLowercaseCheck = document.getElementById('includeLowercase');
  const includeUppercaseCheck = document.getElementById('includeUppercase');
  const beginWithLetterCheck = document.getElementById('beginWithLetter');
  const includeSymbolsCheck = document.getElementById('includeSymbols');
  const symbolsListInput = document.getElementById('symbolsList');
  const noSimilarCharsCheck = document.getElementById('noSimilarChars');
  const noDuplicateCharsCheck = document.getElementById('noDuplicateChars');
  const noSequentialCharsCheck = document.getElementById('noSequentialChars');
  const autoGenerateCheck = document.getElementById('autoGenerate');
  // Removed quantity select since it's not in the HTML anymore
  const savePreferenceCheck = document.getElementById('savePreference');
  
  // Theme toggle elements
  const themeToggle = document.getElementById('themeToggle');
  
  // Default number of passwords to generate
  const DEFAULT_QUANTITY = 5;
  
  // Default theme is dark mode
  const DEFAULT_THEME = 'dark';
  
  const generateBtn = document.getElementById('generate');
  const copy1stBtn = document.getElementById('copy1st');
  const copyAllBtn = document.getElementById('copyAll');
  const passwordsOutput = document.getElementById('passwordsOutput');
  
  // Character sets
  const numbers = '0123456789';
  const lowercase = 'abcdefghijklmnopqrstuvwxyz';
  const uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
  
  // Similar characters to avoid if selected
  const similarChars = 'iIl1Lo0O';
  
  // Load saved preferences if they exist
  loadPreferences();
  
  // Load theme preference
  loadThemePreference();
  
  // Auto-generate on page load if selected
  if (autoGenerateCheck.checked) {
    generatePasswords();
  }
  
  // Event listeners
  generateBtn.addEventListener('click', () => generatePasswords());
  copy1stBtn.addEventListener('click', copyFirstPassword);
  copyAllBtn.addEventListener('click', copyAllPasswords);
  savePreferenceCheck.addEventListener('change', savePreferences);
  themeToggle.addEventListener('change', toggleTheme);
  
  // Toggle theme function
  function toggleTheme() {
    if (themeToggle.checked) {
      document.documentElement.classList.add('dark-mode');
      localStorage.setItem('theme', 'dark');
    } else {
      document.documentElement.classList.remove('dark-mode');
      localStorage.setItem('theme', 'light');
    }
  }
  
  // Load theme preference from localStorage
  function loadThemePreference() {
    const theme = localStorage.getItem('theme') || DEFAULT_THEME;
    if (theme === 'dark') {
      document.documentElement.classList.add('dark-mode');
      themeToggle.checked = true;
    } else {
      document.documentElement.classList.remove('dark-mode');
      themeToggle.checked = false;
    }
  }
  
  // Generate passwords based on selected options
  function generatePasswords() {
    const passwordLength = parseInt(passwordLengthSelect.value);
    // Use default quantity instead of reading from select element
    const quantity = DEFAULT_QUANTITY;
    const passwords = [];
    
    for (let i = 0; i < quantity; i++) {
      passwords.push(generatePassword(passwordLength));
    }
    
    displayPasswords(passwords);
    
    if (savePreferenceCheck.checked) {
      savePreferences();
    }
  }
  
  // Advanced password generation algorithm
  function generatePassword(length) {
    let chars = '';
    let password = '';
    
    // Build character set based on selections
    if (includeNumbersCheck.checked) chars += numbers;
    if (includeLowercaseCheck.checked) chars += lowercase;
    if (includeUppercaseCheck.checked) chars += uppercase;
    if (includeSymbolsCheck.checked) chars += symbolsListInput.value;
    
    // Remove similar characters if option is selected
    if (noSimilarCharsCheck.checked) {
      for (let i = 0; i < similarChars.length; i++) {
        chars = chars.replace(similarChars[i], '');
      }
    }
    
    // Ensure we have some characters to work with
    if (chars.length === 0) {
      return 'Error: No character sets selected';
    }
    
    // Begin with a letter if option is selected
    if (beginWithLetterCheck.checked) {
      let letterChars = '';
      if (includeLowercaseCheck.checked) letterChars += lowercase;
      if (includeUppercaseCheck.checked) letterChars += uppercase;
      
      if (letterChars.length > 0) {
        password += letterChars.charAt(Math.floor(Math.random() * letterChars.length));
      } else {
        // If no letter option is selected, just use the first character from chars
        password += chars.charAt(Math.floor(Math.random() * chars.length));
      }
      
      length--;
    }
    
    // Array to track used characters for the "no duplicates" option
    const usedChars = password.split('');
    
    // Get previous character to check for sequential characters
    let prevChar = password.length > 0 ? password.charAt(password.length - 1) : '';
    
    // Generate the rest of the password
    while (password.length < length) {
      // Create a temporary character set for this iteration
      let tempChars = chars;
      
      if (noDuplicateCharsCheck.checked) {
        // Remove already used characters
        for (let i = 0; i < usedChars.length; i++) {
          tempChars = tempChars.replace(usedChars[i], '');
        }
        
        if (tempChars.length === 0) {
          // If we've used all available characters, break out
          break;
        }
      }
      
      if (noSequentialCharsCheck.checked && prevChar) {
        // Get ASCII values to check for sequences
        const prevCharCode = prevChar.charCodeAt(0);
        tempChars = tempChars.split('')
          .filter(char => {
            const charCode = char.charCodeAt(0);
            return Math.abs(charCode - prevCharCode) !== 1;
          })
          .join('');
      }
      
      // If we have no characters left to use, break out
      if (tempChars.length === 0) {
        break;
      }
      
      // Get the next character
      const nextChar = tempChars.charAt(Math.floor(Math.random() * tempChars.length));
      
      password += nextChar;
      usedChars.push(nextChar);
      prevChar = nextChar;
    }
    
    return password;
  }
  
  // Display generated passwords
  function displayPasswords(passwords) {
    passwordsOutput.innerHTML = '';
    
    passwords.forEach((password, index) => {
      const passwordLine = document.createElement('div');
      passwordLine.className = 'password-line';
      
      const lineNumber = document.createElement('div');
      lineNumber.className = 'line-number';
      lineNumber.textContent = index + 1;
      
      const passwordText = document.createElement('div');
      passwordText.className = 'password-text';
      passwordText.textContent = password;
      
      passwordLine.appendChild(lineNumber);
      passwordLine.appendChild(passwordText);
      passwordsOutput.appendChild(passwordLine);
    });
  }
  
  // Copy the first password to clipboard
  function copyFirstPassword() {
    const passwordElements = document.querySelectorAll('.password-text');
    if (passwordElements.length > 0) {
      navigator.clipboard.writeText(passwordElements[0].textContent)
        .catch(err => {
          console.error('Failed to copy password:', err);
        });
    }
  }
  
  // Copy all passwords to clipboard
  function copyAllPasswords() {
    const passwordElements = document.querySelectorAll('.password-text');
    if (passwordElements.length > 0) {
      const allPasswords = Array.from(passwordElements)
        .map(el => el.textContent)
        .join('\n');
      
      navigator.clipboard.writeText(allPasswords)
        .catch(err => {
          console.error('Failed to copy passwords:', err);
        });
    }
  }
  
  // Save user preferences to cookies
  function savePreferences() {
    if (savePreferenceCheck.checked) {
      const preferences = {
        passwordLength: passwordLengthSelect.value,
        includeNumbers: includeNumbersCheck.checked,
        includeLowercase: includeLowercaseCheck.checked,
        includeUppercase: includeUppercaseCheck.checked,
        beginWithLetter: beginWithLetterCheck.checked,
        includeSymbols: includeSymbolsCheck.checked,
        symbolsList: symbolsListInput.value,
        noSimilarChars: noSimilarCharsCheck.checked,
        noDuplicateChars: noDuplicateCharsCheck.checked,
        noSequentialChars: noSequentialCharsCheck.checked,
        autoGenerate: autoGenerateCheck.checked,
        // Remove quantity from preferences
      };
      
      document.cookie = `pwdGenPrefs=${encodeURIComponent(JSON.stringify(preferences))}; expires=${new Date(Date.now() + 30 * 24 * 60 * 60 * 1000).toUTCString()}; path=/PasswordGenerator; SameSite=Strict; Secure`;
    }
  }
  
  // Load saved preferences from cookies
  function loadPreferences() {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.startsWith('pwdGenPrefs=')) {
        try {
          const preferences = JSON.parse(decodeURIComponent(cookie.substring('pwdGenPrefs='.length)));
          
          passwordLengthSelect.value = preferences.passwordLength || 16;
          includeNumbersCheck.checked = preferences.includeNumbers !== false;
          includeLowercaseCheck.checked = preferences.includeLowercase !== false;
          includeUppercaseCheck.checked = preferences.includeUppercase !== false;
          beginWithLetterCheck.checked = preferences.beginWithLetter !== false;
          includeSymbolsCheck.checked = preferences.includeSymbols !== false;
          symbolsListInput.value = preferences.symbolsList || symbolsListInput.value;
          noSimilarCharsCheck.checked = preferences.noSimilarChars !== false;
          noDuplicateCharsCheck.checked = preferences.noDuplicateChars !== false;
          noSequentialCharsCheck.checked = preferences.noSequentialChars !== false;
          autoGenerateCheck.checked = preferences.autoGenerate !== false;
          // Remove quantity from preferences loading
          savePreferenceCheck.checked = true;
        } catch (e) {
          console.error('Error loading preferences:', e);
        }
        break;
      }
    }
  }
});