import numpy
import random

def check_command (message) -> str:
    message_content = (message.content.split(" "))[0]
    isCommand: Bool = False;
    if (message_content.startswith("/")):
        command = (message_content.split("/"))[1]
        if (command == "roll20"):
            return(str(random.randint(0,20)));
        else:
            return("Command not identified")
