import asyncio
import os
from concurrent.futures import ThreadPoolExecutor

from pytube import YouTube

from .logger import Logger

logger = Logger().logger


def download_youtube_audio(url, console):
    try:
        yt = YouTube(url.strip())
        video = yt.streams.filter(only_audio=True).first()

        out_file = video.download(output_path='./output')

        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)

        console.insert(yt.title + " has been successfully downloaded.")
    except Exception as e:
        console.insert(f"Failed to download video from {url}. Error: {str(e)}")


def download_youtube_mp3(console, raw_urls, textbox, download_button):
    console.insert("Downloaded MP3 will be stored in output directory")
    console.insert(f"Read URLs...\n{raw_urls}")

    urls = raw_urls.split("\n")
    urls = [item for item in urls if item != ""]

    logger.info(urls)

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    with ThreadPoolExecutor() as executor:
        tasks = [loop.run_in_executor(executor, download_youtube_audio, url, console) for url in urls]
        loop.run_until_complete(asyncio.gather(*tasks))

    textbox.is_enable(True)
    download_button.is_enabled(True)
