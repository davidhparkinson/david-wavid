# 👋 Hello there! This file contains ready-to-edit bot code.
# 🟢 Open "README.md" for instructions on how to get started!
# TL;DR Run ./connect (or .\connect.cmd on Windows) to begin.

class Bot:
    def __init__(self, config):
        print("Hello World!", config)
        self.config = config
        self.previous_ball = {"x": None, "y": None}
        self.previous_ball2 = {"x": None, "y": None}

    def move(self, paddle, ball):
        # This prints the position of your paddle and the ball to the bot terminal.
        # Use these values to determine which direction your paddle should move so
        # you hit the ball!
        print("paddle", paddle["x"], paddle["y"])
        print("ball", ball["x"], ball["y"])
        print(self.previous_ball["x"], self.previous_ball["y"])
        print(self.previous_ball2["x"], self.previous_ball2["y"])

        # Find the spot to go
        if self.previous_ball["x"] == None:
            interception = {"x": 0, "y": 0}
        elif ball["x"] > self.previous_ball["x"]:
            direction = "toward"
            slope = (ball["y"] - self.previous_ball["y"]) / (ball["x"] - self.previous_ball["x"])
            print("Slope: " + str(slope))
            print("Coming toward me!")
            # Interception point
            distance = paddle["x"] - ball["x"]
            interception = {"x": paddle["x"], "y": distance * slope + ball["y"]}
            print("Int point: (" + str(interception["x"]) + ", " + str(interception["y"]) + ")")
        else:
            direction = "away"
            slope = (ball["y"] - self.previous_ball["y"]) / (ball["x"] - self.previous_ball["x"])
            distance = -30 - ball["x"]
            interception = {"x": -30, "y": abs(distance) * slope + ball["y"]}
            print("Going away")
            print("Int point: (" + str(interception["x"]) + ", " + str(interception["y"]) + ")")

        # Return the direction you'd like to move here:
        # "north" "south" "east" "west" or "none"
        if interception["x"] == 0:
            if ball["y"] > paddle["y"]:# + 0.5:
                move = "north"
            elif ball["y"] < paddle["y"]:# - 0.5:
                move = "south"
            else:
                move = "none"
        else:
            if direction == "toward":
                if interception["y"] > paddle["y"] + 3:
                    move = "north"
                elif interception["y"] < paddle["y"] - 3:
                    move = "south"
                elif ball["x"] > 15: 
                    move = "east"
                elif paddle["x"] < 35:
                    move = "west"
                else:
                    move = "none"
            elif direction == "away":
                if interception["y"] > paddle["y"]:
                    move = "north"
                elif interception["y"] < paddle["y"]:
                    move = "south"
                else:
                    move = "none"

        # Set previous balls
        self.previous_ball2["x"] = self.previous_ball["x"]
        self.previous_ball2["y"] = self.previous_ball["y"]

        self.previous_ball["x"] = ball["x"]
        self.previous_ball["y"] = ball["y"]

        return move

    def end(self, paddle, ball):
        print("Good game!")
