from playwright.sync_api import Page
class EditDialog:
    def __init__(self, page: Page):
        self.page = page
        self.dialog = self.page.get_by_role("dialog", name="Edit This Project")
        self.title_textbox = self.dialog.get_by_role("textbox", name="Title")
        self.save_button = self.dialog.get_by_role("button", name="Save")
        self.cancel_button = self.dialog.get_by_role("button", name="Cancel")
        self.delete_button = self.dialog.get_by_role("button", name="Delete")
        self.close_button = self.dialog.get_by_role("button", name="Close dialog")

    def edit_title(self, new_title):
        self.title_textbox.fill(new_title)
        self.save_button.click()

    def cancel_edit(self):
        self.cancel_button.click()

    def delete_project(self):
        self.delete_button.click()

    def close_dialog(self):
        self.close_button.click()
