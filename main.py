from customtkinter import CTkLabel

from components import AppLayout, Button, Console, URLInputBox, DirDialog
from constant import GLOBAL_PADDING_Y, GLOBAL_PADDING_X, GLOBAL_COLUMN_SPAN
from utils import onclick_download

layout = AppLayout(title="YouTube Audio Downloader")
layout.set_column_config((0, 1), 1)
app = layout.app

title = CTkLabel(app, text="YouTube Audio Downloader", fg_color="transparent")
title.grid(row=0, column=0, pady=(GLOBAL_PADDING_Y, 0), columnspan=GLOBAL_COLUMN_SPAN)

url_input_box = URLInputBox(app, row=1, column_span=GLOBAL_COLUMN_SPAN)
dir_dialog = DirDialog(app, row=2, column_span=GLOBAL_COLUMN_SPAN)
console = Console(app, row=3, column_span=GLOBAL_COLUMN_SPAN)
download_button = Button(app, text="Download", row=4, column=0, column_span=GLOBAL_COLUMN_SPAN,
                         padding_x=GLOBAL_PADDING_X, padding_y=GLOBAL_PADDING_Y, button_color="green",
                         command=lambda: onclick_download(url_input_box,
                                                          console,
                                                          download_button,
                                                          dir_dialog))

layout.start()
