import flet as ft
from attr import define, field
from app.utils import Logger

logger = Logger().logger

@define
class Console(ft.TextField):
    label_text: str = field(default="Console")

    def __attrs_post_init__(self):
        super().__init__()
        self.label=self.label_text
        self.multiline=True
        self.min_lines=10
        self.max_lines=10
        self.width=500
        self.read_only=True
        self.selectable=True
        self.border_color=ft.Colors.WHITE

    def insert(self, text):
        self.value = (self.value or "") + text + "\n"
        self.update()

    def clear(self):
        self.value = ""
        self.update()

    def is_enabled(self, enable=True):
        self.disabled = not enable
        self.update()
