import pygame
import time
import copy

pygame.init()
SIDE = 1000
WINDOW = pygame.display.set_mode((SIDE, SIDE))
pygame.display.set_caption("Conway Game of Life")

def draw_board(screen, board, grid, cell_side):
	for i in range(grid):
		for j in range(grid):
			if board[i][j] == 0:
				pygame.draw.rect(screen, (0, 0, 0),
					             pygame.Rect(i*cell_side, j*cell_side,
					             	         cell_side, cell_side))
			else:
				pygame.draw.rect(screen, (255, 255, 255),
					             pygame.Rect(i*cell_side, j*cell_side,
					             	         cell_side, cell_side))

def neighbors(board, i, j):
	count = 0
	for _i in range(i-1, i+2):
		for _j in range(j-1, j+2):
			if not (_i == i and _j == j) and board[_i][_j] == 1:
				count += 1
	return count

def update(board, grid):
	new_board = copy.deepcopy(board)
	for i in range(1, grid-1):
		for j in range(1, grid-1):
			nghs = neighbors(board, i, j)
			if board[i][j] == 0:
				if nghs == 3:
					new_board[i][j] = 1
			else:
				if not (nghs == 2 or nghs == 3):
					new_board[i][j] = 0

	return new_board

def revive(board, pos, cell_side):
	i = int(pos[0]/cell_side)
	j = int(pos[1]/cell_side)
	board[i][j] = 1
	return board

def draw(screen, board, grid, cell_side):
	screen.fill((128, 128, 128))
	draw_board(screen, board, grid, cell_side)
	pygame.display.update()

def main(screen):
	grid = 50
	cell_side = int(SIDE/grid)
	board = [[0 for j in range(grid)] for i in range(grid)]
	delay = 0.25
	curr_time = time.time()
	clock = pygame.time.Clock()
	start = False
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if pygame.mouse.get_pressed()[0]:
				pos = pygame.mouse.get_pos()
				board = revive(board, pos, cell_side)
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_s:
					start = not start
		
		clock.tick(60)
		if time.time() - curr_time > delay and start:
			board = update(board, grid)
			curr_time = time.time()
		draw(screen, board, grid, cell_side)

if __name__ == '__main__':
	main(WINDOW)