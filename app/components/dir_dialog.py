from tkinter import filedialog

import customtkinter
from attrs import define, field
from customtkinter import CTkEntry, CTkLabel, CTkFrame

from app.constant import GLOBAL_PADDING_X, GLOBAL_PADDING_Y, OUTPUT_DIR
from app.utils import Logger
from .button import Button

logger = Logger().logger


@define
class DirDialog(CTkFrame):
    app: customtkinter.CTk | CTkFrame = field(default=customtkinter.CTk())
    row: int = field(default=0)
    column_span: int = field(default=1)
    button: Button = field(init=False)
    entry: CTkEntry = field(init=False)
    file_dialog: filedialog = field(default=filedialog, init=False)
    label: CTkLabel = field(init=False)
    label_text: str = field(default="Output Directory:", init=False)

    def __attrs_post_init__(self):
        super().__init__(master=self.app, fg_color="transparent")
        self.grid_columnconfigure(0, weight=1)
        self.label = CTkLabel(self, text=self.label_text)
        self.label.grid(row=0, column=0, sticky="w")
        self.entry = CTkEntry(self, state="disabled", width=500)
        self.entry.grid(row=1, column=0, sticky="ew", padx=(0, GLOBAL_PADDING_X))
        self.button = Button(self, text="Browse", row=1, column=1, command=self.__browse, sticky="w")
        self.grid(row=self.row, column=0, columnspan=self.column_span, padx=GLOBAL_PADDING_X, pady=GLOBAL_PADDING_Y,
                  sticky="ew")

    def __browse(self):
        pass
        self.entry.configure(state="normal")
        self.entry.delete(0, "end")
        path = self.file_dialog.askdirectory(title="Select Output Directory", initialdir=OUTPUT_DIR,
                                             mustexist=True)
        if not path:
            path = OUTPUT_DIR

        self.entry.insert(0, path)
        self.entry.configure(state="disabled")

    def get_path(self):
        path = self.entry.get() if self.entry.get() else OUTPUT_DIR
        logger.info(f"Output directory: {path}")
        return path
