from abc import ABC, abstractmethod

import customtkinter
from attrs import define, field
from customtkinter import CTkLabel, CTkTextbox, CTkFrame

from app.constant import GLOBAL_PADDING_X, GLOBAL_PADDING_Y
from app.utils import Logger

logger = Logger().logger


@define
class BaseTextBox(ABC, CTkFrame):
    app: customtkinter.CTk | CTkFrame = field(default=customtkinter.CTk())
    row: int = field(default=0)
    column_span: int = field(default=1)
    label: customtkinter.CTkLabel = field(init=False)
    textbox: customtkinter.CTkTextbox = field(init=False)
    label_text: str = field(default="", init=False)

    @abstractmethod
    def __attrs_post_init__(self):
        super().__init__(master=self.app, fg_color="transparent")
        self.grid_columnconfigure(0, weight=1)

        self.label = CTkLabel(self, text=self.label_text, fg_color="transparent")
        self.label.grid(row=0, column=0, sticky="w")

        self.textbox = CTkTextbox(self)
        self.textbox.grid(row=1, column=0, sticky="nsew")

        self.grid(row=self.row, column=0, columnspan=self.column_span, padx=GLOBAL_PADDING_X, pady=GLOBAL_PADDING_Y,
                  sticky="nsew")
