from playwright.sync_api import expect
from pages.home import Home
from test_data.project_tasks_titles import project_title

# TC_PROJ_023
def test_project_deletion(logged_in_user):
    """Verify that the project can be deleted successfully."""
    
    home_page = Home(logged_in_user)
    home_page.create_project(project_title)
    home_page.delete_project()

    # verify that the project is deleted
    expect(home_page.get_project_link(project_title)).to_have_count(0)