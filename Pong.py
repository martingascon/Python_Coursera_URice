#Implementation of classic arcade game Pong
import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos = [WIDTH/2,HEIGHT/2]
ball_vel = [0,0]
paddle1_pos = HEIGHT/2
paddle2_pos = HEIGHT/2
paddle1_vel = 0
paddle2_vel = 0
score1 = 0
score2 = 0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def restart():
    global score1, score2
    score1 = 0
    score2 = 0
    new_game()

def spawn_ball(direction):
    global ball_pos, ball_vel    # these are vectors stored as lists
    ball_pos = [WIDTH/2,HEIGHT/2]
    ball_vel = [random.randrange(120,240)/60.0,-1*random.randrange(60,180)/60.0]
    if direction == LEFT:
        ball_vel[0] = -1*ball_vel[0]
        
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    spawn_ball(LEFT)
    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel, ball_pos, ball_vel
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # collide and reflect off of top and bottom sides of canvas
    if  ball_pos[1] >= HEIGHT - 1 - BALL_RADIUS or ball_pos[1] <= BALL_RADIUS + 1:
        ball_vel[1] = - ball_vel[1]
    
    # update ball    
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]  
    if  ball_pos[0] >= WIDTH - PAD_WIDTH:
        spawn_ball(LEFT)
        score1 += 1
    elif ball_pos[0] <= PAD_WIDTH:
        spawn_ball(RIGHT)
        score2 += 1
    
    # draw ball
    canvas.draw_circle( ball_pos, BALL_RADIUS, 2, "White", "White")
        
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos += paddle1_vel
    paddle2_pos += paddle2_vel
    if paddle1_pos <= HALF_PAD_HEIGHT or paddle1_pos >= HEIGHT-HALF_PAD_HEIGHT:
        paddle1_pos-= paddle1_vel
        paddle1_vel = 0
    if paddle2_pos <=HALF_PAD_HEIGHT or paddle2_pos >=HEIGHT-HALF_PAD_HEIGHT:
        paddle2_pos-= paddle2_vel      
        paddle2_vel = 0
    
    # draw paddles  
    canvas.draw_polygon([(0,paddle1_pos-HALF_PAD_HEIGHT), (PAD_WIDTH, paddle1_pos-HALF_PAD_HEIGHT), (PAD_WIDTH, paddle1_pos+HALF_PAD_HEIGHT),(0, paddle1_pos+HALF_PAD_HEIGHT)], 2, 'White','White')
    canvas.draw_polygon([(WIDTH-PAD_WIDTH,paddle2_pos-HALF_PAD_HEIGHT), (WIDTH, paddle2_pos-HALF_PAD_HEIGHT), (WIDTH, paddle2_pos+HALF_PAD_HEIGHT), (WIDTH-PAD_WIDTH, paddle2_pos+HALF_PAD_HEIGHT)], 2,'White','White')
    
    # determine whether paddle and ball collide    
    if ((ball_pos[0]-BALL_RADIUS<PAD_WIDTH+1) and (ball_pos[1]> (paddle1_pos-HALF_PAD_HEIGHT+1)) and  (ball_pos[1]< (paddle1_pos+HALF_PAD_HEIGHT+1))):
        ball_vel[0] = -1*ball_vel[0]*1.1
        ball_vel[1] =   ball_vel[1]*1.1
    if ((ball_pos[0]+BALL_RADIUS>WIDTH-PAD_WIDTH-1) and (ball_pos[1]> (paddle2_pos-HALF_PAD_HEIGHT)) and  (ball_pos[1]< (paddle2_pos+HALF_PAD_HEIGHT))):
        ball_vel[0] = -1*ball_vel[0]*1.1
        ball_vel[1] =   ball_vel[1]*1.1
    # draw scores
    canvas.draw_text(str(score1), (WIDTH*0.4, HEIGHT*0.2),50, "white")   
    canvas.draw_text(str(score2), (WIDTH*0.6, HEIGHT*0.2),50, "white")          
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    acc = 1
    if key==simplegui.KEY_MAP["s"]:
        paddle1_vel+= acc
        
    if key==simplegui.KEY_MAP["down"]:
        paddle2_vel+= acc
       
def keyup(key):
    global paddle1_vel, paddle2_vel
    acc = 1
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel -= acc

    if key==simplegui.KEY_MAP["up"]:
        paddle2_vel -= acc
        
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", restart) 
frame.add_button("New game", new_game) 
# start frame
frame.start()
