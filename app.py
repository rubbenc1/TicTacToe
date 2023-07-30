from tkinter import *
from cell import Cell
import settings
import utils

root = Tk()
root.configure(bg='white')
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title('Tic-Tac-Toe')
root.resizable(False, False)

top_frame = Frame(
    root,
    bg = 'DodgerBlue2',
    width = settings.WIDTH,
    height = utils.height_prct(25)
                  )
top_frame.place(x=0, y=0)
game_title = Label(
    top_frame,
    bg = 'DodgerBlue2',
    fg = 'black',
    text = 'Tic-Tac-Toe Game',
    font = ('', 20)
                    )
game_title.place(x=utils.width_prct(35), y=45)

left_frame = Frame(
    root,
    bg = 'light goldenrod',
    width = utils.width_prct(25),
    height = utils.height_prct(75)
)

left_frame.place(x = 0, y = utils.height_prct(25))

center_frame = Frame(
    root,
    bg = 'black',
    width = utils.width_prct(75),
    height = utils.height_prct(75)
)

center_frame.place(x=utils.width_prct(25), y=utils.height_prct(25))


for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x, y)
        c.create_btns(center_frame)
        c.btn_obj.grid(column=x, row=y)


a= Cell(4,4)
a.create_player_btn1(left_frame, 'player 1')
a.btn_player1.grid(column = 2, row = 1)
b = Cell(5,5)
b.create_player_btn2(left_frame, 'player 2')
b.btn_player2.grid(column = 2, row = 2)

Cell.scorelabel1(left_frame)
Cell.scrolab1.grid(column = 2, row = 3)
Cell.scorelabel2(left_frame)
Cell.scrolab2.grid(column = 2, row = 4)

root.mainloop()