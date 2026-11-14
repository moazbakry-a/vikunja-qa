from playwright.sync_api import Page

class TaskPage():
    def __init__(self, page: Page):
        self.page = page
        self.back_button = self.page.get_by_role("button", name=" Back to project")
        self.task_title = self.page.get_by_role("heading", name="Title")
        self.mark_task_done_button = self.page.get_by_role("button", name="Mark Task done!")
        self.mark_task_undone_button = self.page.get_by_role("button", name="Mark as undone")
        self.delete_task_button = self.page.get_by_role("button", name="Delete")
        

    def edit_title(self, new_title):
        self.task_title.fill(new_title)
        self.task_title.press("Enter")

    def mark_task_as_done(self):
        self.mark_task_done_button.click()

    def mark_task_as_undone(self):
        self.mark_task_undone_button.click()

    def delete(self):
        self.delete_task_button.click()
        

    def back(self):
        self.back_button.click()

        
