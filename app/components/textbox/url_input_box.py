import flet as ft
from attr import define, field
from pydash import is_blank
from app.utils import Logger

logger = Logger().logger

@define
class URLInputBox(ft.Row):
    label_text: str = field(default="Youtube URLs:")
    textbox: ft.TextField = field(init=False)
    clear_button: ft.ElevatedButton = field(init=False)

    def __attrs_post_init__(self):
        super().__init__()
        self.textbox = ft.TextField(
            multiline=True,
            min_lines=3,
            max_lines=5,
            width=500,
            label=self.label_text,
            border_color=ft.Colors.WHITE
        )
        self.clear_button = ft.ElevatedButton("Clear", on_click=self.clear, bgcolor=ft.Colors.RED_700, color=ft.Colors.WHITE)
        self.spacing=8
        self.alignment=ft.MainAxisAlignment.START
        self.controls=[self.textbox, self.clear_button]

    def read_urls(self):
        import validators
        text = self.textbox.value or ""
        urls = [item.strip() for item in text.split("\n") if not is_blank(item.strip()) and validators.url(item.strip())]
        logger.info(f"There are {len(urls)} valid URLs")
        return urls

    def is_enabled(self, enable=True):
        self.textbox.disabled = not enable
        self.clear_button.disabled = not enable
        self.clear_button.bgcolor = ft.Colors.RED_700 if enable else ft.Colors.GREY_700
        self.textbox.update()
        self.clear_button.update()

    def clear(self, e=None):
        self.textbox.value = ""
        self.textbox.update()
