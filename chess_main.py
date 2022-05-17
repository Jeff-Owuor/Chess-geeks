import pygame as p
import chess_engine

WIDTH = HEIGHT = 500
DIMENSION = 8
SQ_SIZE = WIDTH/DIMENSION
p.init()
#for animations later on
MAX_FPS = 14 
IMAGES = {}

def loadImages():
    pieces = ['bp','bN','bR','bK','bB','bQ','wp','wN','wR','wK','wB','wQ']
    
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"),(SQ_SIZE,SQ_SIZE))
        
def main():
    screen = p.display.set_mode((WIDTH,HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))#not needed later
    gs = chess_engine.Gamestate()
    loadImages()
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running= False
        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()
 
def drawGameState(screen, gs):
    drawBoard(screen)
    
    drawPieces(screen, gs.board)
 
def drawBoard(screen):
    colors = [p.Color("white"),p.Color("gray")]
    
    for row in range(DIMENSION):
        for column in range(DIMENSION):
            color = colors[((row+column) % 2 )]
            p.draw.rect(screen,color, p.Rect(column * SQ_SIZE, row * SQ_SIZE, SQ_SIZE,SQ_SIZE))
            
def drawPieces(screen, board):
    for row in range(DIMENSION):
        for column in range(DIMENSION):
            piece = board[row][column]
            
            if piece != "--":
                screen.blit(IMAGES[piece],p.Rect(column * SQ_SIZE, row * SQ_SIZE, SQ_SIZE,SQ_SIZE))

 
if __name__ == '__main__':
     main()