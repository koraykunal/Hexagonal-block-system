from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import math
import time

p_time = time.time()

app = Ursina()

model = 'hexagon_.obj'
texture = load_texture('hex.png')

far = Vec3(0, 0, 0)

Grid(10, 10, mode='line', thickness=1)


class Tile(Button):
    def __init__(self, model, position=(0, 0, 0), collider='mesh'):
        self.model = model
        super().__init__(
            parent=scene,
            position=position,
            model=load_model(model),
            texture=texture,
            color=color.color(0, 0, random.uniform(.9, 1.0)),
            highlight_color=color.lime,
        )
        self.collider = 'mesh'

    def input(self, key):
        global far
        if self.hovered:
            if key == 'left mouse down':
                # far = Vec3(0,0,0)
                direction = mouse.world_point - self.position
                print(direction[0])
                if direction[0] > 0:
                    angle = math.atan(direction[2] / direction[0]) * 57.2957795
                    print('angle', angle)
                if direction[0] < 0:
                    angle = (math.atan(direction[2] / direction[0]) * 57.2957795 + 180)
                    print('angle', angle)
                var = (((angle + 30) // 60) % 6) + 1
                print(var)
                if var == 1:
                    far = Vec3(1.72, 0, 0)
                elif var == 2:
                    far = Vec3(0.86, 0, 1.5)
                elif var == 3:
                    far = Vec3(-0.86, 0, 1.5)
                elif var == 4:
                    far = Vec3(-1.72, 0, 0)
                elif var == 5:
                    far = Vec3(-0.86, 0, -1.5)
                elif var == 6:
                    far = Vec3(0.86, 0, -1.5)
                print(far)
                voxel = Tile(position=self.position + far, model=model)

            if key == 'right mouse down':
                destroy(self)


def create(x, y):
    for z in range(-x, x):
        for x in range(-y, y):
            if z % 2 == 1:
                tile = Tile(model=model, position=((x * 1.72) - 0.86, 0, (z * 1.5)))
            else:
                tile = Tile(model=model, position=(x * 1.72, 0, (z * 1.5)))


# camera.position = (0, 15, -20)
# camera.rotation_x = 37

create(5, 5)
player = FirstPersonController()

c_time = time.time()
app.run()
print("time :" ,c_time - p_time)
