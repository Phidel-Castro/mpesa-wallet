# app.py
import streamlit as st
import streamlit.components.v1 as components
import numpy as np
import pandas as pd

html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        :root {
            --bg-color: #ffffff;
            --text-color: #333333;
            --card-bg: #f5f5f5;
            --btn-bg: #4a90e2;
            --btn-hover: #357abd;
        }

        [data-theme="dark"] {
            --bg-color: #1a1a1a;
            --text-color: #ffffff;
            --card-bg: #2d2d2d;
            --btn-bg: #4a90e2;
            --btn-hover: #357abd;
        }

        body {
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
            background-color: var(--bg-color);
            color: var(--text-color);
            transition: all 0.3s ease;
        }

        .container {
            width: 350px;
            padding: 20px;
            margin: 0 auto;
        }

        .card {
            background-color: var(--card-bg);
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }

        .form-page {
            display: none;
        }

        .form-page.active {
            display: block;
        }

        h2 {
            text-align: center;
            margin-bottom: 20px;
        }

        .form-group {
            margin-bottom: 15px;
        }

        input {
            width: 100%;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
            background-color: var(--bg-color);
            color: var(--text-color);
            box-sizing: border-box;
        }

        button {
            width: 100%;
            padding: 10px;
            background-color: var(--btn-bg);
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }

        button:hover {
            background-color: var(--btn-hover);
        }

        .toggle-link {
            text-align: center;
            margin-top: 15px;
            cursor: pointer;
            color: var(--btn-bg);
        }

        .theme-toggle {
            padding: 8px 16px;
            background-color: var(--btn-bg);
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            margin-bottom: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <button class="theme-toggle" onclick="toggleTheme()">Toggle Theme</button>
        
        <div id="login-page" class="form-page active card">
            <h2>Login</h2>
            <div class="form-group">
                <input type="email" id="login-email" placeholder="Email" required>
            </div>
            <div class="form-group">
                <input type="password" id="login-password" placeholder="Password" required>
            </div>
            <button onclick="parent.postMessage({type: 'login', email: document.getElementById('login-email').value, password: document.getElementById('login-password').value}, '*')">Login</button>
            <div class="toggle-link" onclick="switchForm('signup')">Don't have an account? Sign up</div>
        </div>

        <div id="signup-page" class="form-page card">
            <h2>Sign Up</h2>
            <div class="form-group">
                <input type="text" id="signup-username" placeholder="Username" required>
            </div>
            <div class="form-group">
                <input type="email" id="signup-email" placeholder="Email" required>
            </div>
            <div class="form-group">
                <input type="password" id="signup-password" placeholder="Password" required>
            </div>
            <button onclick="parent.postMessage({type: 'signup', username: document.getElementById('signup-username').value, email: document.getElementById('signup-email').value, password: document.getElementById('signup-password').value}, '*')">Sign Up</button>
            <div class="toggle-link" onclick="switchForm('login')">Already have an account? Login</div>
        </div>
    </div>

    <script>
        function toggleTheme() {
            const html = document.documentElement;
            const currentTheme = html.getAttribute('data-theme');
            if (currentTheme === 'dark') {
                html.removeAttribute('data-theme');
            } else {
                html.setAttribute('data-theme', 'dark');
            }
        }

        function switchForm(formId) {
            const loginPage = document.getElementById('login-page');
            const signupPage = document.getElementById('signup-page');
            
            if (formId === 'login') {
                signupPage.classList.remove('active');
                loginPage.classList.add('active');
            } else {
                loginPage.classList.remove('active');
                signupPage.classList.add('active');
            }
        }
    </script>
</body>
</html>
"""

if 'users' not in st.session_state:
    st.session_state.users = pd.DataFrame(columns=['username', 'email', 'password'])

def main():
    st.title("Login/Signup App")
    component_value = components.html(html_code, height=500)

    if st.session_state.get('message'):
        message = st.session_state.message
        if message['type'] == 'login':
            email = message['email']
            password = message['password']
            if email in st.session_state.users['email'].values:
                user = st.session_state.users[st.session_state.users['email'] == email].iloc[0]
                if user['password'] == password:
                    st.success(f"Welcome back! Logged in as {email}")
                    random_data = np.random.randn(5)
                    st.write("Random data sample:", random_data)
                else:
                    st.error("Incorrect password")
            else:
                st.error("User not found")
        elif message['type'] == 'signup':
            username = message['username']
            email = message['email']
            password = message['password']
            if email not in st.session_state.users['email'].values:
                new_user = pd.DataFrame([[username, email, password]], 
                                     columns=['username', 'email', 'password'])
                st.session_state.users = pd.concat([st.session_state.users, new_user], 
                                                 ignore_index=True)
                st.success(f"Successfully signed up! Welcome {username}")
                st.write("Current users:", st.session_state.users)
            else:
                st.error("Email already exists")

    st.markdown("""
        <script>
        window.addEventListener('message', function(e) {
            const data = e.data;
            if (data.type) {
                Streamlit.setComponentValue(data);
            }
        });
        </script>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()