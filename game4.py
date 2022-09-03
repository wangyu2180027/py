# 1.ゲームの準備をする
import pygame as pg, sys
pg.init()
screen = pg.display.set_mode((800, 600))
myrect = pg.Rect(100,100,100,150)
img1 = pg.image.load("images.jpg")
img1 = pg.transform.scale(img1,(100,150))
# 2.この下をずっとループする
while True:
    # 3.画面を初期化する
    screen.fill(pg.Color("WHITE"))
    # 5.絵を描いたり、判定したりする
    myrect.x = myrect.x + 1
    pg.draw.rect(screen, pg.Color("RED"), myrect)
    screen.blit(img1,(300,300))
    # 6.画面を表示する
    pg.display.update()
    pg.time.Clock().tick(60)
    # 7.閉じるボタンが押されたら、終了する
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()