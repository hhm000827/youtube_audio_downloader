import flet as ft
from attr import define, field
from app.utils import Logger

logger = Logger().logger

@define
class Dropdown(ft.Dropdown):
    label_text: str = field(default="ComboBox:")
    options_values: list = field(default=["Option 1", "Option 2", "Option 3"])

    def __attrs_post_init__(self):
        super().__init__()
        self.label=self.label_text
        self.options=[ft.dropdown.Option(opt) for opt in self.options_values]
        self.width=300
        self.border_color=ft.Colors.WHITE

    def get_option(self):
        return self.value

    def is_enabled(self, enable=True):
        self.disabled = not enable
        self.update()
