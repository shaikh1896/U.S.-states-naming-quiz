import turtle
import pandas as pd

screen = turtle.Screen()
screen.title('U.S. States Quiz')

image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv('50_states.csv')
states_list = data.state.to_list()
guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f'{len(guessed_states)}/50 States Correct',prompt="What's another state's name?r").title()

    if answer_state == 'Exit':
        missed_states = []
        for state in states_list:
            if state not in guessed_states:
                missed_states.append(state)
        print(missed_states)
        break

    if answer_state in states_list:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data['state'] == answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer_state)


df = pd.DataFrame(missed_states)
df.to_csv('missed_states.csv')