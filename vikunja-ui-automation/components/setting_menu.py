
# from playwright.sync_api import Page


# class SettingsMenu:
#     def __init__(self, page: Page):
#         self.page = page

#     def open_project_settings(self, project_name):
#         project_card = self.page.locator(
#             "li.project-grid-item"
#         ).filter(
#             has=self.page.get_by_role(
#                 "link", name=project_name, exact=True
#             )
#         )

#         project_card.get_by_role(
#             "button", name="Open project settings menu"
#         ).click()

#         return project_card

    # def open_edit_project_dialog(self):
    #     project_card = self.open_project_settings(project_name)

    #     project_card.get_by_role(
    #         "link", name="Edit", exact=True
    #     ).click()

#     def open_delete_project_dialog(self, project_name):
#         project_card = self.open_project_settings(project_name)

#         project_card.get_by_role(
#             "link", name="Delete", exact=True
#         ).click()

#-------------------------------------------
from playwright.sync_api import Page


class SettingsMenu:
    def __init__(self, page: Page):
        self.page = page
        self.edit_button = self.page.get_by_role("link", name="Edit", exact=True)
        self.delete_button = self.page.get_by_role("link", name="Delete", exact=True)

    def open_edit_dialog(self):
        self.edit_button.click()

    def open_delete_dialog(self):
        self.delete_button.click()