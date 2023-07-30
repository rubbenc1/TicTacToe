from tkinter import *
import ctypes
from logic import Logic

class Cell(Logic):
    all = []
    Player_1 = 0
    Player_2 = 0
    scrolab1 = None
    scrolab2 = None
    def __init__(self, x, y):
        self.btn_obj = None
        self.btn_player1 = None
        self.btn_player2 = None
        self.x = x
        self.y = y
        Cell.all.append(self)

    def create_player_btn1(self, location, name_of_btn):
        btn = Button(
            location,
            text = name_of_btn,
            bg = 'orange',
            width = 10,
            height = 4,
            state = NORMAL
        )
        btn.bind('<Button-1>', self.deactivating_player_btn2)
        self.btn_player1 = btn

    def deactivating_player_btn2(self, event):
        for x in Cell.all:
            try:
                x.btn_player2['state'] = DISABLED
            except:
                pass

    def create_player_btn2(self, location, name_of_btn):
        btn = Button(
            location,
            text = name_of_btn,
            bg = 'orange',
            width = 10,
            height = 4,
            state = NORMAL
        )
        btn.bind('<Button-1>', self.deactivating_player_btn1)
        self.btn_player2 = btn

    def deactivating_player_btn1(self, event):
        for x in Cell.all:
            try:
                x.btn_player1['state'] = DISABLED
            except:
                pass

    def create_btns(self, location):
        btn = Button(
            location,
            text = '',
            width = 16,
            height = 8,
            state = NORMAL
        )
        btn.bind('<Button-1>', self.when_clicked)
        self.btn_obj = btn

    def get_cell_position(self, x, y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    @staticmethod
    def scorelabel1(location):
        lbl = Label(location, bg = 'grey', fg = 'black', text= 'Player-1 Score ' + f'{Cell.Player_1}')
        Cell.scrolab1 = lbl

    @staticmethod
    def scorelabel2(location):
        lbl = Label(location, bg='grey', fg='black', text='Player-2 Score ' + f'{Cell.Player_2}')
        Cell.scrolab2 = lbl
    def when_clicked(self, event):
        for cell in Cell.all:
            try:
                if cell.btn_player2['state'] == DISABLED:
                    self.btn_obj.configure(text='x') # need to change the size of text
                    cell.btn_player2['state'] = NORMAL
                    self.btn_obj['state'] = DISABLED
            except:
                pass
            try:
                if cell.btn_player1['state'] == DISABLED:
                    self.btn_obj.configure(text = 'o')
                    cell.btn_player1['state'] = NORMAL
                    self.btn_obj['state'] = DISABLED
            except:
                pass
        if len(self.logic1[0])==2 or len(self.logic2[0])==2 or len(self.logic3[0])==2 or len(self.logic4[0])==2 or len(self.logic5[0])==2 or len(self.logic6[0])==2 or len(self.logic7[0])==2 or len(self.logic8[0])==2:
            ctypes.windll.user32.MessageBoxW(0, 'Player 1 wins', 'Game over', 0)
            for cell in Cell.all:
                if cell.btn_obj !=None:
                    cell.btn_obj.configure(text= "")
                    cell.btn_obj['state'] = NORMAL
            Cell.Player_1 += 1
            Cell.scrolab1['text'] = 'Player-1 Score ' + f'{Cell.Player_1}'
        elif len(self.logic1[1])==2 or len(self.logic2[1])==2 or len(self.logic3[1])==2 or len(self.logic4[1])==2 or len(self.logic5[1])==2 or len(self.logic6[1])==2 or len(self.logic7[1])==2 or len(self.logic8[1])==2:
            ctypes.windll.user32.MessageBoxW(0, 'Player 2 wins', 'Game over', 0)
            for cell in Cell.all:
                if cell.btn_obj != None:
                    cell.btn_obj.configure(text= "")
                    cell.btn_obj['state'] = NORMAL
            Cell.Player_2 += 1
            Cell.scrolab2['text'] = 'Player-2 Score ' + f'{Cell.Player_2}'
