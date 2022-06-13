
import socketio
import time
from core.act_queue import q as queueA
from core import actions
from core import status

sio = socketio.Client()


def mydisconnected():
    if(status.connected.value==1):
        status.connected.value=0
        status.selected.value=1
        

def myconnected():
    if(status.connected.value==0):
        status.connected.value=1
        print("connected")
        # queueA.put(actions.hide())

def myselected():
    print("selected")
    status.selected.value=1

def myreleased():
    print("release")
    if(status.selected.value==1):
        queueA.put(actions.hide())
    status.selected.value=0



class client():

    @sio.event
    def connect():
        sio.emit('client', {'data': 'connection established'})
        myconnected()

    @sio.on('server')
    def on_message(data):
        print('I get :',data['data'])


    @sio.on('response')
    def on_message(data):
        print('Client get response:',data)
        if(data['selected']=='1'):
            myselected()
        elif (data['selected']=='0'):
            myreleased()
        else:
            print("maintain")
            



    @sio.event
    def message(data):
        print('message received with ', data)
        sio.emit('client', {'response': 'my response'})
        


    @sio.event
    def disconnect():
        mydisconnected()

  
    def start(self):
        while True:
            try:
                sio.connect('http://localhost:5000')
                while sio.connected:
                    a=input()
                    sio.emit('client', {'data': str(a)})
            except BaseException as e:
                mydisconnected()
            time.sleep(5)



cli=client()
if __name__ == '__main__':
    cli.start()