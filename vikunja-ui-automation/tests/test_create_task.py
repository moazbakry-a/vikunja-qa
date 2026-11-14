import pytest
from playwright.sync_api import expect
from test_data.project_tasks_titles import task1

# TC_TASK_002
def test_create_task(project_to_test):
    home_page, project_title = project_to_test

    home_page.add_new_task(task1)

    # Verify that the new task is created
    expect(home_page.get_task_link(task1)).to_be_visible()




