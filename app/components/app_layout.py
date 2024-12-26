import customtkinter
from attr import define, field
from customtkinter import CTk


@define(frozen=True)
class AppLayout:
    app: CTk = field(default=customtkinter.CTk(), init=False)
    title: str = field(default="CustomTkinter App")
    geometry: str = field(default="900x730")
    appearance_mode: str = field(default="dark")
    color_theme: str = field(default="dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

    def __attrs_post_init__(self):
        self.app.title(self.title)
        self.app.geometry(self.geometry)
        self.app.grid_columnconfigure(0, weight=1)
        customtkinter.set_appearance_mode(self.appearance_mode)
        customtkinter.set_default_color_theme(self.color_theme)

    def set_column_config(self, column: int | tuple, weight: int):
        self.app.grid_columnconfigure(column, weight=weight)

    def set_row_config(self, row: int | tuple, weight: int):
        self.app.grid_rowconfigure(row, weight=weight)

    def start(self):
        self.app.mainloop()
