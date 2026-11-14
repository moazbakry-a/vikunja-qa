from components.setting_menu import SettingsMenu
from components.edit_dialog import EditDialog
from playwright.sync_api import Page
from components.project_delete_conf import ProjectDeleteDialog
from components.task_delete_conf import TaskDeleteDialog
from pages.projects import Projects
from pages.task import TaskPage
from pages.login import LoginPage



class Home:
    def __init__(self, page: Page):
        self.page = page
        
        self.welcome_heading = self.page.get_by_role(
            "heading", level=1)
        ## "navigation"
        self.overview_link = self.page.get_by_role(
            "link", name="Overview")
        self.projects_link = self.page.get_by_role(
            "link", name="Projects")
        self.project_settings_button = self.page.get_by_role(
            "button", name="Open project settings menu")
        self.edit_project_button = self.page.get_by_role(
            "link", name="Edit")
        self.delete_project_button = self.page.get_by_role(
            "link", name="Delete")
        
        self.add_task_textbox = self.page.get_by_role(
            "textbox", name="Add a task…")
        self.add_task_button = self.page.get_by_role("button", name="Add", exact=True)

        self.account_menu_button = self.page.get_by_role(
          "button", name="testing_account", exact=True)
        self.logout_button = self.page.get_by_role(
           "button", name="Logout")
        
        
        self.setting_menu = SettingsMenu(self.page)
        self.project_delete_conf = ProjectDeleteDialog(self.page)
        self.task_delete_conf = TaskDeleteDialog(self.page)
        self.projects = Projects(self.page)
        self.edit_dialog = EditDialog(self.page)
        self.task_page = TaskPage(self.page)
        self.login_page = LoginPage(self.page)

    def refresh(self):
        self.page.reload()


    def navigate_to_projects(self):
        self.projects_link.click()

    def navigate_to_overview(self):
        self.overview_link.click()

    def logout(self):
        self.account_menu_button.click()
        self.logout_button.click()

    def open_project(self, project_name):
        self.page.get_by_role("link", name=project_name, exact=True ).click()
    

    # project management

    def open_project_settings(self):
        self.page.get_by_role(
        "banner", name="main navigation").get_by_role(
        "button", name="Open project settings menu").click()

    def create_project(self, project_title):
        self.navigate_to_projects()
        self.projects.create_new_project(project_title)

    def edit_project_title(self, project_edited_title):
        self.open_project_settings()
        self.setting_menu.open_edit_dialog()
        self.edit_dialog.edit_title(project_edited_title)
        

    def delete_project(self):
        self.open_project_settings()
        self.setting_menu.open_delete_dialog()
        self.project_delete_conf.confirm_delete()

    def get_project_link(self, project_title):
        return self.page.get_by_role(
        "link", name=project_title, exact=True)
    

    ## task management
    def add_new_task(self, task_name):
        self.add_task_textbox.fill(task_name)
        self.add_task_button.click()

    def open_task(self, task_name):
        self.page.get_by_role("link", name=task_name , exact=True).click()


    def edit_task_title(self, task_name, new_title):
        self.open_task(task_name)
        self.task_page.edit_title(new_title)
        self.task_page.back()
        

    def complete_task(self, task_title):
        task_row = self.page.locator("[data-task-id]").filter(
        has=self.page.get_by_role("link", name=task_title, exact=True))
        task_row.locator("label.base-checkbox__label").click()

    def reopen_task(self, task_name):
        self.open_task(task_name)
        self.task_page.mark_task_as_undone()
        self.task_page.back()

    def delete_task(self, task_name):
        self.open_task(task_name)
        self.task_page.delete()
        self.task_delete_conf.confirm_delete()

    def get_task_link(self, task_name):
        return self.page.get_by_role(
        "link", name=task_name, exact=True)
    
    def task_status(self, task_name):
         return self.page.get_by_role(
        "checkbox",
        name=f"Mark '{task_name}' as done", exact=True)
    
