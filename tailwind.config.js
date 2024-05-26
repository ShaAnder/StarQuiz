/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [

    './frontend/templates/frontend/**/*.{galaxy.html, index.html, intro.html, planet_detail.html}',
    './quiz/templates/quiz/**/*.{leaderboard.html, quiz_result.html, quiz.html}',
    './templates/**/*base.html',

  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

