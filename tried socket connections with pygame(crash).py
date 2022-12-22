import pygame
import socket

# Initialize pygame
pygame.init()
window_size = (400, 400)
screen = pygame.display.set_mode(window_size)

pygame.display.set_caption('Battleships')

cell_width = int(window_size[0] / 10)
cell_height = int(window_size[1] / 10)

# Set the grid color to white
grid_color = (255, 255, 255)

# Set the cell color to red
cell_color = (255, 0, 0)


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 8000))
sock.listen()

# Set up the main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Accept a connection from a client
    conn, addr = sock.accept()

    # Receive data from the client
    data = conn.recv(1024).decode()

    # Split the data into x and y coordinates
    x, y = map(int, data.split(','))

    # Draw the grid
    for i in range(10):
        for j in range(10):
            if i == x and j == y:
                pygame.draw.rect(screen, cell_color, (i * cell_width, j * cell_height, cell_width, cell_height))
            else:
                pygame.draw.rect(screen, grid_color, (i * cell_width, j * cell_height, cell_width, cell_height))

    pygame.display.flip()

# Close the socket and quit pygame
sock.close()
pygame.quit()