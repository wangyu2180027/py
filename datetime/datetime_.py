import pygame as pg, sys
pg.init()
# スクリーンセット
screen = pg.display.set_mode((800, 600))

##################
#必要に応じて処理書く
##################

# 描画用のループ
while True:
    # スクリーンの背景色
    screen.fill(pg.Color("WHITE"))
    # 再描画
    pg.display.update()
# 更新の速さ（1秒間に６０回以下実行）
    pg.time.Clock().tick(60)

# ウィンドウの閉じるを押したとき終了
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
