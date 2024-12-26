import customtkinter
from attr import define, field


@define()
class Button:
    button: customtkinter.CTkButton = field(init=False)
    app: customtkinter.CTk = field(default=customtkinter.CTk())
    text: str = field(default="Button")
    command: callable = field(default=lambda: print("Button clicked"))
    row: int = field(default=0)
    column: int = field(default=0)
    padding_x: int | tuple = field(default=0)
    padding_y: int | tuple = field(default=0)
    sticky: str = field(default="")
    column_span: int = field(default=1)
    button_color: str = field(default="blue")

    def __attrs_post_init__(self):
        self.button = customtkinter.CTkButton(self.app, text=self.text, command=self.command,
                                              fg_color=self.button_color)
        self.button.grid(row=self.row, column=self.column, padx=self.padding_x, pady=self.padding_y,
                         sticky=self.sticky, columnspan=self.column_span)

    def is_enabled(self, enable=True):
        self.button.configure(state="normal" if enable else "disabled")
