import pytest
from playwright.sync_api import expect


# TC_TASK_002
def test_edit_task(task_to_test):
    home_page, task1 = task_to_test

    home_page.complete_task(task1)
    
    # Verify task cehcked
    expect(home_page.task_status(task1)).to_be_checked()

    # verify task is no longer exist in list view
    home_page.refresh()
    expect(home_page.get_task_link(task1)).to_have_count(0)