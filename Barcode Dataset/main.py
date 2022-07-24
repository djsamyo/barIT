import pygame
import pygame.camera
import sys
from pygame.locals import *
import cv2

cap = cv2.VideoCapture(0)

# Window setup
pygame.init()
fpsClock = pygame.time.Clock()
window_width = 1200
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Thingy')            # change name of tab here
icon = pygame.Surface((20, 20))
pygame.display.set_icon(icon)

# initializing font for later use
pygame.font.init()
font = pygame.font.SysFont('helvetica', 100)
medium_font = pygame.font.SysFont('helvetica', 30)

def main():
    bg = pygame.Rect(25, 25, 695, 535)
    green = False
    img = pygame.image.load("capture.jpg")
    img_rect = pygame.Rect(50, 50, 655, 495)
    print_front = pygame.Rect(1000, 500, 80, 50)
    bg_img = pygame.image.load('bg_image.jpeg')
    bg_img = pygame.transform.scale(bg_img, (1200, 600))
    bg_img.set_alpha(60)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # background
        window.fill((0, 0, 0))
        window.blit(bg_img, pygame.Rect(0, 0, 1200, 600))

        # capturing photo. not sure how it works, copy/pasted
        cap.set(3,224)
        cap.set(4,224)
        ret, frame = cap.read()
        cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
        cv2.imwrite('capture.jpg', frame)

        # preparing image
        if green or pygame.key.get_pressed()[K_RETURN]:
            img = pygame.image.load("capture.jpg")
            img_rect = pygame.Rect(50, 50, 655, 495)

        # buttons
        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_rect = pygame.Rect(mouse_x, mouse_y, 1, 1)
        if not mouse_rect.colliderect(print_front):
            pygame.draw.rect(window, (100, 100, 100), print_front)
        else:
            pygame.draw.rect(window, (100, 100, 0), print_front)
        window.blit(medium_font.render("Print", False, (255, 255, 255)), (1014, 507))

        # drawing stuff
        if green:
            pygame.draw.rect(window, (0, 100, 0), bg)
            window.blit(font.render("Success", False, (0, 200, 0)), (800, 200))
        else:
            pygame.draw.rect(window, (100, 0, 0), bg)
            window.blit(font.render("Failure", False, (200, 0, 0)), (800, 200))
            window.blit(medium_font.render("Press Enter to continue.", False, (200, 0, 0)), (800, 300))

        # image drawn last, on top
        window.blit(img, img_rect)

        # TEMPORARY - can make success with spacebar
        if pygame.key.get_pressed()[K_SPACE]:
            green = True
        else:
            green = False

        # ticks at FPS, updates screen to show new drawings
        fpsClock.tick(60)
        pygame.display.update()


if __name__ == "__main__":
    main()
