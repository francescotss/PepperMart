import random

def color_print(string, color=None):
    if color is None:
        print(string)
    elif color == 'green':
        print("\033[1;32m {}\033[0m".format(string))
    elif color == 'red':
        print("\033[91m {}\033[0m".format(string))
    elif color == 'yellow':
        print("\033[93m {}\033[0m".format(string))

# Return a vocabolary with all the combination of v1 and v2
def build_vocabolary(v1, v2):
    ret = []
    for w1 in v1:
        for w2 in v2:
            ret.append("{} {}".format(w1,w2))
    return ret
        
def create_mapdata_file(data):
    data = {"data": data}
    with open('modim/actions/mapdata', 'w') as action_file:
        json_text = str(data) #json.dumps(data) Not working: modim will remove the double quotes. 
        text = "TEXT_mapdata\n<*,*,*,*>: " + json_text + "\n----"
        action_file.write(text)        

def ask_loop(vocabulary, robot, timeout=5, patience=3, buttons=False):
    try_again = [["try again", "animations/Stand/Gestures/Desperate_2"], ["Sorry, can you repeat?", "animations/Stand/Emotions/Neutral/Embarrassed_1"], ["Please say again", "animations/Stand/Gestures/Please_1"]]
    count = 1
    while True:
        ret = robot.asr(vocabulary, timeout) 
        if ret != "":
            return ret
        if count == patience:
            robot.say("Sorry I can't help you right now. Please wait here, an human collegue will arrive soon")
            return "ERROR"
        say, anim = random.choice(try_again)
        animated_say(say, anim, robot)
        count += 1
    
def animated_say(text, animation, robot):
    robot.say("^start("+animation+") " + text+" ^wait("+animation+")")