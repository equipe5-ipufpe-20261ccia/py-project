import pygame


# Essential for making text
class Draw_text():
  def __init__(self , text , screen):
    self.text = text.split(" ")
    self.current_word = 0
    self.last_update = 0
    self.screen = screen
  def draw_and_update(self, font , text_col , x , y , current_state , cooldown):
    if current_state - self.last_update > cooldown:
        if self.current_word < len(self.text):
            self.current_word += 1
            self.last_update = current_state

    visible_words = self.text[:self.current_word]
    text_to_render = " ".join(visible_words)

    if text_to_render:
        text_surface = font.render(text_to_render, True, text_col)
        self.screen.blit(text_surface, (x, y))