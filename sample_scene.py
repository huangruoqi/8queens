from UI.scene import Scene
from UI.components.container import Container
from UI.components.button import Button
from UI.components.text import Text
from UI.components.slider import Slider
from block import Block
from UI.sound import Channel
from UI.utils import IMAGE, SOUND
from eight_queens import dfs

import pygame
from pygame.locals import *  # noqa


class SampleScene(Scene):
    def __init__(self, screen, *args, **kwargs):
        super(SampleScene, self).__init__(screen, *args, **kwargs)
        self.background_music = SOUND("castle.wav", Channel.BACKGROUND)
        self.speed = 1
        self.playing = False
        self.add(
            "play_pause",
            Button(
                image=IMAGE("play-solid.png"),
                height=50,
                x=130,
                y=700,
                animation="opacity",
                parameter={"factor": 0.5},
                on_click=lambda: self.play()
            ),
        )
        self.add(
            "next",
            Button(
                image=IMAGE("arrow-right-solid.png"),
                height=50,
                x=530,
                y=700,
                animation="opacity",
                parameter={"factor": 0.5},
                on_click=lambda: self.next()
            ),
        )
        

        def change_speed(val):
            self.speed = val

        bg = pygame.Surface([1, 1])
        bg.fill((0, 0, 0))

        self.add("bg", Container(bg, width=640, height=640, x=320, y=320))

        for i in range(8):
            for j in range(8):
                self.add(
                    f"block_{i}{j}",
                    Block(width=60, height=60, x=j * 80 + 40, y=i * 80 + 40),
                    layer_number=2,
                )
        self.add("label", Text("Speed:", x=250, y=700, size=30, align_mode="CENTER"))
        self.add(
            "slider",
            Slider(
                on_change=change_speed,
                interval=[1, 61],
                x=370,
                y=700,
                animation="opacity",
                parameter={"factor": 0.5},
                on_click=lambda: 0,
            ),
        )
        bg.fill((150, 150, 150))
        self.add("slider_bg", Container(bg, width=100, height=20, x=370, y=700))
        solutions = []
        self.gen = dfs(solutions, [])
        self.total_time = 0
        self.display_time = 3
        self.has2 = False

    def play(self):
        self.playing = True
        btn = self.get("play_pause")
        pos = btn.get_pos()
        btn.set_temp_image(IMAGE("pause-solid.png"), height=50).set_pos(pos)
        btn.on_click = lambda: self.pause()
        self.get("next").hide()

    def pause(self):
        self.playing = False
        btn = self.get("play_pause")
        btn.show()
        btn.on_click = lambda: self.play()
        self.get("next").show()

    def next(self):
        self.set_display(next(self.gen))

    def set_display(self, grid):
        self.has2 = False
        for i in range(8):
            for j in range(8):
                block = self.get(f"block_{i}{j}")
                block_value = grid[i][j]
                if block_value < 1:
                    block.change("empty")
                else:
                    if block_value == 1:
                        block.change("queen")
                    elif block_value == 2:
                        block.change("queen_win")
                    else:
                        block.change("red")
                self.has2 |= block_value == 2

    def update(self, delta_time, mouse_pos, clicked, pressed):
        super().update(delta_time, mouse_pos, clicked, pressed)
        if not self.playing:
            return
        self.total_time += delta_time
        self.display_time += delta_time
        if self.total_time > 1 / self.speed:
            self.next()
            if self.has2:
                self.pause()
            self.total_time = 0
