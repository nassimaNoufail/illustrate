__author__ = 'oahayder'
import moviepy.editor

def get_video(filename):
    clip = moviepy.editor.VideoFileClip(filename)
    return clip
