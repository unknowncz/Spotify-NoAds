def main():
    from subprocess import check_output,run,check_call
    while True:
        if input():break
        x=check_output(['tasklist','/APPS','/FI','IMAGENAME eq Spotify.exe','/FO','CSV'])
        ez=int(x.split(b',')[1::3][1].strip(b'"'))
        try:
            check_call(['taskkill','/PID',str(ez)])
            print()
            run('Spotify')
        except Exception as e:print(f'Failed to kill process\n Reason: {e}\n')
if __name__=='__main__':main()