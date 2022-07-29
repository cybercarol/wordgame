import pygame
from utils.colors import PORTAGE_BLUE, RED, WHITE


class Button:
    OFFSET_Y = 20

    def __init__(self, text, width, height) -> None:
        font = pygame.font.SysFont('Verdana', 20)
        self.text = font.render(text, True, WHITE)
        self.rect = pygame.Rect(0, 0, width, height)
        self.color = PORTAGE_BLUE

    def draw(self, screen: pygame.Surface, offset_index=0):
        # Changes color on mouse hover
        self.color = RED if self.is_mouse_hover() else PORTAGE_BLUE

        # Aligns the button with at the center of the screen
        self.rect.center = screen.get_rect().center

        if offset_index > 0:
            self.rect.y += (self.rect.height + self.OFFSET_Y) * offset_index

        pygame.draw.rect(screen, self.color, self.rect)
        button_center_coordinates = self.text.get_rect(center=self.rect.center)
        screen.blit(self.text, button_center_coordinates)

    def is_mouse_hover(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())
