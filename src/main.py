import commands
import os
import getch
import time


def main():
    commands.load_settings()
    input_loop()



def input_loop():

    user_input = ""
    while (user_input != "q" and user_input != "x"):
        user_input = getch.getch()
        if ord(user_input) == 27:
            getch.getch()
            user_input = ord(getch.getch())

        command_info = commands.command_list.get(user_input, [None, None])
        command = command_info[0]
        description = command_info[1]

        if (command is not None):
            command()

        if (description is not None):
            print(description)


def exec_command(command):
    full_command = "{} {}".format(commands.basecommand, command)
    os.system(full_command)


if __name__ == "__main__":
    main()
