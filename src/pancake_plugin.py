from abc import ABCMeta, abstractmethod
from senkalib import CaajJournal

class CaajPlugin(metaclass=ABCMeta):
  chain = None

  @abstractmethod
  def can_handle(cls, transaction_id) -> bool:
    pass

  @abstractmethod
  def get_caajs(cls) -> CaajJournal:
    return CaajJournal