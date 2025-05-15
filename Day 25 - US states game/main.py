import turtle
import pandas as pd
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
write = turtle.Turtle()
write.hideturtle()
write.penup()
guessed_states = []
remaining_states = []

data = pd.read_csv("50_states.csv")
state_list = data["state"].to_list()

while len(guessed_states) < 50:
    user_guess = screen.textinput(f"{len(guessed_states)}/50 States Correct", "What's another state's name?").title()
    if user_guess == "Exit":
        remaining_states = [items for items in state_list if items not in guessed_states]

        df = pd.DataFrame(remaining_states)
        df.to_csv("remaining_states.csv")
        break
    if user_guess in guessed_states:
        print(f"You already guess {user_guess}")
    elif user_guess in state_list:
        guessed_states.append(user_guess)
        ind = state_list.index(user_guess)
        state_data = data[data.state == user_guess]
        write.goto(state_data.x.item(), state_data.y.item())
        write.write(user_guess)
