# multiproc
Creating threads py
import threading
import time

glst = ['up','and','down','the','spider','went']
gcount = 0
lock = threading.RLock()

class MyThread(threading.Thread):
    def run(self):
        for w in glst:
            lock.acquire()
            print('Thread ID: {}. Text: {}'.format(self.ident,w))
            global gcount
            gcount += 1
            lock.release()
        return super().run()

def threadfunc(v):
    time.sleep(v)

if __name__ == '__main__':
    i = 0
    tlist = []
    try:
        while i < 5:
            t = MyThread()
            tlist.append(t)
            t.start()
            i+=1
        for item in tlist:
            item.join()
        print('Total operations on gcount was {}'.format(gcount))
    except Exception as e:
        print('Exception raised. {}'.format(e))
