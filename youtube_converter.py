import threading
from pathlib import Path

from pytube import YouTube


def instruction():
    print("Designed by hhm000827. All rights reserved.")
    print("------------------------------")
    print("Put everything in prepare.txt")
    print("First line must be storing mp3 path")
    print("Another lines must be youtube URL (one line one URL)")
    print("------------------------------")
    input("Click Enter to confirm:")


def youtube_convert_to_mp3(url, target_path):
    if not url.startswith("https://youtu.be/"):
        print("This is not URL:", url)
        return
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first()
    out_file = target_path / (yt.title.replace("/", " ").replace("\\", " ") + ".mp3")
    if out_file.exists():
        print(out_file, "already exists!")
        return
    try:
        video.download(output_path=target_path, filename=yt.title.replace("/", " ").replace("\\", " ") + ".mp3")
        print(out_file, "has been successfully downloaded.")
    except Exception as e:
        print(e)
        return


def main():
    a = instruction()
    if not a:
        print("Start Convert youtube video to mp3")
        with open('prepare.txt') as f:
            text = f.read()
            lines = text.split("\n")
            target_path = Path(lines[0])
            if not target_path.is_dir():
                print("This is not path! Please correct it and try again.")
                return
            urls = [url for url in lines[1:] if url.startswith("https://youtu.be/")]
            threads = []
            for url in urls:
                t = threading.Thread(target=youtube_convert_to_mp3, args=(url, target_path))
                threads.append(t)
                t.start()

            for t in threads:
                t.join()
        input("All done! Click Enter to end program.")
    else:
        input("not confirm! Click Enter to end program.")


if __name__ == '__main__':
    main()
