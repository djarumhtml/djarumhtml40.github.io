import pygame
import sys
import random

# Inisialisasi Pygame
pygame.init()

# Pengaturan layar
WIDTH, HEIGHT = 600, 400
FPS = 10

# Warna
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Inisialisasi layar
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Oney Makan Buah")

# Inisialisasi font
font = pygame.font.Font(None, 36)

# Inisialisasi ular
snake = [(100, 100), (90, 100), (80, 100)]
snake_direction = (10, 0)  # Gerakan ke kanan
snake_speed = 10

# Inisialisasi buah
fruit = (random.randrange(1, (WIDTH // 10)) * 10, random.randrange(1, (HEIGHT // 10)) * 10)

# Inisialisasi score
score = 0

# Inisialisasi love
love_active = False
love_lines = [(100, 200), (140, 150), (180, 200), (220, 150), (260, 200)]
love_speed = 5

# Mulai permainan
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and snake_direction != (0, 10):
        snake_direction = (0, -10)
    if keys[pygame.K_DOWN] and snake_direction != (0, -10):
        snake_direction = (0, 10)
    if keys[pygame.K_LEFT] and snake_direction != (10, 0):
        snake_direction = (-10, 0)
    if keys[pygame.K_RIGHT] and snake_direction != (-10, 0):
        snake_direction = (10, 0)

    # Perbarui posisi ular
    snake = [(snake[0][0] + snake_direction[0], snake[0][1] + snake_direction[1])] + snake[:-1]

    # Cek apakah ular memakan buah
    if snake[0] == fruit:
        score += 1
        snake.append((0, 0))  # Tambah panjang ular
        fruit = (random.randrange(1, (WIDTH // 10)) * 10, random.randrange(1, (HEIGHT // 10)) * 10)

    # Cek apakah ular menabrak dinding
    if snake[0][0] < 0 or snake[0][0] >= WIDTH or snake[0][1] < 0 or snake[0][1] >= HEIGHT:
        print("Game Over! Score Anda:", score)
        pygame.quit()
        sys.exit()

    # Cek apakah ular menabrak dirinya sendiri
    if snake[0] in snake[1:]:
        print("Game Over! Score Anda:", score)
        pygame.quit()
        sys.exit()

    # Bersihkan layar
    screen.fill(WHITE)

    # Gambar ular
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], 10, 10))

    # Gambar buah
    pygame.draw.rect(screen, RED, (fruit[0], fruit[1], 10, 10))

    # Tampilkan skor
    score_text = font.render(f"Score: {score}", True, GREEN)
    screen.blit(score_text, (10, 10))

    # Cek apakah skor mencapai 6 untuk menampilkan love
    if score == 6 and not love_active:
        love_active = True

    # Tampilkan love jika aktif
    if love_active:
        for i in range(len(love_lines) - 1):
            pygame.draw.line(screen, RED, love_lines[i], love_lines[i + 1], 5)

        # Bergerakkan garis love ke atas
        love_lines = [(x, y - love_speed) for x, y in love_lines]

        # Cek apakah garis love mencapai bagian atas layar
        if love_lines[0][1] < 0:
            love_active = False  # Setel love menjadi tidak aktif

            # Tampilkan pesan cinta
            love_message = font.render("Sayangku, oneykuu i love you. can you be mine & i be yours?", True, RED)
            screen.blit(love_message, (50, 150))

            # Tampilkan pilihan "Yes" atau "No"
            response = input("Pilih 'Yes' atau 'No': ")
            if response.lower() == 'yes':
                love_message2 = font.render("Selamat! Kita sekarang pacaran. 💑", True, RED)
                screen.blit(love_message2, (50, 200))
            else:
                love_message3 = font.render("Oh, maaf kalau aku terlalu cepat. Mungkin lain kali ya. 😔", True, RED)
                screen.blit(love_message3, (50, 200))

            pygame.display.flip()

            # Hentikan permainan setelah menampilkan pesan cinta
            pygame.time.delay(3000)
            pygame.quit()
            sys.exit()

    pygame.display.flip()

    # Kontrol kecepatan ular
    pygame.time.Clock().tick(snake_speed)