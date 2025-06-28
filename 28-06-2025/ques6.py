//Hotel Room Availability Checker
room_availability = {
    'Standard': {'2024-04-12': 10, '2024-04-13': 5},
    'Deluxe': {'2024-04-12': 5, '2024-04-13': 2}
}
date = '2024-04-13'
availability = {room: dates.get(date, 0) for room, dates in room_availability.items()}
print("Availability on", date, ":", availability)
