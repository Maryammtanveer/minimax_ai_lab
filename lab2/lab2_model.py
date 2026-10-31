# Testing the Classroom Agent

from model import ClassroomAgent

classroom = ClassroomAgent()

temperature_data = [
    (29, True),
    (24, True),
    (29, False),
    (19, True),
    (30, True)
]

for count, (current_temp, room_occupied) in enumerate(temperature_data, 1):

    previous_mode, target_mode, notification = classroom.act(
        current_temp, room_occupied
    )

    print("Step:", count)
    print("Previous Temperature:", previous_mode)
    print("Temperature:", current_temp)
    print("Occupied:", room_occupied)
    print("Target Temperature:", target_mode)
    print("Send Message:", notification)
    print("--------------------")
