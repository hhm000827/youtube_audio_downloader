import flet as ft
from app.components import Dropdown
from app.components.textbox.url_input_box import URLInputBox
from app.components.textbox.console import Console
from app.components.dir_dialog import DirDialog
from app.components.button import Button
from app.constant import MOVIE_MUSIC, PLAYLIST, AUDIO_TYPES
from app.utils import onclick_download

def main(page: ft.Page):
    page.title = "YouTube Audio Downloader"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = ft.Colors.BLACK
    page.window.maximized = True

    # Instantiate components
    url_source_option = Dropdown(label_text="URL Type:", options_values=[MOVIE_MUSIC, PLAYLIST])
    audio_type_dropdown = Dropdown(label_text="Audio Type:", options_values=AUDIO_TYPES)
    url_input_box = URLInputBox()
    dir_dialog = DirDialog()
    console = Console()
    download_button = Button(text_value="Download", bg_color=ft.Colors.GREEN_700, text_color=ft.Colors.WHITE)

    # Add the DirDialog's FilePicker to the page overlay
    page.overlay.append(dir_dialog.get_file_picker())

    # Build UI widgets
    title = ft.Text(
        "YouTube Audio Downloader",
        size=32,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.WHITE,
        text_align=ft.TextAlign.CENTER,
    )

    # Main card content
    card_content = ft.Column([
        title,
        ft.Row([url_source_option,audio_type_dropdown], spacing=20, alignment=ft.MainAxisAlignment.START),
        url_input_box,
        dir_dialog,
        ft.Divider(height=30, color="rgba(255,255,255,0.08)"),
        console,
        ft.Row([
            ft.Container(expand=True),
            download_button
        ], alignment=ft.MainAxisAlignment.END)
    ],
        spacing=20,
        horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
    )

    main_card = ft.Container(
        content=card_content,
        padding=30,
        border_radius=20,
        bgcolor="rgba(255,255,255,0.03)",
        shadow=ft.BoxShadow(
            spread_radius=2,
            blur_radius=16,
            color="rgba(0,0,0,0.4)",
            offset=ft.Offset(0, 8),
        ),
        width=800,
    )

    def on_download(e):
        onclick_download(url_input_box, console, download_button, dir_dialog, url_source_option, audio_type_dropdown)

    download_button.on_click = on_download

    # Center the card both vertically and horizontally
    page.add(
        ft.Row([
            ft.Container(
                main_card,
                alignment=ft.alignment.center,
                expand=False
            )
        ], alignment=ft.MainAxisAlignment.CENTER, vertical_alignment=ft.CrossAxisAlignment.CENTER)
    )

ft.app(target=main)
