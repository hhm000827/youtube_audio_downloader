import flet as ft
from attr import define, field

@define
class Button(ft.ElevatedButton):
    text_value: str = field(default="Button")
    command: callable = field(default=None)
    bg_color: str = field(default=ft.Colors.GREEN_700)
    text_color: str = field(default=ft.Colors.WHITE)

    def __attrs_post_init__(self):
        super().__init__()
        self.text=self.text_value
        self.on_click=self.command
        self.bgcolor=self.bg_color
        self.color=self.text_color

    def is_enabled(self, enable=True):
        self.disabled = not enable
        self.bgcolor = self.bg_color if enable else ft.Colors.GREY_700
        self.update()
