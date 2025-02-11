import enum


class EventType(enum.Enum):
    goal = "goal"
    assist = "assist"
    yellow_card = "yellow_card"
    red_card = "red_card"
