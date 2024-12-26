import customtkinter
from attrs import define, field
from customtkinter import CTkComboBox, CTkFrame, CTkLabel

from constant import GLOBAL_PADDING_X, GLOBAL_PADDING_Y
from utils import Logger

logger = Logger().logger


@define
class ComboBox(CTkFrame):
    app: customtkinter.CTk | CTkFrame = field(default=customtkinter.CTk())
    combobox: CTkComboBox = field(init=False)
    Label: CTkLabel = field(init=False)
    label_text: str = field(default="ComboBox:")
    options: list[str] = field(default=["Option 1", "Option 2", "Option 3"])
    row: int = field(default=0)
    column: int = field(default=0)
    column_span: int = field(default=1)

    def __attrs_post_init__(self):
        super().__init__(master=self.app, fg_color="transparent")
        self.grid_columnconfigure(0, weight=1)

        self.Label = CTkLabel(self, text=self.label_text)
        self.Label.grid(row=0, column=0, sticky="w")

        combobox_var = customtkinter.StringVar(value=self.options[0])
        self.combobox = CTkComboBox(self, values=self.options, variable=combobox_var)
        self.combobox.grid(row=1, column=0, columnspan=self.column_span, sticky="w")

        self.grid(row=self.row, column=self.column, columnspan=self.column_span, padx=GLOBAL_PADDING_X,
                  pady=GLOBAL_PADDING_Y, sticky="ew")

    def is_enable(self, is_enable: bool = True):
        self.combobox.configure(state="normal" if is_enable else "disabled")

    def get_option(self):
        option = self.combobox.get()
        logger.info(f"Current option: {option}")
        return option
