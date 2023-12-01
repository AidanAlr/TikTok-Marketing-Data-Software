import flet as ft
import appbar
import mode_switch
from form import Form
from data_table import DataTable
from file_import import MyFilePicker
from my_colors import MyColors
from scraper_ui import ScraperUi


my_file_picker = MyFilePicker()

form: ft.Container = Form(table=DataTable(collection='influencers'))

browse_page = ft.View("/Browse", [ft.Row(
    controls=[
        # Rail().rail,
        ft.Column(
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            expand=True,
            scroll="always",
            controls=[
                ft.Row(
                    [
                        form
                    ],
                    expand=False,
                    height=300,
                    width=1300

                ),
                ft.Divider(color='transparent', height=5),
                ft.Row(
                    [
                        form.table,

                    ],
                    expand=False,
                    height=380,
                    width=1300,
                    alignment=ft.MainAxisAlignment.CENTER,
                )
            ]
        )
    ]
)],
                      bgcolor=MyColors.BACKGROUND_COLOR,
                      navigation_bar=appbar.navbar,

                      )

import_page = ft.View("/Import", [ft.Row(
    controls=[
        ft.Column(
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            # expand=True,
            scroll="always",
            controls=[
                ft.Row(
                    [
                        my_file_picker

                    ],
                    expand=False,
                ),
                ft.Divider(color='transparent', height=2),
                ft.Row(
                    [
                        # data_table
                    ],
                    expand=False,
                    height=500,
                    width=1300,
                    alignment=ft.MainAxisAlignment.CENTER,
                )
            ]
        )
    ]
)],
                      bgcolor=MyColors.BACKGROUND_COLOR,
                      navigation_bar=appbar.navbar
                      )

explore_page = ft.View("/Analytics", [ft.Row(
    controls=[
        # Rail().rail,
        ft.Column(
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            expand=True,
            scroll="always",
            controls=[
                ft.Row(
                    [
                        mode_switch.ModeSwitch()
                    ],
                ),
            ]
        )
    ]
)],
                       bgcolor=MyColors.BACKGROUND_COLOR,
                       navigation_bar=appbar.navbar
                       )

scraper_page = ft.View("/Scraper", [ft.Row(
    controls=[
        # Rail().rail,
        ft.Column(
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            expand=True,
            scroll="always",
            controls=[
                ft.Row(
                    [
                        ScraperUi()
                    ],
                    expand=False,
                    height=300,
                    width=1300,
                    alignment=ft.MainAxisAlignment.CENTER


                ),
                ft.Divider(color='transparent', height=5),
                ft.Row(
                    [
                        # form.table,

                    ],
                    expand=False,
                    height=380,
                    width=1300,
                    alignment=ft.MainAxisAlignment.CENTER,
                )
            ]
        )
    ]
)],
                      bgcolor=MyColors.BACKGROUND_COLOR,
                      navigation_bar=appbar.navbar,

                      )
