
VALID_PASSWORD = "testing_passowrd123!"
VALID_USERNAME = "testing_account"

login_cases = [
    # TC_LOGIN_001: Valid username and password
    (VALID_USERNAME, VALID_PASSWORD, "TC_LOGIN_001"),

    # TC_LOGIN_002: Valid email and password
    ("testing_account@example.com", VALID_PASSWORD, "TC_LOGIN_002"),

    # TC_LOGIN_005: Both fields empty
    ("", "", "TC_LOGIN_005"),

    # TC_LOGIN_006: Both fields contain spaces only
    ("   ", "   ", "TC_LOGIN_006"),

    # TC_LOGIN_007: Empty username
    ("", VALID_PASSWORD, "TC_LOGIN_007"),

    # TC_LOGIN_008: Empty password
    (VALID_USERNAME, "", "TC_LOGIN_008"),

    # TC_LOGIN_009: Username with leading/trailing spaces
    (" testing_account ", VALID_PASSWORD, "TC_LOGIN_009"),

    # TC_LOGIN_010: Email with leading/trailing spaces
    (" testing_account@example.com ", VALID_PASSWORD, "TC_LOGIN_010"),

    # TC_LOGIN_011: Wrong password
    ("testing_account", "wrong_password123!", "TC_LOGIN_011"),

    # TC_LOGIN_012: Unregistered email
    ("unregistered_user@example.com", VALID_PASSWORD, "TC_LOGIN_012"),

    # TC_LOGIN_013: Unregistered username
    ("unregistered_user", VALID_PASSWORD, "TC_LOGIN_013"),
]