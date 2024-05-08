// Get references to the form and submit button
const registerForm = document.getElementById('RegisterForm');
const submitButton = document.getElementById('submitButton');

// Event listener for the form submission
registerForm.addEventListener('submit', (event) => {
    event.preventDefault();  // Prevent default form submission

    const email = document.getElementById('regEmail').value;
    const password = document.getElementById('regPassword').value;

    // Send a POST request to the /register endpoint
    fetch('http://127.0.0.1:5000/register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ email, password })
    })
        .then(response => response.text())
        .then(responseText => {
            if (responseText === 'done') {
                // Redirection
                window.location.href = '/login';
            } else if (responseText === 'Exists') {
                // Error message
                alert('Username already exists.');
            } else {
                // Handle any other unexpected responses
                console.error('Unexpected response from server:', responseText);
                alert('An error occurred. Please try again.');
            }
        })
        .catch(error => {
            console.error('Error during registration:', error);
            alert('An error occurred. Please try again.');
        });
});