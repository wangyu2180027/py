import pygame as pg, sys
pg.init()
screen = pg.display.set_mode((800, 600))
img1 = pg.image.load("images.jpg")
img2 = pg.image.load("5e7e8b864959fb80f69ee8ce53ac1a93_c_700_395.png")
img1 = pg.transform.scale(img1,(400,300))
img2 = pg.transform.scale(img2,(500,400))
font = pg.font.Font(None, 100)
textimg = font.render("seifu!", True, pg.Color("black"))

# 2.この下をずっとループする
while True:
    # 3.画面を初期化する
    screen.fill(pg.Color("WHITE"))
    # 5.絵を描いたり、判定したりする
    screen.blit(textimg, (300, 100))
    screen.blit(img1, (1,1))
    screen.blit(img2,(200,200))

    # 6.画面を表示する
    pg.display.update()
    # 7.閉じるボタンが押されたら、終了する
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()