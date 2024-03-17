from tkinter import END

import customtkinter
from attr import define, field
from customtkinter import CTkLabel, CTkTextbox

from utils import Logger

logger = Logger().logger


@define
class TextBox:
    app: customtkinter.CTk = field(default=customtkinter.CTk())
    label: customtkinter.CTkLabel = field(init=False)
    textbox: customtkinter.CTkTextbox = field(init=False)
    label_text: str = field(default="TextBox")
    label_row: int = field(default=0)
    label_padding_x: int | tuple = field(default=0)
    label_padding_y: int | tuple = field(default=0)
    textbox_padding_x: int | tuple = field(default=0)
    textbox_padding_y: int | tuple = field(default=0)
    column_span: int = field(default=1)

    def __attrs_post_init__(self):
        self.label = CTkLabel(self.app, text=self.label_text, fg_color="transparent")
        self.label.grid(row=self.label_row, column=0,
                        padx=self.label_padding_x, pady=self.label_padding_y,
                        sticky="w", columnspan=self.column_span)

        self.textbox = CTkTextbox(self.app)
        self.textbox.grid(row=self.label_row + 1, column=0, padx=self.textbox_padding_x,
                          pady=self.textbox_padding_y,
                          sticky="ew", columnspan=self.column_span)

    def read_urls(self):
        text = self.textbox.get("0.0", "end")  # get text from line 0 character 0 till the end
        logger.info(f"Read URLs:\n{text}")
        return text

    def is_enable_textbox(self, enable=True):
        self.textbox.configure(state="normal" if enable else "disabled")

    def insert(self, text):
        logger.info(f"Insert:\n{text}")
        self.textbox.insert(END, text + "\n")

    def clear_textbox(self):
        self.textbox.delete("0.0", "end")
