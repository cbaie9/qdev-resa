from enum import Enum

class Room(Enum):
  REFUSE = 0
  SMALL = 1
  MEDIUM = 2
  LARGE = 3

  def __str__(self):
    if self == Room.LARGE:
      return "Large"
    if self == Room.MEDIUM:
      return "Medium"
    if self == Room.SMALL:
      return "Small"
    return "Refused"

def bookMeetingRoom(participants):
  if 1 <= participants <=10:
    return Room.SMALL
  elif 10< participants <= 30:
    return Room.MEDIUM
  elif 30< participants <=50:
    return Room.LARGE
  return Room.REFUSE
