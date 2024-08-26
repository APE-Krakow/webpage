import drawsvg as draw
import yaml
from draw_utils import Lesson, Place, Drawer

days = {}
places = []
drawer = Drawer()

with open("zajecia.yaml", "rt") as file:
    data = yaml.safe_load(file)

for lesson in data["lessons"]:
    day_name = lesson["day"]
    if day_name not in days:
        days[day_name] = []
    days[day_name].append(Lesson(lesson["time"], lesson["place"], lesson["title"]))

drawer.reserve_left(300)

for place in data["places"]:
    places.append(Place(place["name"], place["address"], place["abbrv"]))

for place in places:
    drawer.draw_place(place)

for day, lessons in days.items():
    drawer.draw_day(day, lessons)

drawer.draw_title("APE KRAKÓW", 300)

drawer.generate(True)    







