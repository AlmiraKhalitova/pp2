import pygame
import math
pygame.init()
size = width, height = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Plot of main trigonometric functions")
font = pygame.font.SysFont('times-new-roman', 20)
is_going = True

white, black = (255, 255, 255), (0, 0, 0)
red, blue = (255, 0, 0), (0, 0, 255)
PI = math.pi

x_axis_points = ['-3п', ' 5п', '-2п', ' 3п', '-п ', ' п ', ' 0 ', ' п ', ' п ', ' 3п', ' 2п', ' 5п', ' 3п']
x_axis_points_extra1 = ['', '_ ', '', '_ ', '', '_ _', '', '   _', '', '   ', '', '   ', '']
x_axis_points_extra2 = ['', '  2', '', '  2', '', ' 2', '', ' 2', '', '  2', '', '  2', '']
y_axis_points = [' 1.00', ' 0.75', ' 0.50', ' 0.25', ' 0.00', '-0.25', '-0.50', '-0.75', '-1.00']

while is_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_going = False
    screen.fill(white)

    pygame.draw.rect(screen, black, (70, 10, 660, 540), 2) 
    pygame.draw.line(screen, black, (70, 280), (730, 280), 3)  
    pygame.draw.line(screen, black, (400, 10), (400, 550), 3)  
    pygame.draw.line(screen, black, (70, 40), (730, 40))  
    pygame.draw.line(screen, black, (70, 520), (730, 520))  
    pygame.draw.line(screen, black, (100, 10), (100, 550)) 
    pygame.draw.line(screen, black, (700, 10), (700, 550))  

    pygame.draw.line(screen, red, (530, 60), (570, 60))
    for x in range(530, 570, 7):
        pygame.draw.line(screen, blue, (x, 90), (x + 3, 90))

    for x in range(100, 701, 100):
        if x != 500:
            pygame.draw.line(screen, black, (x, 10), (x, 550))
        else:
            pygame.draw.line(screen, black, (x, 10), (x, 40))
            pygame.draw.line(screen, black, (x, 100), (x, 550))
    for x in range(100, 701, 50):
        pygame.draw.line(screen, black, (x, 10), (x, 30))
        pygame.draw.line(screen, black, (x, 550), (x, 530))
    for x in range(100, 701, 25):
        pygame.draw.line(screen, black, (x, 10), (x, 20))
        pygame.draw.line(screen, black, (x, 550), (x, 540))

    for y in range(40, 521, 60):
        pygame.draw.line(screen, black, (70, y), (730, y))
    for y in range(40, 521, 30):
        pygame.draw.line(screen, black, (70, y), (90, y))
        pygame.draw.line(screen, black, (710, y), (730, y))
    for y in range(40, 521, 15):
        pygame.draw.line(screen, black, (70, y), (80, y))
        pygame.draw.line(screen, black, (720, y), (730, y))

    for x in range(100, 700):
        sin_y1 = 240 * math.sin((x - 100) / 100 * PI)
        sin_y2 = 240 * math.sin((x - 99) / 100 * PI)
        pygame.draw.aalines(screen, red, False, [(x, 280 + sin_y1), ((x + 1), 280 + sin_y2)])

    for x in range(100, 700, 3):
        cos_y1 = 240 * math.cos((x - 100) / 100 * PI)
        cos_y2 = 240 * math.cos((x - 99) / 100 * PI)
        pygame.draw.aalines(screen, blue, False, [(x, 280 + cos_y1), ((x + 1), 280 + cos_y2)])

    screen.blit(font.render('sin(x)', False, black), (475, 45))
    screen.blit(font.render('cos(x)', False, black), (475, 75))
    screen.blit(font.render('X', False, black), (393, 575))

    for x in range(100, 701, 50):
        screen.blit(font.render(x_axis_points[(x - 100) // 50], False, black), (x - 10, 550))
        screen.blit(font.render(x_axis_points_extra1[(x - 100) // 50], False, black), (x - 20, 550))
        screen.blit(font.render(x_axis_points_extra2[(x - 100) // 50], False, black), (x - 10, 570))
    for y in range(40, 521, 60):
        screen.blit(font.render(y_axis_points[(y - 40) // 60], False, black), (25, (y - 10)))

    pygame.display.flip()
pygame.quit()