// Get references to the form and submit button
const loginForm = document.getElementById('loginForm');
const loginButton = document.getElementById('loginButton');

// Event listener for the login form
loginForm.addEventListener('submit', (event) => {
    event.preventDefault();  // Prevent default form submission

    const email = document.getElementById('logEmail').value;
    const password = document.getElementById('logPassword').value;
    // console.log(email + " " + password);
    // Send a POST request to the /login endpoint
    fetch('http://127.0.0.1:5000/login', {
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
                window.location.href = '/index';
            }
            else {
                // Error message
                alert('Invalid username or password.');
            }
        })
        .catch(error => {
            console.error('Error during login:', error);
            alert('An error occurred. Please try again.');
        });
});