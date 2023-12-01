import flet as ft
from form import form_style, label_style


class ScraperUi(ft.Container):
    def __init__(self):
        super().__init__(**form_style["main"])

        self.content = ft.Column(controls=[
            ft.Text("Please enter your sound ID", color="white"),
            ft.TextField(**form_style["input"], label="Sound ID", label_style=label_style),
        ],
            height=100,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
