from abc import ABC, abstractmethod

import common.util as util

class Dungeon(ABC):
  @abstractmethod
  def initialize(frame, btn, runs):
    pass

  def path_find(unit=util.UNIT_BLANK):
    pass

  @abstractmethod
  def run_dungeon(runs):
     pass