# "Stopwatch: The Game"

import simplegui

# define global variables
counter = 0 
stops = 0
exact = 0
running = True

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    a=(t-t%600)//600
    t=t-a*600
    b=((t%1000)//100)%6
    c=(t%100)//10
    d=t%10
    return str(a)+":"+str(b)+str(c)+"."+str(d)

    
# define event handlers for buttons; "Start", "Stop", "Reset"

def start():
    global running
    running = True
    timer.start()
    
    
    
def stop():
    global counter,stops,exact,running
    if running ==True:
        stops += 1
        if counter%10==0 :
            exact+=1
    timer.stop()
    running = False

def reset():
    global counter,stops,exact
    timer.stop()
    counter = 0
    stops = 0
    exact = 0


def time_handler():
    """Increment the counter."""
    global counter
    counter += 1
    print format(counter)
  


# define event handler for timer with 0.1 sec interval
timer = simplegui.create_timer(100, time_handler)

# define draw handler
def draw_handler(canvas):
    """Draw the circle."""
    global counter,stops,exact
    message = str(exact)+"/"+str(stops)
    canvas.draw_text(str(format(counter)), (100, 100),36, "White")
    canvas.draw_text(message, (250, 20),20, "Green")
# create frame
frame = simplegui.create_frame("Home", 300, 200)
frame.add_button("Start", start)
frame.add_button("Stop", stop)
frame.add_button("Reset", reset)

# register event handlers
frame.set_draw_handler(draw_handler)

# start frame
frame.start()
timer.start()

# Please remember to review the grading rubric
 
