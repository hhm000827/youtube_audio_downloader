import threading

from pydash import is_empty

from constant import OUTPUT_DIR
from jobs import start_download_audio
from .logger import Logger

logger = Logger().logger


def onclick_download(textbox, console, download_button, dir_dialog):
    __lock_components(console, textbox, download_button, dir_dialog)
    out_dir_path = dir_dialog.entry.get() if dir_dialog.entry.get() else OUTPUT_DIR
    logger.info(f"Output directory: {out_dir_path}")
    urls = __read_urls(console, textbox, out_dir_path)
    if is_empty(urls):
        console.insert("No URLs found, please insert URLs")
    else:
        threading.Thread(target=start_download_audio, args=(console, urls, out_dir_path)).start()
    __unlock_components(textbox, download_button, dir_dialog)


def __lock_components(console, urls_input_box, download_button, dir_dialog):
    console.clear()
    urls_input_box.is_enable(False)
    urls_input_box.clear_button.is_enabled(False)
    dir_dialog.button.is_enabled(False)
    download_button.is_enabled(False)


def __read_urls(console, textbox, out_dir_path) -> list[str]:
    console.insert(f"Downloaded audio will be stored in {out_dir_path}")
    console.insert(f"Start reading URLs...")
    urls = textbox.read_urls()
    console.insert(f"There are {len(urls)} URLs found")
    return urls


def __unlock_components(textbox, download_button, dir_dialog):
    textbox.is_enable(True)
    textbox.clear_button.is_enabled(True)
    dir_dialog.button.is_enabled(True)
    download_button.is_enabled(True)
