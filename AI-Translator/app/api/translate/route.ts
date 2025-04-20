import { NextResponse } from 'next/server';
import { GoogleGenerativeAI } from '@google/generative-ai';

// Initialize the Google Generative AI with your API key
const genAI = new GoogleGenerativeAI(process.env.GEMINI_API_KEY || '');

export async function POST(request: Request) {
  try {
    const requestData = await request.json();
    console.log('Request data received:', requestData);
    
    const { sourceText, sourceLanguage, targetLanguage = 'Vietnamese' } = requestData;

    // More detailed validation with logging
    if (!sourceText) console.log('Missing sourceText field');
    if (!sourceLanguage) console.log('Missing sourceLanguage field');
    if (!targetLanguage) console.log('Missing targetLanguage field');

    // Validate the input
    if (!sourceText || !sourceLanguage) {
      return NextResponse.json({ 
        error: 'Missing required fields', 
        received: { sourceText, sourceLanguage, targetLanguage }
      }, { status: 400 });
    }

    // Use "gemini-1.5-flash" model instead of "gemini-pro"
    // This is the current model name supported in the latest API version
    const model = genAI.getGenerativeModel({ model: "gemini-1.5-flash" });

    // Make the prompt more explicit to ensure proper translation
    const prompt = `Translate the following text from ${sourceLanguage} to ${targetLanguage}. 
Return ONLY the translated text without any additional explanations or quotation marks:
"${sourceText}"`;
    
    console.log('Sending prompt to Gemini:', prompt);
    
    const result = await model.generateContent(prompt);
    const response = await result.response;
    let translatedText = response.text().trim();
    
    // Log the raw response for debugging
    console.log('Raw Gemini response:', translatedText);
    
    // Clean up the response if needed (removing quotes or explanations)
    translatedText = translatedText
      .replace(/^['"]|['"]$/g, '') // Remove surrounding quotes if present
      .replace(/^Translation:?\s*/i, '') // Remove "Translation:" prefix if present
      .trim();
    
    console.log('Final translated text:', translatedText);

    return NextResponse.json({ translatedText });
  } catch (error) {
    console.error('Translation API error:', error);
    return NextResponse.json({ error: 'Translation service error' }, { status: 500 });
  }
}