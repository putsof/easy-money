submitBtn = document.getElementById("login-form-submit");
submitBtn.addEventListener('click', function() {
    const loginFormData = {
        email: document.getElementById("user_email"),
        password: document.getElementById("user_password"),
    };
    fetch('/login-check.json', {
        method: 'POST',
        body: JSON.stringify(loginFormData),
        headers: {
            'Content-Type': 'application/json',
        },
    })
    .then((response) => response.json())
    .then((jsonData) => {
        if (jsonData.status == 'Email does not exist'){
            alert("Email does not exist, Sign Up for an account");
        }
        else if (jsonData.status == 'Incorrect Password'){
            alert("Incorrect Password, Please Try Again");
        }
    })
})