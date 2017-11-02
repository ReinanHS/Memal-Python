from moviepy.editor import *
import os.path
class render:
    # Metados Especiais
    def __init__(self, name, local):
        self.name = name
        self.local = local
        self.video = VideoFileClip(self.local)
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
        if os.path.isdir('/home/reinan/Documentos/Python/POO/videos/{}'.format(self.getName())):
            print('Ja existe uma pasta com esse nome!')
        else:
            os.mkdir('/home/reinan/Documentos/Python/POO/videos/{}'.format(self.getName())) # aqui criamos a pasta caso nao exista
            os.mkdir('/home/reinan/Documentos/Python/POO/videos/{}/formats'.format(self.getName())) # aqui criamos a pasta formats
            os.mkdir('/home/reinan/Documentos/Python/POO/videos/{}/tambineio'.format(self.getName())) # aqui criamos a pasta tambineio
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
    def FullHD(self):
        self.video.resize( (1920, 1080) )
        self.video.write_videofile('/home/reinan/Documentos/Python/POO/videos/{}/formats/FullHD.webm'.format(self.getName()), preset='ultrafast')
    def XGA(self):
        self.video.resize( (1024, 768) )
        self.video.write_videofile('/home/reinan/Documentos/Python/POO/videos/{}/formats/XGA.webm'.format(self.getName()), preset='ultrafast')
    def VGA(self):
        self.video.resize( (720, 480) )
        self.video.write_videofile('/home/reinan/Documentos/Python/POO/videos/{}/formats/VGA.webm'.format(self.getName()), preset='ultrafast')
    def VGA2(self):
        self.video.resize( (640, 480) )
        self.video.write_videofile('/home/reinan/Documentos/Python/POO/videos/{}/formats/VGA2.webm'.format(self.getName()), preset='ultrafast')
    def QVGA(self):
        self.video.resize( (320, 240) )
        self.video.write_videofile('/home/reinan/Documentos/Python/POO/videos/{}/formats/QVGA.webm'.format(self.getName()), preset='ultrafast')
    def GameBoyAdvance(self):
        print(self.video.size)
        self.video.resize(240, 160)
        self.video.write_videofile('/home/reinan/Documentos/Python/POO/videos/{}/formats/GameBoyAdvance.webm'.format(self.getName()), preset='ultrafast')
        print(self.video.size)
    def QQVGA(self):
        self.video.resize( (160, 120) )
        self.video.write_videofile('/home/reinan/Documentos/Python/POO/videos/{}/formats/QQVGA.webm'.format(self.getName()), preset='ultrafast')
        
        
        
