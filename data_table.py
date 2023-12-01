import flet as ft
from my_colors import MyColors
import db_logic
from my_timer import timeit

data_table_style: dict = {
    "data_table": {
        "expand": True,
        "bgcolor": MyColors.CONTAINER_COLOR_1,
        "border_radius": 10

    },
}

text_style: dict = {
    "text_field": {
        "text_size": 10,
        "height": 35,
        'content_padding': 10,
        'expand': True,
        'border': ft.InputBorder.UNDERLINE
    },
    "text": {
        "size": 10,
        "color": MyColors.TEXT_COLOR_1,
        "text_align": ft.TextAlign.START
    }
}


def create_data_row(fields: list):
    cells_list = []
    for field in fields:
        cells_list.append(ft.DataCell(
            ft.Container(padding=5, content=ft.Text(value=field, width=92, tooltip=field, **text_style['text']))))

    return ft.DataRow(cells=cells_list)


column_headers = ['username', 'nickname', 'followers', 'bio', 'posts in last 28 days', 'median views in last 28 days',
                  'mean views in last 28 days', 'median comments in last 28 days', 'median likes in last 28 days',
                  'median views per follower',
                  'tags']


def get_db_row_data_for_table(collection):
    db_logic.connect_to_db()
    rows = []
    valid_record_count = 0

    # Querying for valid records i.e. contain the required columns
    for document in db_logic.query_collection({}, collection):
        if all(ele in list(document.keys()) for ele in column_headers):
            valid_record_count += 1
            # secuid = str(document['secUid'])[-5:]
            username = document['username']
            followers = document['followers']
            # link = document['link']
            nickname = document['nickname']
            bio = document['bio']
            posts = document['posts in last 28 days']
            median_views = document['median views in last 28 days']
            mean_views = document['mean views in last 28 days']
            median_likes = document['median likes in last 28 days']
            median_comments = document['median comments in last 28 days']
            median_views_per_follower = document['median views per follower'][:4]
            tags = document['tags']

            columns = [username, nickname, followers, bio, posts, median_views, mean_views, median_likes,
                       median_comments, median_views_per_follower, tags]

            new_data_row = create_data_row(columns)
            rows.append(new_data_row)

    print(str(valid_record_count) + " Valid Records")

    return rows


def get_db_column_data():
    headers_title = ['username', 'nickname', 'followers', 'bio', 'posts', 'median views',
                     'mean views', 'median likes', 'median comments', 'median views per follower', 'tags']
    column_headers_tooltip = column_headers
    pairs = zip(headers_title, column_headers_tooltip)

    return [ft.DataColumn(ft.Container(
        padding=10,
        content=ft.Text(title, tooltip=tooltip, style=ft.TextThemeStyle.DISPLAY_MEDIUM, size=14))) for
        title, tooltip in pairs]


class DataTable(ft.Container):
    global column_headers

    def __init__(self, collection):
        super().__init__(**data_table_style["data_table"])
        self.table = ft.DataTable(
            border=ft.border.all(2, "red"),
            show_bottom_border=True,
            border_radius=10,
            column_spacing=5,
            vertical_lines=ft.BorderSide(1, "green"),
            horizontal_lines=ft.BorderSide(1, "green"),
        )

        # Updating table data
        self.table.columns = get_db_column_data()
        self.table.rows = get_db_row_data_for_table(collection)

        cv = ft.Column([self.table], scroll="always")
        rv = ft.Row([cv], scroll="always", expand=1, vertical_alignment=ft.CrossAxisAlignment.START)

        self.content = (ft.Container(
            padding=10,
            margin=10,
            bgcolor=MyColors.CELL_COLOR,
            border_radius=10,
            border=ft.border.all(1, "black"),
            content=rv
        ))

