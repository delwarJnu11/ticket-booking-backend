TIME_CHOICES = [
    ('08:00 AM', '08:00 AM'),
    ('09:00 AM', '09:00 AM'),
    ('011:00 AM', '11:00 AM'),
    ('01:00 PM', '01:00 PM'),
    ('03:00 PM', '03:00 PM'),
    ('05:00 PM', '05:00 PM'),
    ('08:00 PM', '08:00 PM'),
    ('11:00 PM', '11:00 PM'),
]

SEAT_CHOICES = [(f"{letter}{i}", f"{letter}{i}") for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' for i in range(1, 6)]