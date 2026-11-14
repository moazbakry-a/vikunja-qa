import pytest 
from pages.home import Home
from test_data.login_data import VALID_USERNAME, VALID_PASSWORD
from test_data import project_tasks_titles as titles
from playwright.sync_api import Page, expect


def test_e2e(page: Page):
    home_page = Home(page)
    home_page.login_page.navigate_to_login_page()
    home_page.login_page.login(VALID_USERNAME, VALID_PASSWORD)
    # verify
    expect(home_page.welcome_heading).to_be_visible()

    home_page.create_project(titles.project_title)
    # verify
    expect(home_page.get_project_link(titles.project_title)).to_be_visible()

    home_page.edit_project_title(titles.project_edited_title)
    # verify
    expect(home_page.get_project_link(titles.project_edited_title)).to_be_visible()

    for task in titles.tasks:
        home_page.add_new_task(task)
    # verify 
    for task in titles.tasks:
        expect(home_page.get_task_link(task)).to_be_visible()


    home_page.edit_task_title(titles.task1, titles.task1_edited)
    # verify
    expect(home_page.get_task_link(titles.task1_edited)).to_be_visible()

    home_page.delete_task(titles.task2)
    # verify
    expect(home_page.get_task_link(titles.task2)).to_have_count(0)

    home_page.complete_task(titles.task3)
    # verify 
    expect(home_page.task_status(titles.task3)).to_be_checked()

    home_page.reopen_task(titles.task3)
    # verify
    expect(home_page.task_status(titles.task3)).not_to_be_checked()

    home_page.delete_project()
    #verify
    expect(home_page.get_project_link(titles.project_edited_title)).to_have_count(0)