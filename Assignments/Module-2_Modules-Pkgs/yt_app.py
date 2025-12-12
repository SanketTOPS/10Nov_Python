from pytubefix import YouTube

url="https://www.youtube.com/watch?v=KbMnQYJM5U0"

YouTube(url).streams.first().download()