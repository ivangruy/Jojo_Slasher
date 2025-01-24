import pygame

FPS = 50

def terminate():
    pygame.quit()
    sys.exit()

def start_screen():
    intro_text = ["ЗАСТАВКА", "",
                  "Правила игры",
                  "Если в правилах несколько строк,",
                  "приходится выводить их построчно"]
    clock = pygame.time.Clock()
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYUP or \
                    event.type == pygame.MOUSEBUTTONUP:
                return menu()
        pygame.display.flip()
        clock.tick(FPS)

def menu():
    # Размеры окна
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Меню")

    # Цвета
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GRAY = (128, 128, 128)

    # Шрифты
    font = pygame.font.Font(None, 36)

    # Кнопки
    button_width = 150
    button_height = 50
    button_margin = 20

    # Листы и кнопки
    m = ["New Game", "Continue", "Quit"]
    pages = 2
    buttons_per_page = 3
    current_page = 0
    buttons = []

    # Создание кнопок
    for page in range(pages):
        menu_buttons = []
        for i in range(buttons_per_page):
            x = WIDTH // 8
            y = (WIDTH * 1.5 - button_width * buttons_per_page - button_margin * (buttons_per_page - 1)) // 2 + (
                        button_width + button_margin) * i/2
            button_rect = pygame.Rect(x, y - button_height, button_width, button_height)
            button_text = font.render(m[i], True, BLACK)
            menu_buttons.append((button_rect, button_text))
        buttons.append(menu_buttons)


    # Основной цикл
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # Левая кнопка мыши
                    for i in range(buttons_per_page):
                        if buttons[current_page][i][0].collidepoint(event.pos):
                            if i == 1:
                                return slots()
                        print(f"Нажата кнопка {i+1+(current_page*4)} на странице {current_page+1}")

        screen.fill(WHITE)


        # Отрисовка кнопок
        for page in range(pages):
            for button_rect, button_text in buttons[page]:
                if abs(page - current_page) <= 0: # Отображать только текущую страницу и соседние
                    pygame.draw.rect(screen, GRAY, button_rect)
                    text_rect = button_text.get_rect(center=button_rect.center)
                    screen.blit(button_text, text_rect)



        pygame.display.flip()

def select_level():
    # Размеры окна
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Перелистывание страниц")

    # Цвета
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GRAY = (128, 128, 128)

    # Шрифты
    font = pygame.font.Font(None, 36)

    # Кнопки
    button_width = 150
    button_height = 50
    button_margin = 20
    next_page_button = pygame.Rect(WIDTH - button_width - button_margin, HEIGHT - button_height - button_margin,
                                   button_width, button_height)
    prev_page_button = pygame.Rect(button_margin, HEIGHT - button_height - button_margin, button_width, button_height)
    next_page_text = font.render("Next Page", True, BLACK)
    prev_page_text = font.render("Prev Page", True, BLACK)

    # Листы и кнопки
    pages = 2
    buttons_per_page = 4
    current_page = 0
    buttons = []

    # Создание кнопок
    for page in range(pages):
        page_buttons = []
        for i in range(buttons_per_page):
            x = (WIDTH - button_width * buttons_per_page - button_margin * (buttons_per_page - 1)) // 2 + (
                        button_width + button_margin) * i
            y = HEIGHT // 2 + (page - current_page) * HEIGHT  # Позиция Y в зависимости от текущей страницы
            button_rect = pygame.Rect(x, y - button_height // 2, button_width, button_height)
            if page == 0:
                button_text = font.render(f"Button {i + 1}", True, BLACK)
            else:
                button_text = font.render(f"Button {i + 5}", True, BLACK)
            page_buttons.append((button_rect, button_text))
        buttons.append(page_buttons)

    # Основной цикл
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Левая кнопка мыши
                    for i in range(buttons_per_page):
                        if buttons[current_page][i][0].collidepoint(event.pos):
                            print(f"Нажата кнопка {i + 1 + (current_page * 4)} на странице {current_page + 1}")

                elif event.button == 4:  # Скролл вверх
                    current_page = max(0, current_page - 1)
                    for page in range(pages):
                        for i in range(buttons_per_page):
                            buttons[page][i] = (pygame.Rect(buttons[page][i][0].x, HEIGHT // 2 + (page - current_page) *
                                                            HEIGHT - button_height // 2, button_width, button_height),
                                                buttons[page][i][1])
                elif event.button == 5:  # Скролл вниз
                    current_page = min(pages - 1, current_page + 1)
                    for page in range(pages):
                        for i in range(buttons_per_page):
                            buttons[page][i] = (pygame.Rect(buttons[page][i][0].x, HEIGHT // 2 + (page - current_page) *
                                                            HEIGHT - button_height // 2,
                                                            button_width, button_height), buttons[page][i][1])
                if next_page_button.collidepoint(event.pos):
                    current_page = min(pages - 1, current_page + 1)
                    for page in range(pages):
                        for i in range(buttons_per_page):
                            buttons[page][i] = (pygame.Rect(buttons[page][i][0].x, HEIGHT // 2 + (
                                    page - current_page) * HEIGHT - button_height // 2, button_width, button_height),
                                                buttons[page][i][1])
                elif prev_page_button.collidepoint(event.pos):
                    current_page = max(0, current_page - 1)
                    for page in range(pages):
                        for i in range(buttons_per_page):
                            buttons[page][i] = (pygame.Rect(buttons[page][i][0].x, HEIGHT // 2 + (
                                    page - current_page) * HEIGHT - button_height // 2, button_width, button_height),
                                                buttons[page][i][1])
        screen.fill(WHITE)

        # Отрисовка кнопок
        for page in range(pages):
            for button_rect, button_text in buttons[page]:
                if abs(page - current_page) <= 0:  # Отображать только текущую страницу и соседние
                    pygame.draw.rect(screen, GRAY, button_rect)
                    text_rect = button_text.get_rect(center=button_rect.center)
                    screen.blit(button_text, text_rect)
        pygame.draw.rect(screen, GRAY, next_page_button)
        pygame.draw.rect(screen, GRAY, prev_page_button)
        screen.blit(next_page_text, next_page_text.get_rect(center=next_page_button.center))
        screen.blit(prev_page_text, prev_page_text.get_rect(center=prev_page_button.center))

        pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    start_screen()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    terminate()