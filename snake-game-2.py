from tkinter import *
import random

class snake(Tk):
    box_width = 25
    box_height = 25
    root_width = 1325
    root_height = 750

    snakex = 500
    snakey = 300
    dirction = "right"
    size = 8

    bodyx = [snakex]
    bodyy = [snakey]

    xbox=root_width/box_width
    ybox=root_height/box_height
    applex=0
    appley=0

    score=0
    st = "Score : " + str(score)
    running=True

    def __init__(self):
        super().__init__()
        self.geometry(f"{snake.root_width}x{snake.root_height}")
        self.canvas = Canvas(self, bg="black")
        self.canvas.pack(expand=YES, fill=BOTH)
        self.resizable(False, False)

        for i in range(1, snake.size):
            snake.bodyx.append(snake.bodyx[len(snake.bodyx) - 1] - snake.box_width)
            snake.bodyy.append(300)

        snake.applex = (random.randint(0, snake.xbox-1) * snake.box_width)
        snake.appley = (random.randint(0, snake.ybox-1) * snake.box_height)


    def draw(self):
        self.canvas.delete(ALL)
        """
        for i in range(0, snake.root_width, snake.box_width):
            self.canvas.create_line(i, 0, i, snake.root_height, fill="green")

        for i in range(0, snake.root_height, snake.box_height):
            self.canvas.create_line(0, i, snake.root_width, i, fill="green")
        """
        for i in range(1, snake.size):
            self.canvas.create_rectangle(snake.bodyx[i], snake.bodyy[i], snake.bodyx[i] + snake.box_width,
                                         snake.bodyy[i] + snake.box_height, fill="light green")

        self.myhead = self.canvas.create_rectangle(snake.bodyx[0], snake.bodyy[0], snake.bodyx[0] + snake.box_width,
                                                   snake.bodyy[0] + snake.box_height, fill="dark green")

        self.canvas.create_text((snake.root_width/2)-len(snake.st)/2,25,text=snake.st,
                                fill=("white" if snake.running else "red"),font="bold")

        self.apple=self.canvas.create_oval(snake.applex,snake.appley,snake.applex+snake.box_width,snake.appley+snake.box_height,
                                           fill=("red" if snake.running else "black"))

    def changedirection(self, event):
        if event.keysym == "Up" and snake.dirction != "down":
            snake.dirction = "up"
        elif event.keysym == "Down" and snake.dirction != "up":
            snake.dirction = "down"
        elif event.keysym == "Right" and snake.dirction != "left":
            snake.dirction = "right"
        elif event.keysym == "Left" and snake.dirction != "right":
            snake.dirction = "left"

    def gameover(self):
        snake.st = f"Game Over\nyou scored {snake.score}"
        snake.running = False
    def checkcollison(self):
        if snake.snakex==snake.root_width and snake.dirction=="right":
           self.gameover()
        elif snake.snakey==snake.root_height and snake.dirction=="down":
           self.gameover()
        elif snake.snakex==-snake.box_width and snake.dirction=="left":
            self.gameover()
        elif snake.snakey==-snake.box_height and snake.dirction=="up":
            self.gameover()

    def checkapple(self):

        if snake.snakex==snake.applex and snake.snakey==snake.appley:
            snake.score+=1
            snake.size+=1
            snake.st="score : "+str(snake.score)
            snake.bodyx.append(snake.bodyx[(len(snake.bodyx)-1)])
            snake.bodyy.append(snake.bodyy[(len(snake.bodyy)-1)])
            snake.applex = (random.randint(0, snake.xbox) * snake.box_width)
            snake.appley = (random.randint(0, snake.ybox) * snake.box_height)

    def snakemove(self):

        for i in range(snake.size - 1, 0, -1):
            snake.bodyx[i] = snake.bodyx[i - 1]
            snake.bodyy[i] = snake.bodyy[i - 1]

        if snake.dirction == "right":
            snake.snakex += snake.box_width
        elif snake.dirction == "left":
            snake.snakex -= snake.box_width
        elif snake.dirction == "up":
            snake.snakey -= snake.box_height
        elif snake.dirction == "down":
            snake.snakey += snake.box_height

        snake.bodyx[0] = snake.snakex
        snake.bodyy[0] = snake.snakey

    def bodycollision(self):

        for i in range(1,snake.size):
            if snake.snakex==snake.bodyx[i] and snake.snakey==snake.bodyy[i]:
                self.gameover()

    def automove(self):
        if snake.running:
            self.snakemove()
        self.checkcollison()
        self.checkapple()
        self.bodycollision()
        self.draw()
        self.canvas.after(150, self.automove)


if __name__ == '__main__':
    root = snake()
    root.title("snake game")
    root.draw()
    root.bind("<Key>", root.changedirection)
    root.automove()
    root.mainloop()
