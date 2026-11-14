import pytest
from playwright.sync_api import Page, expect
from pages.login import LoginPage
from test_data.login_data import login_cases

BASE_URL = "http://localhost:3456"


@pytest.mark.parametrize(
    "username, password, testcase_id",
    login_cases,
    ids=[case[2] for case in login_cases]
)
def test_login(page: Page, username, password, testcase_id):
    """Verify login behaviour using different credential combinations."""

    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(username, password)

    # Assert
    if testcase_id in ("TC_LOGIN_001", "TC_LOGIN_002"):
        # Successful login
        expect(page).not_to_have_url(f"{BASE_URL}/login")
        expect(
            page.get_by_role("link", name="Projects", exact=True)
        ).to_be_visible()

    elif testcase_id == "TC_LOGIN_005":
        # Both fields empty
        expect(page).to_have_url(f"{BASE_URL}/login")
        expect(login_page.empty_username_message).to_be_visible()
        expect(login_page.empty_password_message).to_be_visible()

    elif testcase_id == "TC_LOGIN_007":
        # Empty username
        expect(login_page.empty_username_message).to_be_visible()

    elif testcase_id == "TC_LOGIN_008":
        # Empty password
        expect(login_page.empty_password_message).to_be_visible()

    elif testcase_id in (
        "TC_LOGIN_006",
        "TC_LOGIN_009",
        "TC_LOGIN_010",
        "TC_LOGIN_011",
        "TC_LOGIN_012",
        "TC_LOGIN_013"
    ):
        # Invalid credentials
        expect(page).to_have_url(f"{BASE_URL}/login")
        expect(login_page.wrong_message).to_be_visible()

    else:
        pytest.fail(f"No assertions defined for {testcase_id}")
    