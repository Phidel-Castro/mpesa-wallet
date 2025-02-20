import streamlit as st
import streamlit.components.v1 as components

html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin: 0;
            padding: 50px;
            background: linear-gradient(to right, #4a90e2, #357abd);
            color: white;
        }
        .container {
            width: 350px;
            margin: auto;
        }
        .card {
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            color: black;
        }
        input, button {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: none;
            border-radius: 5px;
        }
        button {
            background: #4a90e2;
            color: white;
            cursor: pointer;
        }
        button:hover {
            background: #357abd;
        }
    </style>
</head>
<body>
    <h1>Welcome to Our Platform</h1>
    <p>Experience seamless login and signup.</p>
    <div class="container">
        <div id="login-page" class="card">
            <h2>Login</h2>
            <input type="text" id="login-name" placeholder="Name" required>
            <input type="email" id="login-email" placeholder="Email" required>
            <input type="password" id="login-password" placeholder="Password" required>
            <button onclick="window.location.href='/?page=main&name='+document.getElementById('login-name').value">Login</button>
            <p><a href="#" onclick="switchForm('signup')">Don't have an account? Sign up</a></p>
        </div>
        <div id="signup-page" class="card" style="display:none;">
            <h2>Sign Up</h2>
            <input type="text" id="signup-name" placeholder="Name" required>
            <input type="email" id="signup-email" placeholder="Email" required>
            <input type="password" id="signup-password" placeholder="Password" required>
            <button onclick="window.location.href='/?page=main&name='+document.getElementById('signup-name').value">Sign Up</button>
            <p><a href="#" onclick="switchForm('login')">Already have an account? Login</a></p>
        </div>
    </div>
    <script>
        function switchForm(formId) {
            document.getElementById('login-page').style.display = formId === 'login' ? 'block' : 'none';
            document.getElementById('signup-page').style.display = formId === 'signup' ? 'block' : 'none';
        }
    </script>
</body>
</html>
"""

def main():
    page = st.query_params.get("page", "welcome")
    name = st.query_params.get("name", "User")
    
    if page == "welcome":
        st.markdown("""
            <h1 style='text-align: center; color: #4a90e2;'>Welcome to Our Platform</h1>
            <p style='text-align: center;'>Experience seamless login and signup.</p>
            <div style='display: flex; justify-content: center;'>
                <a href='/?page=login'><button style='padding: 10px 20px; background: #4a90e2; color: white; border: none; border-radius: 5px; cursor: pointer;'>Get Started</button></a>
            </div>
        """, unsafe_allow_html=True)
    elif page == "main":
        st.success(f"Welcome to the Main Page, {name}! 🎉")
        st.write("Here is your main application content.")
    else:
        components.html(html_code, height=600)

if __name__ == "__main__":
    main()
