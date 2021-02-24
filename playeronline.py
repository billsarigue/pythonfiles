import urllib.request
import re
from os import system


print('Qual o nome da música?')
keyword = str(input('-> '))

html = urllib.request.urlopen("https://www.youtube.com/results?search_query="+keyword.replace(' ', '_'))

video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())

search = "https://www.youtube.com/watch?v="+video_ids[0]

system(f'start {search} ')
