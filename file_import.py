import flet as ft
import shutil
from my_timer import timeit
from my_colors import MyColors
from csv_to_json import csv_to_json
from db_logic import post_document
import pandas as pd


def upload_csv(csv_file_path, collection):
    def add_index_column_to_csv(csv_file_path):
        # Read the CSV file into a DataFrame
        df = pd.read_csv(csv_file_path)

        # Check if the "index" column already exists
        if "index" not in df.columns:
            # If it doesn't exist, add a new "index" column with row numbers
            df["index"] = df.index + 1  # You can change 1 to 0 if you want 0-based indexing

            # Write the updated DataFrame back to the CSV file
            df.to_csv(csv_file_path, index=False)  # Set index=False to avoid writing the default index

        else:
            print("The 'index' column already exists in the CSV file.")

    add_index_column_to_csv(csv_file_path)

    converted_csv_dic = csv_to_json(csv_file_path)
    counter = 0
    for document in converted_csv_dic.values():
        if document['index']:
            del document['index']
        post_document(document, collection)
        counter += 1

    print(f"Posted {counter} documents to {collection}")


class MyFilePicker(ft.Container):
    def __init__(self):
        super().__init__()
        self.pick_files_dialog = ft.FilePicker(on_result=self.pick_files_result)
        self.selected_files_text = ft.Text()
        self.selected_file = None

        @timeit
        def pick_files(_) -> None:
            self.pick_files_dialog.pick_files(allow_multiple=False)

        @timeit
        def upload_files(_) -> None:
            if str(self.selected_file.path).endswith(".csv"):
                print("You have chosen a CSV!")
                upload_csv(self.selected_file.path, 'influencers')
                self.selected_files_text.value = 'Upload Complete'
                self.selected_files_text.update()

        self.content = ft.Container(
            bgcolor=MyColors.CONTAINER_COLOR_1,
            padding=10,
            margin=10,
            alignment=ft.alignment.center,
            expand=True,
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[self.pick_files_dialog,
                          ft.Row(controls=[ft.ElevatedButton("Pick files",
                                                             icon=ft.icons.FILE_OPEN,
                                                             on_click=pick_files,
                                                             ),
                                           ft.ElevatedButton("Upload",
                                                             icon=ft.icons.UPLOAD_FILE,
                                                             on_click=upload_files,
                                                             )],
                                 alignment=ft.MainAxisAlignment.CENTER,
                                 ),
                          self.selected_files_text],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )

    def pick_files_result(self, e: ft.FilePickerResultEvent) -> None:
        if e:
            # Getting the path of our selected file
            self.selected_file = e.files[0]
            self.selected_files_text.value = f'{self.selected_file.name}'
            self.selected_files_text.update()
        else:
            print("Error no file")
