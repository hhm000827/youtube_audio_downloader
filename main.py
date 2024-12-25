import threading

from customtkinter import CTkLabel

from components import AppLayout, Button, Console, URLInputBox
from utils import download_youtube_mp3

GLOBAL_PADDING_X = 20
GLOBAL_PADDING_Y = 20


def onclick_download(textbox, console, button):
    console.clear()
    textbox.is_enable(False)
    button.is_enabled(False)
    text = textbox.read_urls()
    threading.Thread(target=download_youtube_mp3, args=(console, text, textbox, button)).start()


layout = AppLayout(title="YouTube MP3 Downloader")
layout.set_column_config(0, 1)
app = layout.app

title = CTkLabel(app, text="YouTube MP3 Downloader", fg_color="transparent")
title.grid(row=0, column=0, pady=(GLOBAL_PADDING_Y, 0))

url_input_box = URLInputBox(app, label_row=1, label_padding_x=GLOBAL_PADDING_X, textbox_padding_x=GLOBAL_PADDING_X)

console = Console(app, label_row=3, label_padding_x=GLOBAL_PADDING_X, textbox_padding_x=GLOBAL_PADDING_X)

download_button = Button(app, text="Download", row=5, column=0, padding_x=GLOBAL_PADDING_X, padding_y=GLOBAL_PADDING_Y,
                         command=lambda: onclick_download(url_input_box, console, download_button))

layout.start()
