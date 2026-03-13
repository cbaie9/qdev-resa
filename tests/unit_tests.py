import unittest
from resa.resa import *

class bookMeetingRoomUnitTests(unittest.TestCase):
  def test_small_room(self):
    self.assertEqual(bookMeetingRoom(5), Room.SMALL)
  def test_medium_room(self):
    self.assertEqual(bookMeetingRoom(15), Room.MEDIUM)
  def test_large_room(self):
    self.assertEqual(bookMeetingRoom(35), Room.LARGE)
  def test_refuse_room(self):
    self.assertEqual(bookMeetingRoom(55), Room.REFUSE)

if __name__ == '__main__':
  unittest.main()
