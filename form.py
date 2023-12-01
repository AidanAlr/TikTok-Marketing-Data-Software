import flet as ft
import data_table
import db_logic
import mode_switch
from my_colors import MyColors
from my_timer import timeit
from data_table import DataTable

label_style = ft.TextStyle(size=10, weight="bold", color=MyColors.TEXT_COLOR_1)

form_style: dict = {
    "main": {
        "expand": 1,
        "bgcolor": MyColors.CONTAINER_COLOR_1,
        "padding": 5,
        "border_radius": 20,

    },
    "input": {
        "height": 50,
        "border_color": "#aeaeb3",
        "focused_border_color": "black",
        "border_radius": 5,
        "cursor_height": 16,
        "cursor_color": "black",
        "content_padding": 10,
        "border_width": 1.5,
        "text_size": 12,
        "color": MyColors.TEXT_COLOR_1,
        "width": 150,
        "bgcolor": MyColors.CELL_COLOR,
        "opacity": 0.9,

    },
    "long_input": {
        "height": 38,
        "border_color": "#aeaeb3",
        "focused_border_color": "black",
        "border_radius": 5,
        "cursor_height": 16,
        "cursor_color": "black",
        "content_padding": 10,
        "border_width": 1.5,
        "text_size": 12,
        "width": 200,
        "multiline": True,
        "min_lines": 1,
        "max_lines": 10,
        "bgcolor": MyColors.CONTAINER_COLOR_1,
    },
    "dropdown": {
        "label_style": label_style,
        "width": 100,
        "height": 38,
        "text_size": 12,
        "content_padding": 10,
        "border_width": 1.5,
        "border_color": "#aeaeb3",
        "bgcolor": MyColors.CELL_COLOR,
    },
    'foreground_style': ft.TextStyle(size=47,
                                     weight=ft.FontWeight.BOLD,
                                     foreground=ft.Paint(
                                         color=ft.colors.BLACK,
                                         stroke_width=1,
                                         # stroke_join=ft.StrokeJoin.ROUND,
                                         style=ft.PaintingStyle.FILL))
}

title = ft.Stack(
    [
        ft.Text(
            spans=[
                ft.TextSpan(
                    "AGENCY",
                    ft.TextStyle(
                        size=40,
                        weight=ft.FontWeight.BOLD,
                        foreground=ft.Paint(
                            color=MyColors.BACKGROUND_COLOR,
                            stroke_width=6,
                            stroke_join=ft.StrokeJoin.ROUND,
                            style=ft.PaintingStyle.STROKE,
                        ),
                    ),
                ),
            ],
        ),
        ft.Text(
            spans=[
                ft.TextSpan(
                    "AGENCY",
                    ft.TextStyle(
                        size=40,
                        weight=ft.FontWeight.BOLD,
                        color=ft.colors.GREY_300,
                    ),
                ),
            ],
        ),
    ]
)


class Form(ft.Container):

    def __init__(self, table: ft.DataTable):
        super().__init__(**form_style["main"])

        self.collection_dropdown = ft.Dropdown(
            label="Collection",
            options=[
                ft.dropdown.Option(x) for x in db_logic.get_collection_names()
            ],
            width=200
        )

        self.table: DataTable = table

        # First row of fields in form
        self.username = ft.TextField(**form_style["input"], label="username", label_style=label_style)
        self.nickname = ft.TextField(**form_style["input"], label="nickname", label_style=label_style)
        self.followers = ft.TextField(**form_style["input"], label="followers", label_style=label_style)
        self.bio = ft.TextField(**form_style["input"], label="bio", label_style=label_style)
        self.posts = ft.TextField(**form_style["input"], label="posts", label_style=label_style)
        self.median_views = ft.TextField(**form_style["input"], label="median views", label_style=label_style)
        self.mean_views = ft.TextField(**form_style["input"], label="mean views", label_style=label_style)
        self.median_likes = ft.TextField(**form_style["input"], label="median likes", label_style=label_style)
        self.median_comments = ft.TextField(**form_style["input"], label="median comments", label_style=label_style)
        self.median_views_per_follower = ft.TextField(**form_style["input"], label="median views per follower",
                                                      label_style=label_style)
        self.tags = ft.TextField(**form_style["input"], label="tags", label_style=label_style)

        # Button to trigger add to database
        self.add_to_db_button = ft.ElevatedButton(
            text="Save",
            color="white",
            bgcolor="blue600",
            height=38,
            style=ft.ButtonStyle(shape={"": ft.RoundedRectangleBorder(radius=5)}),
            on_click=self.save_data,
            width=100
        )

        self.region = ft.Dropdown(
            label="Region",
            options=[
                ft.dropdown.Option("NA"),
                ft.dropdown.Option("EU"),
                ft.dropdown.Option("Asia"),
            ],
            **form_style["dropdown"]
        )

        self.category = ft.Dropdown(
            label="Category",
            options=[
                ft.dropdown.Option("Anime"),
                ft.dropdown.Option("Edits"),
                ft.dropdown.Option("Gaming"),
            ],
            **form_style["dropdown"]
        )

        # Creating our Text fields for our form, we call our db and get all keys in the collection
        text_fields = [ft.TextField(**form_style["input"], label=key, label_style=label_style) for key in
                       db_logic.get_all_collection_keys('influencers')]

        text_fields.append(self.add_to_db_button)

        # Creating our responsive row from our text fields
        info_row = (ft.ResponsiveRow(controls=
                                     [ft.Column(col={"sm": 1, "md": 1, "xl": 1}, controls=[text_field]) for text_field
                                      in text_fields],
                                     alignment=ft.MainAxisAlignment.START
                                     ))

        # Setting the content of the form
        self.content = ft.Container(
            padding=10,
            margin=10,
            border_radius=10,
            bgcolor=MyColors.INNER_CONTAINER_COLOR,
            content=ft.Column(
                controls=[
                    ft.Container(
                        content=ft.Row(
                            controls=[
                                title,
                                self.collection_dropdown,
                                mode_switch.ModeSwitch()
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                        ),
                        bgcolor=MyColors.CELL_COLOR,
                        margin=0,
                        border_radius=10,
                        padding=ft.Padding(top=10, bottom=10, left=20, right=20),
                    ),

                    ft.Divider(height=5, color="transparent"),
                    info_row,
                ],
                spacing=2,

            ))

    # @timeit
    def update_data_table(self):
        self.table.table.rows = data_table.get_db_row_data_for_table(collection='influencers')
        self.table.update()

    def save_data(self, event):
        all_fields = [self.username, self.nickname, self.followers, self.bio,
                      self.posts, self.median_views, self.mean_views, self.median_comments,
                      self.median_likes, self.median_views_per_follower, self.tags]
        # required_fields = [x.value for x in all_fields]
        required_fields = [True]
        # Check if the required fields are all filled out
        if all(required_fields):
            db_logic.post_document(
                {"username": self.username.value,
                 "nickname": self.nickname.value,
                 "followers": self.followers.value,
                 "bio": self.bio.value,
                 "posts in last 28 days": self.posts.value,
                 "median views in last 28 days": self.median_views.value,
                 "mean views in last 28 days": self.median_views.value,
                 "median comments in last 28 days": self.median_comments.value,
                 "median likes in last 28 days": self.median_likes.value,
                 "median views per follower": self.median_views_per_follower.value,
                 "tags": self.tags.value},
                'influencers')

            # Resetting all of our text fields
            for x in all_fields:
                x.value = ''

            self.update_data_table()
            self.page.update()

        else:
            print("Not all required fields are filled")
