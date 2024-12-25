from tkinter import END

from attr import define, field

from utils import Logger
from .base_text_box import BaseTextBox

logger = Logger().logger


@define
class Console(BaseTextBox):
    label_text: str = field(default="Console:", init=False)

    def __attrs_post_init__(self):
        super().__attrs_post_init__()
        self.textbox.configure(state="disabled")

    def insert(self, text):
        self.textbox.configure(state="normal")
        logger.info(f"Insert:\n{text}")
        self.textbox.insert(END, text + "\n")
        self.textbox.configure(state="disabled")

    def clear(self):
        self.textbox.delete("0.0", "end")
