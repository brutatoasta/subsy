from pathlib import Path

from pytube import YouTube

# chinese video
link = "https://www.youtube.com/watch?v=DtncJJR5W50"


def download(stream):
    # download audio to downloads folder with some basic info
    try:
        yt = YouTube(link)
        output_path = Path("downloads") / Path(yt.title)
        # ensure output directory exists
        if not output_path.is_dir():
            output_path.mkdir()
        stream = yt.streams.filter(only_audio=True).first()
        txt_file = output_path / Path(f"{yt.title}.txt")
        with open(txt_file, mode="x", encoding="utf-8") as f:
            f.write(f"Title: {yt.title}\n")
            f.write(f"Author: {yt.author}\n")
            f.write(f"Date: {yt.publish_date}\n")
            f.write(f"Description: {yt.description}\n")
        return (
            stream.download(
                output_path=output_path, filename=f"{stream.title.strip()}.mp4"
            ),
            txt_file,
        )
    except:
        raise


if __name__ == "__main__":
    download()
