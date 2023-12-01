import flet as ft
from my_colors import MyColors


class Rail(ft.Container):
    def __init__(self):
        super().__init__()
        # Setting Form.table equal to the table passed into the func in main, which is created in data_table.py

        self.rail = ft.NavigationRail(
            bgcolor=MyColors.CONTAINER_COLOR_1,
            selected_index=0,
            label_type=ft.NavigationRailLabelType.ALL,
            extended=False,
            min_width=100,
            height=800,
            min_extended_width=150,
            leading=ft.FloatingActionButton(icon=ft.icons.STACKED_LINE_CHART, text="Create Campaign",
                                            bgcolor=MyColors.TEXT_COLOR_1),
            group_alignment=-0.7,
            destinations=[
                ft.NavigationRailDestination(
                    icon_content=ft.Icon(ft.icons.ANALYTICS_OUTLINED, color=MyColors.TEXT_COLOR_1),
                    selected_icon_content=ft.Icon(ft.icons.ANALYTICS, color=MyColors.TEXT_COLOR_1),
                    label_content=ft.Text("Analytics", color=MyColors.TEXT_COLOR_1)
                ),
                ft.NavigationRailDestination(
                    icon_content=ft.Icon(ft.icons.BUILD, color=MyColors.TEXT_COLOR_1),
                    selected_icon_content=ft.Icon(ft.icons.BUILD_OUTLINED, color=MyColors.TEXT_COLOR_1),
                    label_content=ft.Text("Scraper", color=MyColors.TEXT_COLOR_1)
                ),
                ft.NavigationRailDestination(
                    icon_content=ft.Icon(ft.icons.IMPORT_EXPORT_OUTLINED, color=MyColors.TEXT_COLOR_1),
                    selected_icon_content=ft.Icon(ft.icons.IMPORT_EXPORT, color=MyColors.TEXT_COLOR_1),
                    label_content=ft.Text("Import/Export", color=MyColors.TEXT_COLOR_1),
                ),
            ],
            on_change=lambda e: e.page.go("/page_2"),
        )
