

class Logic:
    @property
    def logic1(self):
        cells0 = [
            self.get_cell_position(self.x - 1, self.y),
            self.get_cell_position(self.x - 2, self.y),
        ]
        cells1 = [cell for cell in cells0 if cell != None if cell.btn_obj.cget('text') == 'x']
        cells2 = [cell for cell in cells0 if cell !=None if cell.btn_obj.cget('text') == 'o']
        return [cells1, cells2]

    @property
    def logic2(self):
        cells0 = [
            self.get_cell_position(self.x + 1, self.y),
            self.get_cell_position(self.x + 2, self.y)
        ]
        cells1 = [cell for cell in cells0 if cell != None if cell.btn_obj.cget('text') == 'x']
        cells2 = [cell for cell in cells0 if cell != None if cell.btn_obj.cget('text') == 'o']
        return [cells1, cells2]


    @property
    def logic3(self):
        cells0 = [
            self.get_cell_position(self.x + 1, self.y + 1),
            self.get_cell_position(self.x + 2, self.y + 2)
        ]
        cells1 = [cell for cell in cells0 if cell != None if cell.btn_obj.cget('text') == 'x']
        cells2 = [cell for cell in cells0 if cell != None if cell.btn_obj.cget('text') == 'o']
        return [cells1, cells2]

    @property
    def logic4(self):
        cells0 = [
            self.get_cell_position(self.x - 1, self.y - 1),
            self.get_cell_position(self.x - 2, self.y - 2)
        ]
        cells1 = [cell for cell in cells0 if cell != None if cell.btn_obj.cget('text') == 'x']
        cells2 = [cell for cell in cells0 if cell != None if cell.btn_obj.cget('text') == 'o']
        return [cells1, cells2]

    @property
    def logic5(self):
        cells0 = [
            self.get_cell_position(self.x + 1, self.y - 1),
            self.get_cell_position(self.x + 2, self.y - 2)
        ]
        cells1 = [cell for cell in cells0 if cell != None if cell.btn_obj.cget('text') == 'x']
        cells2 = [cell for cell in cells0 if cell != None if cell.btn_obj.cget('text') == 'o']
        return [cells1, cells2]

    @property
    def logic6(self):
        cells0 = [
            self.get_cell_position(self.x - 1, self.y + 1),
            self.get_cell_position(self.x - 2, self.y + 2)
        ]
        cells1 = [cell for cell in cells0 if cell != None if cell.btn_obj.cget('text') == 'x']
        cells2 = [cell for cell in cells0 if cell != None if cell.btn_obj.cget('text') == 'o']
        return [cells1, cells2]

    @property
    def logic7(self):
        cells0 = [
            self.get_cell_position(self.x, self.y + 1),
            self.get_cell_position(self.x, self.y + 2),
        ]
        cells1 = [cell for cell in cells0 if cell != None if cell.btn_obj.cget('text') == 'x']
        cells2 = [cell for cell in cells0 if cell != None if cell.btn_obj.cget('text') == 'o']
        return [cells1, cells2]

    @property
    def logic8(self):
        cells0 = [
            self.get_cell_position(self.x, self.y - 1),
            self.get_cell_position(self.x, self.y - 2),
        ]
        cells1 = [cell for cell in cells0 if cell != None if cell.btn_obj.cget('text') == 'x']
        cells2 = [cell for cell in cells0 if cell != None if cell.btn_obj.cget('text') == 'o']
        return [cells1, cells2]