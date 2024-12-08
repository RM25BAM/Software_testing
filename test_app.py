from app import App

def test_signup_success():
    app = App()
    result = app.signup(name="John Doe", email="john.doe@example.com", password="password123")
    assert result["message"] == "User signed up and data stored successfully. mock_user_id"

def test_signup_missing_fields():
    app = App()
    result = app.signup(name="", email="john.doe@example.com", password="password123")
    assert result["message"] == "All fields are required"

def test_login_success():
    app = App()
    app.signup(name="John Doe", email="john.doe@example.com", password="password123")
    result = app.login(email="john.doe@example.com", password="password123")
    assert result["role"] == "employee"
    assert result["userId"] == "mock_user_id"

def test_login_missing_fields():
    app = App()
    result = app.login(email="", password="password123")
    assert result["message"] == "All fields are required"
