import flet as ft
from attr import define, field
from app.utils import Logger
from .button import Button

logger = Logger().logger

@define
class DirDialog(ft.Row):
    label_text: str = field(default="Output Directory:")
    path: str = field(default="")
    entry: ft.TextField = field(init=False)
    button: Button = field(init=False)
    file_picker: ft.FilePicker = field(init=False)

    def __attrs_post_init__(self):
        super().__init__()

        self.file_picker = ft.FilePicker(on_result=self.__on_picker_result)

        self.entry = ft.TextField(label=self.label_text, value=self.path, width=400, read_only=True, border_color=ft.Colors.WHITE)
        self.button = Button("Browse", command=lambda e: self.file_picker.get_directory_path(dialog_title="Select Download Directory"),
                             bg_color=ft.Colors.BLUE_700, text_color=ft.Colors.WHITE)
        self.controls=[self.entry, self.button]

    def get_file_picker(self):
        return self.file_picker

    def __on_picker_result(self, e: ft.FilePickerResultEvent):
        if e.path:
            self.path = e.path
            self.entry.value = self.path
            self.entry.update()
            logger.info(f"Directory selected: {self.path}")
        else:
            logger.info("No directory selected")

    def get_path(self):
        path = self.entry.value
        logger.info(f"Output directory: {path}")
        return path

    def is_enabled(self, enable=True):
        self.entry.disabled = not enable
        self.button.disabled = not enable
        self.button.bgcolor = ft.Colors.BLUE_700 if enable else ft.Colors.GREY_700
        self.entry.update()
        self.button.update()
