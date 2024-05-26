document.addEventListener('DOMContentLoaded', function() {
    const inputs = document.querySelectorAll('input, select, textarea');
    inputs.forEach(input => {
        input.classList.add('form-input');
    });
});