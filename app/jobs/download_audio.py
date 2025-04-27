import asyncio
from concurrent.futures import ThreadPoolExecutor
import os

from pytubefix import YouTube, Playlist
from pytubefix.cli import on_progress
from rich.progress import Progress

from app.constant import MOVIE_MUSIC
from app.utils.logger import Logger

logger = Logger().logger

def __download(url, console, task_id, progress, out_dir_path, audio_type):
    yt = YouTube(url.strip(), on_progress_callback=on_progress)
    audio = yt.streams.get_audio_only()
    try:
        out_file = audio.download(output_path=out_dir_path)
        if audio_type == "mp3":
            mp3_path = out_file.replace('.m4a', '.mp3')
            os.rename(out_file, mp3_path)
        console.insert("Downloaded: " + audio.title)
    except Exception as e:
        logger.error(f"Failed to download video from {url}. Error: {str(e)}")
        console.insert(f"Failed to download video from {url}. Error: {str(e)}")
    finally:
        progress.update(task_id, advance=1)


def __download_from_playlist(url, console, task_id, progress, out_dir_path, audio_type):
    pl = Playlist(url)
    videos = list(pl.videos)
    logger.info(f"Found {len(videos)} videos in playlist {pl.title}")
    console.insert(f"Found {len(videos)} videos in playlist {pl.title}")
    for video in videos:
        try:
            ys = video.streams.get_audio_only()
            out_file = ys.download(output_path=out_dir_path)
            if audio_type == "mp3":
                mp3_path = out_file.replace('.m4a', '.mp3')
                os.rename(out_file, mp3_path)
            console.insert("Downloaded: " + ys.title)
        except Exception as e:
            logger.error(f"Failed to download video from {url}. Error: {str(e)}")
            console.insert(f"Failed to download video from {url}. Error: {str(e)}")
    progress.update(task_id, advance=1)


async def __download_all(loop, urls, console, out_dir_path, url_type, audio_type):
    with ThreadPoolExecutor() as executor, Progress() as progress:
        task_id = progress.add_task("Downloading...", total=len(urls))
        download_func = __download if url_type == MOVIE_MUSIC else __download_from_playlist
        tasks = [
            loop.run_in_executor(executor, download_func, url, console, task_id, progress, out_dir_path, audio_type)
            for url in urls
        ]
        await asyncio.gather(*tasks)
    logger.info("All downloads are finished")
    console.insert("All downloads are finished")


def start_download_audio(console, urls, out_dir_path, url_type, audio_type):
    console.insert("Start downloading...")
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(__download_all(loop, urls, console,
                                           out_dir_path, url_type, audio_type))
