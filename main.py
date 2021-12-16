class adSkipper:
    def __init__(self):
        from threading import Thread
        from subprocess import check_output,run,check_call
        from time import sleep
        self.i=[check_output,run,check_call,sleep,Thread]
    def kill(self):
        try:self.i[2](['taskkill','/PID',str(self.i[0](['tasklist','/APPS','/FI','IMAGENAME eq Spotify.exe','/FO','CSV']).split(b',')[1::3][1].strip(b'"'), 'UTF-8')])
        except:
            x=self.i[0](['pidof','spotify']).split(b' ')
            for p in x:
                try:self.i[2](['kill','-9',str(p.strip(b'\n'), 'UTF-8')])
                except:pass
                self.i[3](.1)
    def start(self):
        try:self.i[1]('Spotify')
        except:
            x=self.i[4](target=self.i[1],args=(['spotify','--no-zygote'],),daemon=True)
            x.start()
if __name__=='__main__':
    from time import sleep
    def n():print()
    a=adSkipper()
    while True:
        try:
            if input():break
        except KeyboardInterrupt:pass
        try:a.kill();n();sleep(.3);a.start()
        except Exception as e:print(f'Failed to kill process\nReason: {e}\n')