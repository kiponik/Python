from sys import argv

script_name, total_time, hour_cash, award = argv

print((int(total_time) * int(hour_cash)) + int(award))