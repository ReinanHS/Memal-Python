from moviepy.editor import *
from moviepy.video import *
from random import randrange
import os.path
class render:
    # Metados Especiais
    def __init__(self, name, local):
        self.name = name
        self.local = local
        self.video = VideoFileClip(self.local)
        self.dir = "/home/reinan/Documentos/Python/moviepy/videos/";
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name
    def getLocal(self):
        return self.local
    def setLocal(self, local):
        self.local = local
    def getVideo(self):
        return self.video
    def setVideo(self, video):
        self.video = video
    # Metados
    def processing(self):
        if os.path.isdir('{}{}'.format(self.dir,self.getName())):
            print('Ja existe uma pasta com esse nome!')
        else:
            os.mkdir('{}{}'.format(self.dir,self.getName())) # aqui criamos a pasta caso nao exista
            os.mkdir('{}{}/formats'.format(self.dir,self.getName())) # aqui criamos a pasta formats
            os.mkdir('{}{}/tambineio'.format(self.dir,self.getName())) # aqui criamos a pasta tambineio
            print ('Pasta criada com sucesso!')
            if(self.video.size >= [1920, 1080]):
                self.FullHD()
                self.XGA()
                self.VGA()
                self.VGA2()
                self.QVGA()
                self.GameBoyAdvance()
                self.QQVGA()
            elif(self.video.size >= [1024, 768]):
                self.XGA()
                self.VGA()
                self.VGA2()
                self.QVGA()
                self.GameBoyAdvance()
                self.QQVGA()
            elif(self.video.size >= [720, 480]):
                self.VGA()
                self.VGA2()
                self.QVGA()
                self.GameBoyAdvance()
                self.QQVGA()
            elif(self.video.size >= [640, 480]):
                self.VGA2()
                self.QVGA()
                self.GameBoyAdvance()
                self.QQVGA()
            elif(self.video.size >= [320, 240]):
                self.QVGA()
                self.GameBoyAdvance()
                self.QQVGA()
            elif(self.video.size >= [240, 160]):
                self.GameBoyAdvance()
                self.QQVGA()
            else:
                exit()
            self.tambineio()
    def FullHD(self):
        self.video = self.video.resize( (1920, 1080) )
        self.video.write_videofile('{}{}/formats/FullHD.webm'.format(self.dir, self.getName()), preset='ultrafast')
    def XGA(self):
        self.video = self.video.resize( (1024, 768) )
        self.video.write_videofile('{}{}/formats/XGA.webm'.format(self.dir, self.getName()), preset='ultrafast')
    def VGA(self):
        self.video = self.video.resize( (720, 480) )
        self.video.write_videofile('{}{}/formats/VGA.webm'.format(self.dir, self.getName()), preset='ultrafast')
    def VGA2(self):
        self.video = self.video.resize( (640, 480) )
        self.video.write_videofile('{}{}/formats/VGA2.webm'.format(self.dir, self.getName()), preset='ultrafast')
    def QVGA(self):
        self.video = self.video.resize( (320, 240) )
        self.video.write_videofile('{}{}/formats/QVGA.webm'.format(self.dir, self.getName()), preset='ultrafast')
    def GameBoyAdvance(self):
        self.video = self.video.resize( (240, 160))
        self.video.write_videofile('{}{}/formats/GameBoyAdvance.webm'.format(self.dir, self.getName()), preset='ultrafast')
    def QQVGA(self):
        self.video = self.video.resize( (160, 120) )
        self.video.write_videofile('{}{}/formats/QQVGA.webm'.format(self.dir, self.getName()), preset='ultrafast')
    def tambineio(self):
        tempo = ( (self.video.duration/60 )-0.50 )
        if(tempo > 1):
            tempo = randrange(60)
            tempoI = (tempo-4)
        else:
            tempo = 0
            tempoI = 4

        if(tempoI < 0):
            tempoI = 0

        self.video = self.video.resize((720, 480))
        self.video.save_frame('{}{}/tambineio/frame_HD1.jpeg'.format(self.dir, self.getName()), t=(tempo))

        self.video = self.video.resize((240, 160))
        self.video.save_frame('{}{}/tambineio/frame1.jpeg'.format(self.dir, self.getName()), t=(tempo))  
                        
        if(tempo <= 0):
            self.video = self.video.subclip((0), (4))
            self.video = self.video.resize((240, 160))
            self.video.write_gif('{}{}/tambineio/frame.gif'.format(self.dir, self.getName()))
        else:
            self.video = self.video.subclip((tempoI), (tempo))
            self.video = self.video.resize((240, 160))
            self.video.write_gif('{}{}/tambineio/frame.gif'.format(self.dir, self.getName()))
        
        
        
