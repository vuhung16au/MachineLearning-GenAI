/** @type {import('tailwindcss').Config} */
export default {
  content: [
    './index.html',
    './css/**/*.{css,js}',
    './cypress/e2e/**/*.{js,ts}',
    './*.{html,js,ts}'
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
