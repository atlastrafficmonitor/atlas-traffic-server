# Author: Brian Newsom
# Date: 12/3/14
# Python 3 program to algorithmically determine when someone enters or leaves the room.
import time;
import queue;

sleepTime=1; # In seconds MAX = length of signal from Arduino

# Will be pulled from Arduino sensors
INSIDE=False;
OUTSIDE=False;

Q = queue.Queue()
id = 0;

while True:
    if(INSIDE):
        # Add to queue
        Q.put(id);
        id = id + 1;
        print("Inside Mat Triggered");

    elif(OUTSIDE):
        # Remove from queue
        e = Q.get();
        print("Outside Mat Triggered, Pulled: " + str(e));

    else:
        time.sleep(sleepTime);

print("test");
