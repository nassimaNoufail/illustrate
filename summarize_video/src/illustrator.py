import sys
import urllib.request
from urllib.request import urlopen, FancyURLopener
from urllib.parse import urlparse, parse_qs, unquote

from moviepy.editor import *


def get_video_summary():
    # Get video
    clip = (VideoFileClip("frozen_trailer.mp4")
        .subclip((1,22.65),(1,23.2))
        .resize(0.3))
    clip.write_gif("use_your_head.gif")


    # Get get giffed version
    # return

def youtube_download(video_url):
    video_id = parse_qs(urlparse(video_url).query)['v'][0]

    url_data = urlopen('http://www.youtube.com/get_video_info?&video_id=' + video_id).read()
    url_info = parse_qs(unquote(url_data.decode('utf-8')))
    token_value = url_info['token'][0]

    download_url = "http://www.youtube.com/get_video?video_id={0}&t={1}&fmt=18".format(
        video_id, token_value)

    video_title = url_info['title'][0] if 'title' in url_info else ''
    # Unicode filenames are more trouble than they're worth
    filename = video_title.encode('ascii', 'ignore').decode('ascii').replace("/", "-") + '.mp4'

    print("\t Downloading '{}' to '{}'...".format(video_title, filename))

    try:
        download = urlopen(download_url).read()
        f = open(filename, 'wb')
        f.write(download)
        f.close()
    except Exception as e:
        print("\t Downlad failed! {}".format(str(e)))
        print("\t Skipping...")
    else:
        print("\t Done.")

def main():
    print("\n--------------------------")
    print (" Youtube Video Downloader")
    print ("--------------------------\n")

    try:
        video_urls = sys.argv[1:]
    except:
        video_urls = input('Enter (space-separated) video URLs: ')

    for u in video_urls:
        youtube_download(u)
    print("\n Done.")

if __name__ == '__main__':
    main()
