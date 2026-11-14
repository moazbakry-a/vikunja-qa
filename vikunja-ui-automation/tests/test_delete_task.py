import pytest
from playwright.sync_api import expect

def test_delete_task(task_to_test):
    home_page, task1 = task_to_test

    home_page.delete_task(task1)

    expect(home_page.get_task_link(task1)).to_have_count(0)
