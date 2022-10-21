import pygame
import random
import time


def main():
    pygame.init()
    hard = int(input("输入难度,数字越大越难,0到5:")) * (-5) + 30
    overall_num = int(input('输入小球数量：'))
    a, num, x1, y1, x2, y2, black, white = 0, 0, 0, 0, 300, 300, (0, 0, 0, 255), (255, 255, 255, 255)
    exist = False
    screen = pygame.display.set_mode((800, 800), 0, 32)
    screen.fill(white)
    pygame.display.set_caption('1 wall 1 targets small')
    block = pygame.Surface((hard * 2, hard * 2), flags=pygame.HWSURFACE)
    block.fill(color=white)
    print('鼠标点击任意处开始游戏')
    while True:
        event = pygame.event.wait()
        if num == overall_num and a == 1:
            t2 = time.time()
            t = round(t2 - t1, 4)
            font = pygame.font.SysFont('华文细黑', 50)
            text = font.render('总计用时 ' + str(t) + ' s', True, black)
            rect = text.get_rect()
            rect.center = (400, 400)
            screen.blit(text, rect)
            screen.blit(block, (x2 - hard, y2 - hard))
            a += 1
        if event.type == pygame.QUIT:
            pygame.quit()
            with open('score.txt', 'a', encoding='utf-8') as f:
                write_text = '难度' + str(int((hard-30)/-5)) + '  小球数量为' + str(overall_num) + ' \t总用时：' + str(t) + ' s\n'
                f.write(write_text)

            exit('已记录数据，感谢游玩')

        if event.type == pygame.MOUSEBUTTONDOWN:
            if a == 0:
                for i in range(3, -1, -1):
                    print('开始倒计时:', i)
                    time.sleep(1)
                t1 = time.time()
                a += 1
            x1, y1 = event.pos
            if (x1 - x2) ** 2 + (y1 - y2) ** 2 <= hard ** 2:
                exist = False
                screen.blit(block, (x2 - hard, y2 - hard))
                num += 1
        if not exist and a != 0:
            x2 = random.randrange(0 + hard, 800 - hard)
            y2 = random.randrange(0 + hard, 800 - hard)
            pygame.draw.circle(screen, black, (x2, y2), hard)
            exist = True
        pygame.display.update()


if __name__ == '__main__':
    main()
