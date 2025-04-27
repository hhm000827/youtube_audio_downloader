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
    file_picker: ft.FilePicker = field(default=None)

    def __attrs_post_init__(self):
        super().__init__()
        self.entry = ft.TextField(label=self.label_text, value=self.path, width=400, read_only=True, border_color=ft.Colors.WHITE)
        self.button = Button("Browse", command=self.browse, bg_color=ft.Colors.BLUE_700, text_color=ft.Colors.WHITE)
        self.controls=[self.entry, self.button]

    def set_file_picker(self, file_picker):
        self.file_picker = file_picker

    def browse(self, e=None):
        if not self.file_picker:
            logger.error("FilePicker not set!")
            return
        def on_result(e: ft.FilePickerResultEvent):
            if e.path:
                self.path = e.path
                self.entry.value = self.path
                self.entry.update()
        self.file_picker.on_result = on_result
        self.file_picker.get_directory_path()

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
