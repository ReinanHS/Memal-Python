from moviepy.editor import *
from moviepy.video import *
from random import randrange

clip = VideoFileClip('myHolidays.mp4')

tempo = ( (clip.duration/60 )-0.50 )
if(tempo > 1):
    tempo = randrange(60)
    tempoI = (tempo-4)
else:
    tempo = 0
    tempoI = 4

if(tempoI < 0):
    tempoI = 0

clip = clip.resize((720, 480))
clip.save_frame("frame_HD1.jpeg", t=(tempo))
#clip.save_frame("frame_HD2.jpeg", t=(clip.duration* randrange(100) )/100)
#clip.save_frame("frame_HD3.jpeg", t=(clip.duration* randrange(100) )/100)

clip = clip.resize((240, 160))
clip.save_frame("frame1.jpeg", t=(tempo))
#clip.save_frame("frame2.jpeg", t=(clip.duration* randrange(100) )/100)
#clip.save_frame("frame3.jpeg", t=(clip.duration* randrange(100) )/100)    
                
if(tempo <= 0):
    clip = clip.subclip((0), (4))
    clip = clip.resize((240, 160))
    clip.write_gif("frame.gif")
else:
    clip = clip.subclip((tempoI), (tempo))
    clip = clip.resize((240, 160))
    clip.write_gif("frame.gif")
