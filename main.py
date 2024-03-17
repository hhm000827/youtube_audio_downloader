import threading

from customtkinter import CTkLabel

from components import AppLayout, TextBox, Button
from utils import download_youtube_mp3


def onclick_download(textbox, console, button):
    console.clear_textbox()
    textbox.is_enable_textbox(False)
    button.is_enabled(False)
    text = textbox.read_urls()
    threading.Thread(target=download_youtube_mp3, args=(console, text, textbox, button)).start()


layout = AppLayout(title="YouTube MP3 Downloader")
app = layout.app

title = CTkLabel(app, text="YouTube MP3 Downloader", fg_color="transparent")
title.grid(row=0, column=0, pady=(20, 0), sticky="ew", columnspan=2)

youtube_urls_textbox = TextBox(app, label_text="Youtube URLs:", label_row=1, label_padding_x=20, textbox_padding_x=20,
                               column_span=2)

output_console = TextBox(app, label_text="Console:", label_row=3, label_padding_x=20, textbox_padding_x=20,
                         column_span=2)

output_console.is_enable_textbox(True)

download_button = Button(app, text="Download", row=5, column=0, padding_x=20, padding_y=20, column_span=2, sticky="ew",
                         command=lambda: onclick_download(youtube_urls_textbox, output_console, download_button))

layout.set_column_config((0, 1), 1)
layout.start()
