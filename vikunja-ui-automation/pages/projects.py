from playwright.sync_api import Page

class Projects:
    def __init__(self, page: Page):
        self.page = page
        self.new_project_button = self.page.get_by_role("link", name="New Project")
        self.new_project_dialog = self.page.get_by_role("dialog", name="New project")
        


    def create_new_project(self, project_name):
        self.new_project_button.click()
        self.new_project_dialog.get_by_role("textbox", name="Title").fill(project_name)
        self.new_project_dialog.get_by_role("button", name="Create").click()

    def close_new_project_dialog(self):
        self.new_project_dialog.get_by_role("button", name="Close dialog").click()

    def open_project(self, project_name):
        self.page.get_by_role("link", name=project_name).click()
