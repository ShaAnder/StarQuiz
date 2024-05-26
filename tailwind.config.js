/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [

    './frontend/templates/frontend/**/*galaxy.html',
    './frontend/templates/frontend/**/*planet_detail.html',
    './frontend/templates/frontend/**/*intro.html',
    './frontend/templates/frontend/**/*index.html',
    './quiz/templates/quiz/**/*quiz.html',
    './quiz/templates/quiz/**/*quiz_result.html',
    './quiz/templates/quiz/**/*leaderboard.html',
    './templates/**/*base.html',
    './templates/includes/**/*navbar.html',
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

