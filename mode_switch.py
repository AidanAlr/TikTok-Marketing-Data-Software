import flet as ft
from my_colors import MyColors


class ModeSwitch(ft.Container):
    def __init__(self):
        def button_clicked(e):
            if self.switch.value:
                mode = 'Edit'
                self.mode_icon.name = ft.icons.EDIT

            else:
                mode = 'Search'
                self.mode_icon.name = ft.icons.SEARCH

            self.mode_text.value = f'You are in {mode} mode'
            self.page.update()

        super().__init__()
        self.width = 300
        self.bgcolor = MyColors.INNER_CONTAINER_COLOR
        self.border_radius = 10
        self.mode_text = ft.Text("You are in edit mode", color=MyColors.TEXT_COLOR_1)
        self.mode_icon = ft.Icon(name=ft.icons.EDIT, color="white")

        self.switch = ft.Switch(value=True, on_change=button_clicked)

        self.content = ft.Row(controls=[self.mode_icon, self.switch, self.mode_text],
                              alignment=ft.MainAxisAlignment.CENTER)


