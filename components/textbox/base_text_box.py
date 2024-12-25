from abc import ABC, abstractmethod

import customtkinter
from attrs import define, field
from customtkinter import CTkLabel, CTkTextbox

from utils import Logger

logger = Logger().logger


@define
class BaseTextBox(ABC):
    app: customtkinter.CTk = field(default=customtkinter.CTk())
    label: customtkinter.CTkLabel = field(init=False)
    textbox: customtkinter.CTkTextbox = field(init=False)
    label_text: str = field(default="", init=False)
    label_row: int = field(default=0)
    label_padding_x: int | tuple = field(default=0)
    label_padding_y: int | tuple = field(default=0)
    textbox_padding_x: int | tuple = field(default=0)
    textbox_padding_y: int | tuple = field(default=0)
    column_span: int = field(default=1)

    @abstractmethod
    def __attrs_post_init__(self):
        self.label = CTkLabel(self.app, text=self.label_text, fg_color="transparent")
        self.label.grid(row=self.label_row, column=0,
                        padx=self.label_padding_x, pady=self.label_padding_y,
                        sticky="w", columnspan=self.column_span)

        self.textbox = CTkTextbox(self.app)
        self.textbox.grid(row=self.label_row + 1, column=0, padx=self.textbox_padding_x,
                          pady=self.textbox_padding_y,
                          sticky="ew", columnspan=self.column_span)
