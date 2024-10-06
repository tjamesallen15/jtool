from abc import ABC, abstractmethod

class Dungeon(ABC):
  @abstractmethod
  def initialize(self, frame, btn, runs):
    pass

  @abstractmethod
  def run_dungeon(self, runs):
    pass
