import pytest
from pages.login import LoginPage
from pages.home import Home
from test_data.project_tasks_titles import project_title, task1
from playwright.sync_api import expect

@pytest.fixture()
def logged_in_user(page):
    """Fixture to log in a user before running a test."""
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("testing_account", "testing_passowrd123!")
    expect(page.get_by_role("link", name="Projects", exact=True)).to_be_visible()
    return page

@pytest.fixture
def project_to_test(logged_in_user):

    # Setup: login and create the project
    home_page = Home(logged_in_user)
    home_page.create_project(project_title)

    # Provide the project to the test
    yield home_page, project_title

    # Teardown: delete the project
    home_page.delete_project()

@pytest.fixture
def task_to_test(project_to_test):

    # Setup: create a task
    home_page, project_title = project_to_test

    home_page.add_new_task(task1)

    # Provide the task to the test
    yield home_page, task1

@pytest.fixture
def done_task_to_test(task_to_test):

    # Setup: create a task
    home_page, task1 = task_to_test
    home_page.complete_task(task1)
    expect(home_page.task_status(task1)).to_be_checked()

    # Provide the checked task to the test
    yield home_page, task1

    