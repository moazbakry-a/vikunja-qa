import pytest
from playwright.sync_api import expect
from test_data.project_tasks_titles import task1_edited

# TC_TASK_002
def test_edit_task(task_to_test):
    home_page, task1 = task_to_test

    home_page.edit_task_title(task1, task1_edited)
    # home_page.task_page.back()

    # Verify that the edited task is visible
    expect(home_page.get_task_link(task1_edited)).to_be_visible()

