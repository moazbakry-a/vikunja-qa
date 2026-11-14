import pytest
from playwright.sync_api import expect
from pages.home import Home
from pages.projects import Projects
from components.edit_dialog import EditDialog
from test_data.project_tasks_titles import project_edited_title

#TC_PROJ_011
def test_edit_project(project_to_test):
    """Verify that a project's title can be edited successfully."""
    home_page, project_title = project_to_test
    
    home_page.edit_project_title(project_edited_title)

    # verify that the project title is edited
    expect(home_page.get_project_link(project_edited_title)).to_be_visible()

    
