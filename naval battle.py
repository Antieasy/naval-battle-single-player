import pygame, random

WINDOWWIDTH = 800
WINDOWHEIGHT = 600
pygame.init()
win = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption("Морской бой в одностроннем порядке")
win.fill((255,255,255))
step = 40
x_start = 100
y_start = 100
x_end = 500
y_end = 500
ships = list()
byk = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'К']
history_game = list()
mode = 0

def text(message, size, x, y, color=(0, 0, 0)):
    message = message
    font_color = color
    font_type = 'Robotoblack.ttf'
    font_size = size
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True,  font_color)
    win.blit(text, (x, y))

def check(kord):
    for i in ships:
        if kord in i:
            return 0
    return 1

def draw(pos): # рисуем точку или крестик
    def id():
        for i in ships:
            if (n_x, n_y) in i:
                return ships.index(i), i.index((n_x,n_y))

    if pos[0] > x_start and pos[0] < x_end:
        if pos[1] > y_start and pos[1] < y_end:
            n_x = (pos[0] - x_start) // step
            n_y = (pos[1] - y_start) // step
            pygame.draw.rect(win, (255, 255, 255), (WINDOWWIDTH // 2 - 100, 550, WINDOWWIDTH // 2, 600)) #закрашиваем текст на экране
            pygame.draw.rect(win, (255, 255, 255), (WINDOWWIDTH // 2 + 150, 50, WINDOWWIDTH // 2 + 200, 600)) #закрашиваем текст на экране
            l = 100
            for i in ships:
                text(str(i), 10, WINDOWWIDTH // 2 + 150, l)
                l += 20
            if not check((n_x, n_y)):
                id1, id2 = id()
                pygame.draw.line(win, (255,0,0), (x_start + n_x * step,y_start + step * n_y),
                                 (x_start + (n_x + 1) * step, y_start + (n_y + 1)* step),2)
                pygame.draw.line(win, (255, 0, 0), (x_start + (n_x + 1) * step, y_start + step * n_y),
                                 (x_start + n_x * step, y_start + (n_y + 1) * step), 2)
                del ships[id1][id2]
                if not ships[id1]:
                    text('Убил', 20, WINDOWWIDTH // 2 - 100, 550)
                else:
                    text('Ранил', 20, WINDOWWIDTH // 2 - 100, 550)


            else:
                if (n_x, n_y) not in history_game:
                    pygame.draw.circle(win,(0,90,32),(x_start + n_x * step + step//2,y_start + step * n_y + step // 2), 2, 1)
                    global mode
                    if mode > 0:
                        pygame.draw.rect(win, (255,255,255), (WINDOWWIDTH - 300, 30, WINDOWWIDTH, 50))
                        mode -= 1
                    else:
                        win.fill((255,255,255))
                        text('Компьютер выиграл', 30, WINDOWWIDTH // 2 - 150, WINDOWHEIGHT// 2)
            history_game.append((n_x,n_y))

def creat_ships():
    zone = []

    def generate_koord():
        x, y = random.randint(0, 9), random.randint(0, 9)
        for i in ships:
            if (x, y) in i or (x,y) in zone:
                while (x, y) in i or (x,y) in zone:
                    x, y = random.randint(0, 9), random.randint(0, 9)
        return x, y

    def add_ships(*number):
        k__ = list()
        for count in number:
            k__.append(count)
            if (count[0] + 1, count[1]) not in zone:
                zone.append((count[0] + 1, count[1]))
            if (count[0] - 1, count[1]) not in zone:
                zone.append((count[0] - 1, count[1]))
            if (count[0], count[1] + 1) not in zone:
                zone.append((count[0], count[1] + 1))
            if (count[0], count[1] - 1) not in zone:
                zone.append((count[0], count[1] - 1))
            if (count[0] - 1, count[1] + 1) not in zone:
                zone.append((count[0] - 1, count[1] + 1))
            if (count[0] + 1, count[1] + 1) not in zone:
                zone.append((count[0] + 1, count[1] + 1))
            if (count[0] - 1, count[1] - 1) not in zone:
                zone.append((count[0] - 1, count[1] -1))
            if (count[0] + 1, count[1] - 1) not in zone:
                zone.append((count[0] + 1, count[1] - 1))
        ships.append(k__)

    for one in range(4):
        n_x, n_y = generate_koord()
        add_ships((n_x,n_y))

    two = 3
    while two > 0:

        n_x, n_y = generate_koord()
        if check((n_x + 1 , n_y)) and n_x < 9 and (n_x + 1 , n_y) not in zone:
            add_ships((n_x, n_y), (n_x + 1, n_y))
        elif check((n_x - 1 , n_y)) and n_x > 0 and (n_x - 1, n_y) not in zone:
            add_ships((n_x, n_y), (n_x - 1, n_y))

        elif check((n_x, n_y + 1)) and n_y < 9 and (n_x, n_y + 1) not in zone:
            add_ships((n_x, n_y), (n_x , n_y + 1))

        elif check((n_x, n_y - 1)) and n_y > 0 and (n_x, n_y - 1) not in zone:
            add_ships((n_x, n_y), (n_x, n_y - 1))
        else:
            two += 1
        two -= 1
    three = 2
    while three > 0:

        n_x, n_y = generate_koord()
        if check((n_x + 1 , n_y)) and n_x < 8 and (n_x + 1 , n_y) not in zone\
                and check((n_x + 2 , n_y)) and (n_x + 2 , n_y) not in zone:
                add_ships((n_x, n_y), (n_x + 1, n_y), (n_x + 2, n_y))

        elif check((n_x - 1 , n_y)) and n_x > 1 and (n_x - 1, n_y) not in zone\
                and check((n_x - 2 , n_y)) and (n_x - 2, n_y) not in zone:
                add_ships((n_x, n_y), (n_x - 1, n_y), (n_x - 2, n_y))

        elif check((n_x, n_y + 1)) and n_y < 8 and (n_x, n_y + 1) not in zone\
                and check((n_x, n_y + 2)) and (n_x, n_y + 2) not in zone:
                add_ships((n_x, n_y), (n_x, n_y + 1), (n_x, n_y + 2))

        elif check((n_x, n_y - 1)) and n_y > 1 and (n_x, n_y - 1) not in zone\
                and check((n_x, n_y - 2)) and (n_x, n_y - 2) not in zone:
                add_ships((n_x, n_y), (n_x, n_y - 1), (n_x, n_y - 2))


        else:
            three += 1
        three -= 1

    four = 1
    while four > 0:

        n_x, n_y = generate_koord()
        if check((n_x + 1, n_y)) and n_x < 7 and (n_x + 1 , n_y) not in zone\
                and check((n_x + 2, n_y)) and (n_x + 2 , n_y) not in zone \
                and check((n_x + 3, n_y)) and (n_x + 3, n_y) not in zone:
                add_ships((n_x, n_y), (n_x + 1, n_y), (n_x + 2, n_y), (n_x + 3, n_y))

        elif check((n_x - 1 , n_y)) and n_x > 2 and (n_x - 1, n_y) not in zone\
                and check((n_x - 2 , n_y)) and (n_x - 2, n_y) not in zone \
                and check((n_x - 3, n_y)) and (n_x - 3, n_y) not in zone:
                add_ships((n_x, n_y), (n_x - 1, n_y), (n_x - 2, n_y), (n_x - 3, n_y))

        elif check((n_x, n_y + 1)) and n_y < 7 and (n_x, n_y + 1) not in zone\
                and check((n_x, n_y + 2)) and (n_x, n_y + 2) not in zone \
                and check((n_x, n_y + 3)) and (n_x, n_y + 3) not in zone:
                add_ships((n_x, n_y), (n_x, n_y + 1), (n_x, n_y + 2), (n_x, n_y + 3))
        elif check((n_x, n_y - 1)) and n_y > 2 and (n_x, n_y - 1) not in zone\
                and check((n_x, n_y - 2)) and (n_x, n_y - 2) not in zone\
                and check((n_x, n_y - 3)) and (n_x, n_y - 3) not in zone:
                add_ships((n_x, n_y), (n_x, n_y - 1), (n_x, n_y - 2), (n_x, n_y - 3))

        else:
            four += 1
        four -= 1



def board():
    pygame.draw.line(win, (0, 0, 0), (x_start, y_start), (x_end, y_start), 1)
    pygame.draw.line(win, (0, 0, 0), (x_end, y_end), (x_end, y_start), 1)
    pygame.draw.line(win, (0, 0, 0), (x_start, y_start), (x_start, y_end), 1)
    pygame.draw.line(win, (0, 0, 0), (x_start, y_end), (x_end, y_end), 1)
    z__ = 0
    for i in range(x_start, x_end + 1, step): # вертикальные линии
        pygame.draw.line(win, (0, 0, 0), (i, y_start), (i, y_end), 1)
        if z__ != 10:
            text(byk[z__], 20, x_start + 12 + z__ * step, y_start - 25)
            z__ += 1
    z__ = 0
    for i in range(y_start, y_end, step): # горизонтальные линии
        pygame.draw.line(win, (0, 0, 0), (x_start, i), (x_end, i), 1)
        if z__ < 9:
            text(str(z__ + 1), 20, x_start - 25, y_start + 12 + z__ * step)
        else:
            text(str(z__ + 1), 20, x_start - 30, y_start + 12 + z__ * step)
        z__ += 1


def menu():
    text('Выберите режим игры:', 30, WINDOWWIDTH//2 - 150, y_start)
    text('Легкий -  нажмите 1', 25, WINDOWWIDTH//2 - 150, y_start + 100)
    text('Средний - нажмите 2', 25, WINDOWWIDTH//2 - 150, y_start + 200)
    text('Сложный - нажмите 3', 25, WINDOWWIDTH//2 - 150, y_start + 300)

activity = True

# рисуем квадрат 10 на 10.

menu()
while mode == 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            activity = False
            mode = - 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                mode = 200
            elif event.key == pygame.K_2:
                mode = 15
            elif event.key == pygame.K_3:
                mode = 10
    pygame.display.update()

win.fill((255,255,255))
board()
creat_ships()
while activity:
    text('Попыток осталось: ' + str(mode), 20, WINDOWWIDTH - 300, 30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            activity = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                draw(event.pos)
    k = 1
    for i in ships:
        if i:
            k = 0
            break
    if k:
        win.fill((255,255,255))
        text('Вы выиграли, гц!', 30, WINDOWWIDTH // 2 - 100, WINDOWHEIGHT // 2)
    pygame.display.update()
pygame.quit()