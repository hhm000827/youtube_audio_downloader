from customtkinter import CTkLabel

from components import AppLayout, Button, Console, URLInputBox, DirDialog
from constant import GLOBAL_PADDING_Y, GLOBAL_PADDING_X, GLOBAL_COLUMN_SPAN
from utils import onclick_download, onclick_clear

layout = AppLayout(title="YouTube Audio Downloader")
layout.set_column_config((0, 1), 1)
app = layout.app

title = CTkLabel(app, text="YouTube Audio Downloader", fg_color="transparent")
title.grid(row=0, column=0, pady=(GLOBAL_PADDING_Y, 0), columnspan=GLOBAL_COLUMN_SPAN)

url_input_box = URLInputBox(app, label_row=1, label_padding_x=GLOBAL_PADDING_X, textbox_padding_x=GLOBAL_PADDING_X,
                            column_span=GLOBAL_COLUMN_SPAN)

clear_button = Button(app, text="Clear", row=3, column=0, column_span=GLOBAL_COLUMN_SPAN,
                      padding_x=GLOBAL_PADDING_X, padding_y=(GLOBAL_PADDING_Y / 2, GLOBAL_PADDING_Y), sticky="w",
                      command=lambda: onclick_clear(url_input_box))

dir_dialog = DirDialog(app, row=4, column_span=GLOBAL_COLUMN_SPAN)

console = Console(app, label_row=6, label_padding_x=GLOBAL_PADDING_X,
                  textbox_padding_x=GLOBAL_PADDING_X, column_span=GLOBAL_COLUMN_SPAN)

download_button = Button(app, text="Download", row=8, column=0, column_span=GLOBAL_COLUMN_SPAN,
                         padding_x=GLOBAL_PADDING_X, padding_y=GLOBAL_PADDING_Y, button_color="green",
                         command=lambda: onclick_download(url_input_box,
                                                          console,
                                                          download_button,
                                                          clear_button))

layout.start()
