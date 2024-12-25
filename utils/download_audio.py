import asyncio
from concurrent.futures import ThreadPoolExecutor

from pytubefix import YouTube
from pytubefix.cli import on_progress

from constant import OUTPUT_DIR
from .logger import Logger

logger = Logger().logger


def download(url, console):
    yt = YouTube(url.strip(), on_progress_callback=on_progress)
    audio = yt.streams.get_audio_only()

    try:
        audio.download(output_path=OUTPUT_DIR)
        console.insert(audio.title + " has been successfully downloaded.")
    except Exception as e:
        console.insert(f"Failed to download video from {url}. Error: {str(e)}")


def start_download_audio(console, textbox, download_button):
    console.clear()
    textbox.is_enable(False)
    text = textbox.read_urls()
    download_button.is_enabled(False)

    console.insert("Downloaded MP3 will be stored in output directory")
    console.insert(f"Read URLs...\n{text}")

    urls = text.split("\n")
    urls = [item for item in urls if item != ""]

    logger.info(urls)

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    with ThreadPoolExecutor() as executor:
        tasks = [loop.run_in_executor(executor, download, url, console) for url in urls]
        loop.run_until_complete(asyncio.gather(*tasks))

    textbox.is_enable(True)
    download_button.is_enabled(True)
