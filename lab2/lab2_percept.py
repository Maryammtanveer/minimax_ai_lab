 
class ClassroomController:

    def __init__(self):
        self.last_mode = None

    def take_action(self, temperature, classroom_occupied):

        if not classroom_occupied:
            new_mode = "ECO"

        elif temperature > 26:
            new_mode = "COOL"

        elif temperature < 20:
            new_mode = "WARM"

        else:
            new_mode = "IDLE"

        if new_mode != self.last_mode:
            notification = True
        else:
            notification = False

        previous_mode = self.last_mode
        self.last_mode = new_mode

        return previous_mode, new_mode, notification


controller = ClassroomController()

temperature_data = [
    (29, True),
    (24, True),
    (29, False),
    (19, True),
    (30, True)
]

for count, (current_temperature, occupied_status) in enumerate(temperature_data, 1):

    old_mode, current_mode, alert = controller.take_action(
        current_temperature, occupied_status
    )

    print("Step:", count)
    print("Previous Mode:", old_mode)
    print("Temperature:", current_temperature)
    print("Occupied:", occupied_status)
    print("Target Mode:", current_mode)
    print("Send Notification:", alert)
    print("--------------------")
