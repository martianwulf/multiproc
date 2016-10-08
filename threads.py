import threading
import time

glist = ['up','and','down','the','spider','went']
gcount = 0
lock = threading.RLock()

def threadfunc(**kwargs):
    global glist
    for item in glist:
        kwargs['alock'].acquire()
        print('Text: {}'.format(item))
        kwargs['acount']+=1
        kwargs['alock'].release()

def threadfunc2(*args):
    print('argument 1: {}'.format(args[0]))
    print('argument 2: {}'.format(args[1]))

if __name__ == '__main__':
    i = 0
    kw = {'alock':lock,'acount':gcount}
    tup = (9,'indie')
    tlist = []
    try:
        trd = threading.Thread(target=threadfunc, kwargs=kw)
        trd2 = threading.Thread(target=threadfunc, kwargs=kw)
        trd3 = threading.Thread(target=threadfunc, kwargs=kw)
        #trd2 = threading.Thread(target=threadfunc2,args=tup)
        trd.start()
        trd2.start()
        trd3.start()
        trd.join()
        trd2.join()
        trd3.join()
    except Exception as e:
        print('Exception raised. {}'.format(e))
