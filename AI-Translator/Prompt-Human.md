
# Human Prompt 

Help me write a prompt to create a text-to-text translation app using Gemini API.
the app will use Next.js as backend.
make sure to secure the GEMINI API key - not visible to end-users 

# Overview: 
translation app using Gemini API.
The app will use Next.js as backend.

# Technologies:
- Gemini API for translation
- Next.js for backend
- Frontend: Please suggest a modern technology

# The UI

- Left hand side
 + text area: Translation source - the text to be translated. Maximum character can be input: 5000
 + dropdown box: Source language 
- Right hand side 
 + text area: Translated text 
 + dropbox box: Target language 
- Reset: Deleted Translation source and translated text 
- A button to swap betwwen Translation language and translated language (e.g: English <-> Vietnamese)
- A big button "Translate"
- History: Save most recent 10 Translation users have input. Users can load translation from their history (saved to cookies)
- Save: Users can save and view the saved up to 10 translations at maximum (saved to cookies)

## CSS/Style:

- Simple
- Easy to use 
- Colors: light-dark theme 

# Supported languages 
(ref https://gemini.google.com/faq?hl=en-AU)

English, Japanese, Korean, Arabic, Bahasa Indonesia, Bengali, Bulgarian, Chinese (Simplified/Traditional), Croatian, Czech, Danish, Dutch, Estonian, Farsi, Finnish, French, German, Gujarati, Greek, Hebrew, Hindi, Hungarian, Italian, Kannada, Latvian, Lithuanian, Malayalam, Marathi, Norwegian, Polish, Portuguese, Romanian, Russian, Serbian, Slovak, Slovenian, Spanish, Swahili, Swedish, Tamil, Telugu, Thai, Turkish, Ukrainian, Urdu and Vietnamese.

# Other requirements 
- Secure Gemini API key. (Is it safe it saved in .env.development.local or .env.development.production)

# Folder structure:
Generated a folder structure. How folders/files are stored. 

# Other 

- Save the selections of source language and target language to cookies and make sure the app remembers the last selected language when users come back to the app.

- Set dark mode as default when page is loaded. Save the dark/light mode to cookies and make it persist even after users close browsers.

- Add "Disclaimer" text at the bottom of the page: "This application does not store any of your data. Translations are processed in real-time and are not saved on our servers. However, please exercise caution when translating sensitive information, as this application utilizes the Google Gemini API and is therefore subject to Google's terms of service."

- Users can choose version of Gemini API 
 + Gemini 1.5 Flash (default)
 + Gemini 2.0 Flash 
 + Gemini 2.0 Flash-Lite

- Add "copy" buttons to copy the original text or translated text to clipboard.

Make the text "Translate from" and the source language selection dropdown in ONE line
Make the text "Translate to" and the target language selection dropdown in ONE line

Improve droopdown box for source language and target language.

Improve the following dropdown UI/UX:
the source language selection dropdown
the target language selection dropdown

so that users can 
- search for a language by pyting (such as typing "ja" will display "Japanese"")
- Easier to see all the languages they may select
