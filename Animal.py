import pygame


class Animal:
  #constructor
  def __init__(self, type, speed, position, direction, rect, flying, move):
    self.type = type
    self.speed = speed
    self.position = position
    self.direction = direction
    self.rect = rect
    self.flying = flying
    self.move = move
# 
# #   #getters and setters
# #   def set_speed(self, value):
# #    self.speed = value
# #   
# #   def set_position(self, value):
#     self.position = value
# #   
# #   def set_direction(self, value):
#     self.direction = value
# # 
# #   def set_speed(self):
#     return self.speed
# #   
# #   def get_position(self):
#     return self.position
# #   
# #   def get_direction(self):
#     return self.direction
# # 
# #   def set_rect(self, value):
#     self.rect = value
# # 
# #   def get_rect(self):
#     return self.rect 
# # 
# # class Cow(Animal):
# #   def __init__(self, speed, position, direction, rect, move, is_gold):
# #     self.is_gold = is_gold
#     Animal.__init__(self, speed, position, direction, rect, move)
# #   
# #   def set_gold(self, value):
#     self.is_gold = value
# #   
# #   def get_gold(self):
#     return self.is_gold
# # 
# # class Pig(Animal):
# #   def __init__(self, speed, position, direction, rect, move, is_gold):
# #     Animal.__init__(self, speed, position, direction, rect, move)
#     self.is_gold = is_gold
# # 
# # class Dog(Animal):
# #   def __init__(self, speed, position, direction, rect, move):
#     Animal.__init__(self, speed, position, direction, rect, move)
    