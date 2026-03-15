import pygame
import random
import sys

# 初始化pygame
pygame.init()

# 游戏常量
WIDTH, HEIGHT = 800, 600
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE

# 颜色定义
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# 方向常量
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# 设置游戏窗口
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("贪吃蛇游戏")

# 时钟控制游戏速度
clock = pygame.time.Clock()
FPS = 10


def draw_grid():
    """绘制网格线"""
    for x in range(0, WIDTH, GRID_SIZE):
        pygame.draw.line(screen, (40, 40, 40), (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, (40, 40, 40), (0, y), (WIDTH, y))


def draw_snake(snake):
    """绘制蛇"""
    for segment in snake:
        rect = pygame.Rect((segment[0] * GRID_SIZE, segment[1] * GRID_SIZE),
                           (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, GREEN, rect)
        # 绘制蛇的眼睛
        if segment == snake[0]:  # 头部
            eye_size = GRID_SIZE // 5
            if snake[0][0] - snake[1][0] == 1:  # 向右
                pygame.draw.circle(screen, WHITE,
                                   (segment[0] * GRID_SIZE + GRID_SIZE - eye_size,
                                    segment[1] * GRID_SIZE + eye_size),
                                   eye_size)
                pygame.draw.circle(screen, WHITE,
                                   (segment[0] * GRID_SIZE + GRID_SIZE - eye_size,
                                    segment[1] * GRID_SIZE + GRID_SIZE - eye_size),
                                   eye_size)
            elif snake[0][0] - snake[1][0] == -1:  # 向左
                pygame.draw.circle(screen, WHITE,
                                   (segment[0] * GRID_SIZE + eye_size,
                                    segment[1] * GRID_SIZE + eye_size),
                                   eye_size)
                pygame.draw.circle(screen, WHITE,
                                   (segment[0] * GRID_SIZE + eye_size,
                                    segment[1] * GRID_SIZE + GRID_SIZE - eye_size),
                                   eye_size)
            elif snake[0][1] - snake[1][1] == 1:  # 向下
                pygame.draw.circle(screen, WHITE,
                                   (segment[0] * GRID_SIZE + eye_size,
                                    segment[1] * GRID_SIZE + GRID_SIZE - eye_size),
                                   eye_size)
                pygame.draw.circle(screen, WHITE,
                                   (segment[0] * GRID_SIZE + GRID_SIZE - eye_size,
                                    segment[1] * GRID_SIZE + GRID_SIZE - eye_size),
                                   eye_size)
            elif snake[0][1] - snake[1][1] == -1:  # 向上
                pygame.draw.circle(screen, WHITE,
                                   (segment[0] * GRID_SIZE + eye_size,
                                    segment[1] * GRID_SIZE + eye_size),
                                   eye_size)
                pygame.draw.circle(screen, WHITE,
                                   (segment[0] * GRID_SIZE + GRID_SIZE - eye_size,
                                    segment[1] * GRID_SIZE + eye_size),
                                   eye_size)


def draw_food(food):
    """绘制食物"""
    rect = pygame.Rect((food[0] * GRID_SIZE, food[1] * GRID_SIZE),
                       (GRID_SIZE, GRID_SIZE))
    pygame.draw.rect(screen, RED, rect)


def generate_food(snake):
    """生成食物，确保不会出现在蛇身上"""
    while True:
        x = random.randint(0, GRID_WIDTH - 1)
        y = random.randint(0, GRID_HEIGHT - 1)
        food = (x, y)
        if food not in snake:
            return food


def show_game_over(score):
    """显示游戏结束画面"""
    font = pygame.font.SysFont('SimHei', 72)
    small_font = pygame.font.SysFont('SimHei', 36)

    game_over_text = font.render('游戏结束', True, WHITE)
    score_text = small_font.render(f'得分: {score}', True, WHITE)
    restart_text = small_font.render('按R键重新开始', True, WHITE)

    screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2,
                                 HEIGHT // 2 - 100))
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2,
                             HEIGHT // 2 + 50))
    screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2,
                               HEIGHT // 2 + 100))

    pygame.display.update()


def main():
    """游戏主函数"""
    # 初始化蛇
    snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
    direction = RIGHT
    next_direction = RIGHT

    # 生成初始食物
    food = generate_food(snake)

    # 分数
    score = 0

    # 游戏状态
    game_over = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != DOWN:
                    next_direction = UP
                elif event.key == pygame.K_DOWN and direction != UP:
                    next_direction = DOWN
                elif event.key == pygame.K_LEFT and direction != RIGHT:
                    next_direction = LEFT
                elif event.key == pygame.K_RIGHT and direction != LEFT:
                    next_direction = RIGHT
                elif event.key == pygame.K_r and game_over:
                    # 重新开始游戏
                    snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
                    direction = RIGHT
                    next_direction = RIGHT
                    food = generate_food(snake)
                    score = 0
                    game_over = False

        if not game_over:
            # 更新方向
            direction = next_direction

            # 计算新头部位置
            head_x, head_y = snake[0]
            new_head = (head_x + direction[0], head_y + direction[1])

            # 检查是否撞墙
            if (new_head[0] < 0 or new_head[0] >= GRID_WIDTH or
                    new_head[1] < 0 or new_head[1] >= GRID_HEIGHT):
                game_over = True

            # 检查是否撞到自己
            if new_head in snake:
                game_over = True

            # 添加新头部
            snake.insert(0, new_head)

            # 检查是否吃到食物
            if new_head == food:
                score += 10
                food = generate_food(snake)
                # 增加游戏速度
                global FPS
                FPS = min(20, 10 + score // 100)
            else:
                # 如果没吃到食物，移除尾部
                snake.pop()

            # 绘制游戏元素
            screen.fill(BLACK)
            draw_grid()
            draw_snake(snake)
            draw_food(food)

            # 显示分数
            font = pygame.font.SysFont('SimHei', 24)
            score_text = font.render(f'分数: {score}', True, WHITE)
            screen.blit(score_text, (10, 10))
        else:
            # 显示游戏结束画面
            show_game_over(score)

        # 更新显示
        pygame.display.update()

        # 控制游戏速度
        clock.tick(FPS)


if __name__ == "__main__":
    main()
