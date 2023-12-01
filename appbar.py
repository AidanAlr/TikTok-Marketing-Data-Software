import flet as ft
from my_colors import MyColors

nav_bar_dic = {
    0: '/Browse',
    1: '/Import',
    2: '/Analytics',
    3: '/Scraper',
    4: '/Comment',
}

navbar = ft.NavigationBar(
    on_change=lambda e: e.page.go((nav_bar_dic[e.control.selected_index])),
    bgcolor=MyColors.INNER_CONTAINER_COLOR,
    height=60,
    destinations=[
            ft.NavigationDestination(icon=ft.icons.SEARCH,
                                     selected_icon=ft.icons.SEARCH_OUTLINED,
                                     label="Browse"),
            ft.NavigationDestination(icon=ft.icons.IMPORT_EXPORT,
                                     selected_icon=ft.icons.IMPORT_EXPORT_OUTLINED,
                                     label="Import"),
            ft.NavigationDestination(
                icon=ft.icons.ANALYTICS,
                selected_icon=ft.icons.ANALYTICS_OUTLINED,
                label="Analytics",

            ),
            ft.NavigationDestination(
                icon=ft.icons.BUILD_CIRCLE,
                selected_icon=ft.icons.BUILD_CIRCLE_OUTLINED,
                label="Scraper",

            ),
            ft.NavigationDestination(
                icon=ft.icons.THUMB_UP_ALT,
                selected_icon=ft.icons.THUMB_UP_ALT_OUTLINED,
                label="Comment bot",

            ),
        ]
    )


