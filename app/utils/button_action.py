import threading

from pydash import is_empty

from app.jobs import start_download_audio


def onclick_download(url_input_box, console, download_button, dir_dialog, url_source_option, audio_type_dropdown):
    console.clear()
    
    url_type = url_source_option.get_option()
    out_dir_path = dir_dialog.get_path()
    urls = __read_urls(console, url_input_box)
    audio_type = audio_type_dropdown.get_option()
    
    is_valid = validate(console, audio_type, url_type, out_dir_path, urls)
    if is_valid:
        __set_components_enabled(url_input_box, download_button, dir_dialog, url_source_option, audio_type_dropdown, False)
        def run_download():
            start_download_audio(console, urls, out_dir_path, url_type, audio_type)
            __set_components_enabled(url_input_box, download_button, dir_dialog, url_source_option, audio_type_dropdown, True)
        t = threading.Thread(target=run_download)
        t.start()

def validate(console, audio_type, url_type, out_dir_path, urls):
    is_valid = True
    if is_empty(urls):
        console.insert("No URLs found, please insert URLs")
        is_valid = False
    if is_empty(out_dir_path):
        console.insert("No output directory found, please select an output directory")
        is_valid = False
    if is_empty(url_type):
        console.insert("No URL type found, please select a URL type")
        is_valid = False
    if is_empty(audio_type):
        console.insert("No audio type found, please select an audio type")
        is_valid = False
    return is_valid


def __set_components_enabled(urls_input_box, download_button, dir_dialog, url_source_option, audio_type_dropdown, enabled):
    url_source_option.is_enabled(enabled)
    urls_input_box.is_enabled(enabled)
    dir_dialog.is_enabled(enabled)
    download_button.is_enabled(enabled)
    audio_type_dropdown.is_enabled(enabled)


def __read_urls(console, textbox) -> list[str]:
    urls = textbox.read_urls()
    console.insert(f"There are {len(urls)} URLs found")
    return urls
