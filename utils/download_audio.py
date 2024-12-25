import asyncio
from concurrent.futures import ThreadPoolExecutor

from pytubefix import YouTube
from pytubefix.cli import on_progress
from rich.progress import Progress

from constant import OUTPUT_DIR
from .logger import Logger

logger = Logger().logger


def download(url, console, task_id, progress):
    yt = YouTube(url.strip(), on_progress_callback=on_progress)
    audio = yt.streams.get_audio_only()

    try:
        audio.download(output_path=OUTPUT_DIR)
        console.insert("Downloaded: " + audio.title)
    except Exception as e:
        logger.error(f"Failed to download video from {url}. Error: {str(e)}")
        console.insert(f"Failed to download video from {url}. Error: {str(e)}")
    finally:
        progress.update(task_id, advance=1)


async def download_all(loop, urls, console):
    with ThreadPoolExecutor() as executor:
        with Progress() as progress:
            task_id = progress.add_task("Downloading...", total=len(urls))
            tasks = [loop.run_in_executor(executor, download, url, console, task_id, progress) for url in urls]
            await asyncio.gather(*tasks)


def start_download_audio(console, textbox, download_button):
    console.clear()
    textbox.is_enable(False)
    download_button.is_enabled(False)

    console.insert("Downloaded audio will be stored in output directory")
    console.insert(f"Start reading URLs...")
    urls = textbox.read_urls()
    console.insert(f"There are {len(urls)} URLs, start downloading...")

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(download_all(loop, urls, console))

    textbox.is_enable(True)
    download_button.is_enabled(True)
