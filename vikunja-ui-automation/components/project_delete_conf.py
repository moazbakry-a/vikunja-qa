from playwright.sync_api import Page
class ProjectDeleteDialog:
    def __init__(self, page: Page):
        self.page = page
        self.project_dialog = self.page.get_by_role(
              "dialog", name="Delete This project")
        self.confirm_button = self.project_dialog.get_by_role(
              "button", name="Do it!", exact=True)
        self.cancel_button = self.project_dialog.get_by_role("button", name="Cancel")
        self.close_button = self.project_dialog.get_by_role("button", name="Close dialog")

    def confirm_delete(self):
            self.confirm_button.click()
            

    def cancel_delete(self):
            self.cancel_button.click()

    def close_dialog(self):
            self.close_button.click()