import turtle
import pandas as pd

screen = turtle.Screen()

screen.title("AFGHANISTAN MAB PROVENCE GAME")

screen.bgcolor("black")

image = 'Afghanistan_Map.gif'
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv('./List_of_Afghanistan_Provinces.csv')


all_provinces = data['Province'].tolist()
guessed_provinces = []

while len(guessed_provinces) < len(all_provinces):

    answer = screen.textinput(title=f'{len(guessed_provinces)}/{len(all_provinces)} provinces',prompt='Write another province').title()
    if answer.lower() == 'exit':
        missed_provinces_name = [province for province in all_provinces if province not in guessed_provinces]
        new_data = pd.DataFrame(missed_provinces_name)
        new_data.to_csv('./learn this provinces as well.csv')

        break

    if answer in all_provinces and answer not in guessed_provinces:
        guessed_provinces.append(answer)

        table_answer= data[data.Province==answer]
        x_cord = table_answer['x'].item()
        y_cord = table_answer['y'].item()

        writer = turtle.Turtle()
        writer.hideturtle()
        writer.color("black")
        writer.penup()
        writer.goto(x_cord, y_cord)
        writer.write(answer)
