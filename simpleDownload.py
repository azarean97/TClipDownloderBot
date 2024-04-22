import yt_dlp

def download_video(url, quality, save_path):
    ydl_opts = {
        'format': quality,
        'outtmpl': save_path,
        'merge_output_format': 'mp4'
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(url)

'''
In yt-dlp, quality format options allow you to specify the desired quality of the video/audio that you want to download. These options control parameters such as video resolution, video and audio codecs, and file format. Here are some common quality format options that you can use:

-f, --format FORMAT: This option allows you to specify the format of the video/audio to download. You can specify a specific format code or a format specifier. For example, 'best' will download the best quality available, 'worst' will download the worst quality available, and 'bestvideo+bestaudio' will download the best video and audio separately and then merge them.
--format-sort SORT_ORDER: This option allows you to specify the sort order for formats. Available values are 'filesize', 'abr' (audio bitrate), 'res' (resolution), 'fps' (frames per second), 'tbr' (video bitrate), 'width', 'height', 'channels', 'vcodec' (video codec), 'acodec' (audio codec), 'format_id' (format ID), 'format' (extension), and 'ext' (extension).
--format-selection FORMAT_SELECTION: This option allows you to specify the conditions for format selection. You can use expressions like 'best', 'bestvideo[height<=720]+bestaudio/best[height<=720]', etc.
-q, --quality LEVEL: This option allows you to specify the quality level of the video/audio. Available values are '0' (worst) to '9' (best). This option is mainly used for selecting the preferred quality when multiple formats are available.
--max-quality LEVEL: This option allows you to specify the maximum quality level of the video/audio. Formats above this quality level will not be considered for download.
--min-quality LEVEL: This option allows you to specify the minimum quality level of the video/audio. Formats below this quality level will not be considered for download.
'''

def main():
    # Get user input
    url = ['https://www.youtube.com/watch?v=q8za85Xsbo4']
    quality = 'bestvideo[height<=240]+bestaudio/best'
    save_path = '/Users/amin/Desktop/video-test.mp4'

    # Download the video
    download_video(url, quality, save_path)

if __name__ == "__main__":
    main()

