import threading

from jobs import start_download_audio


def onclick_download(textbox, console, download_button):
    __lock_components(console, textbox, download_button)
    urls = __read_urls(console, textbox)
    threading.Thread(target=start_download_audio, args=(console, urls)).start()
    __unlock_components(textbox, download_button)


def __lock_components(console, textbox, download_button):
    console.clear()
    textbox.is_enable(False)
    download_button.is_enabled(False)


def __read_urls(console, textbox) -> list[str]:
    console.insert("Downloaded audio will be stored in output directory")
    console.insert(f"Start reading URLs...")
    urls = textbox.read_urls()
    console.insert(f"There are {len(urls)} URLs, start downloading...")
    return urls


def __unlock_components(textbox, download_button):
    textbox.is_enable(True)
    download_button.is_enabled(True)
