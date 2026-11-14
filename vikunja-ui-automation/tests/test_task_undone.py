import pytest
from playwright.sync_api import expect


# TC_TASK_002
def test_edit_task(done_task_to_test):
    home_page, task1 = done_task_to_test

    home_page.reopen_task(task1)

    # Verify task undone
    expect(home_page.task_status(task1)).not_to_be_checked()

    # verify task is no longer exist in list view
    home_page.refresh()
    expect(home_page.get_task_link(task1)).to_be_visible()