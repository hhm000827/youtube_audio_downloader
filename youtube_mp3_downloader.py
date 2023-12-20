import os
from concurrent.futures import ThreadPoolExecutor

from pytube import YouTube


def download_youtube_audio(url, destination='.'):
    try:
        yt = YouTube(url.strip())
        video = yt.streams.filter(only_audio=True).first()

        out_file = video.download(output_path=destination)

        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)

        print(yt.title + " has been successfully downloaded.")
    except Exception as e:
        print(f"Failed to download video from {url}. Error: {str(e)}")


def main():
    print("This application will read urls from urls.txt and download the audio from YouTube.")
    print("Enter the destination for downloaded audio files (leave blank for current directory)")
    destination = input(">> ") or '.'

    with open('urls.txt', 'r') as f:
        urls = f.readlines()

    with ThreadPoolExecutor(max_workers=5) as executor:
        for url in urls:
            executor.submit(download_youtube_audio, url, destination)


if __name__ == "__main__":
    main()
