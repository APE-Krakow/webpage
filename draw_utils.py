import drawsvg as draw


violet = "#bd80fa"
gap = 10
block_h = 180
small_block_h = 100
small_block_w = 100
large_block_w = 800
text_offset_x = 50
sum_block_w = 2*small_block_w + 2*gap + large_block_w

class Lesson:
    def __init__(self, time: str, place: str, title: str):
        self.time = time
        self.place = place.upper()
        self.title = title.upper()

class Place:
    def __init__(self, name: str, address: str, abbrv: str):
        self.name = name
        self.address = address
        self.abbrv = abbrv

class Drawer:
    def __init__(self):
        self.table_x = 0
        self.table_y = gap
        self.svg_items = []
    
    def reserve_left(self, x: int):
        self.table_x += x

    def draw_title(self, title: str, width: int):
        title = draw.Text(title, 200, 0, 0, center=True, fill=violet, font_family='Cascadia Code', transform=f'translate({width/2},{self.table_y/2}) rotate(-90)')
        self.svg_items.append(title)

    def draw_place(self, place):
        bg = draw.Rectangle(self.table_x, self.table_y, sum_block_w, small_block_h, fill=violet, rx=10, ry=10)
        abbrv = draw.Text(place.abbrv, 80, self.table_x+30, self.table_y+80)
        name = draw.Text(place.name, 40, self.table_x+270, self.table_y+50)
        address = draw.Text(place.address, 30, self.table_x+270, self.table_y+80)
        self.table_y += small_block_h + gap
        self.svg_items.extend([bg, abbrv, name, address])
    
    def draw_time(self, time, place):
        block_x = self.table_x + small_block_w + gap
        text_x = block_x + small_block_w/4
        text_y = self.table_y + block_h/2
        bg = draw.Rectangle(block_x, self.table_y, small_block_w, block_h, fill=violet, rx=10, ry=10)
        time = draw.Text(time, 35, 0, 0, center=True, transform=f'translate({text_x},{text_y}) rotate(-90)')
        place = draw.Text(place, 35, 0, 0, center=True, transform=f'translate({text_x+small_block_w/2},{text_y}) rotate(-90)')
        self.svg_items.extend([bg, time, place])

    def draw_lesson(self, lesson):
        self.draw_time(lesson.time, lesson.place)
        block_x = self.table_x + 2*gap + 2*small_block_w
        bg = draw.Rectangle(block_x, self.table_y, large_block_w, block_h, fill=violet, rx=10, ry=10)
        title = draw.Text(lesson.title, 60, block_x+30, self.table_y+80)

        self.table_y += block_h + gap
        self.svg_items.extend([bg, title])

    def draw_day(self, day_name, lessons):
        day_block_h = block_h*len(lessons) + gap*(len(lessons)-1)
        text_x = self.table_x + small_block_w/2
        text_y = self.table_y + day_block_h/2
        bg = draw.Rectangle(self.table_x, self.table_y, small_block_w, day_block_h, fill=violet, rx=10, ry=10)
        day = draw.Text(day_name, 35, 0, 0, center=True, transform=f'translate({text_x},{text_y}) rotate(-90)')
        self.svg_items.extend([bg, day])
        for lesson in lessons:
            self.draw_lesson(lesson)


    def generate(self, png=False):
        self.table_x += gap
        drawing = draw.Drawing(self.table_x + sum_block_w, self.table_y, fill='white', font_family='Magnetik', font_weight='bold')
        drawing.append(draw.Rectangle(0, 0, self.table_x + sum_block_w, self.table_y))
        for drawn_item in self.svg_items:
            drawing.append(drawn_item)
        drawing.save_svg('example.svg')
        if png:
            drawing.save_png('example.png')
        