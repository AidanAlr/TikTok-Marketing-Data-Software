import flet as ft

import db_logic
import views
import db_logic as db
from my_colors import MyColors


def main(page: ft.Page):
    db.connect_to_db()
    db.get_all_collection_keys('influencers')
    page.theme_mode = ft.ThemeMode.LIGHT
    page.title = 'Agency'
    page.window_width = 1200
    page.window_height = 800
    page.padding = 5
    page.bgcolor = MyColors.BACKGROUND_COLOR
    page.window_center()

    def route_change(route):
        page.views.clear()
        page.views.append(views.browse_page)
        if page.route == '/Import':
            page.views.clear()
            page.views.append(views.import_page)
        if page.route == '/Browse':
            page.views.clear()
            page.views.append(views.browse_page)
        if page.route == '/Analytics':
            page.views.clear()
            page.views.append(views.explore_page)
        if page.route == '/Scraper':
            page.views.clear()
            page.views.append(views.scraper_page)

        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


if __name__ == "__main__":
    ft.app(target=main)
