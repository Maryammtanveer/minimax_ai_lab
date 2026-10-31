
# Stateful Classroom Agent

class ClassroomController:

    def __init__(self):
        self.previous_mode = None

    def take_action(self, temperature, room_occupied):

        if not room_occupied:
            target_mode = "ECO"

        elif temperature > 26:
            target_mode = "COOL"

        elif temperature < 20:
            target_mode = "WARM"

        else:
            target_mode = "IDLE"

        if target_mode != self.previous_mode:
            notification = True
        else:
            notification = False

        old_mode = self.previous_mode
        self.previous_mode = target_mode

        return old_mode, target_mode, notification
