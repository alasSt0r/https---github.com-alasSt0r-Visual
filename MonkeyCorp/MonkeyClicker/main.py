from ursina import *
app = Ursina()
window.color =color._20

#loading all textures(to-do)
main_monkey = load_texture('Assets/main_monkey')


#creating the main_monkey
main_monkey = Button(
    model = 'cube',
    texture = main_monkey,
    scale= .200,
    color= color.color(0,0,1),
    y=-.1
)

app.run
