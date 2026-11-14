import pytest
from playwright.sync_api import expect
from pages.home import Home
from pages.projects import Projects
from test_data.project_tasks_titles import project_title

#TC_PROJ_003
def test_create_project(logged_in_user):
    """Verify that a new project can be created successfully."""

    home_page = Home(logged_in_user)
    home_page.create_project(project_title)

    # Verify that the new project is created
    expect(home_page.get_project_link(project_title)).to_be_visible()

    

    