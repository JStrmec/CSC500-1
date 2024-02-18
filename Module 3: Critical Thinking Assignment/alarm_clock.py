
def alarm_will_go_off(alarm_time, current_time):
    current_time = int(current_time)
    alarm_time = int(alarm_time)
    total_hours = current_time + alarm_time
    while total_hours > 24:
            total_hours -= 24
    return total_hours


def main():
    print("Welcome to the Alarm Clock Program")
    current_time = input("Enter the time in HH format: ")
    alarm_time = input("Enter number of hours to wait: ")
    alarm = alarm_will_go_off(alarm_time, current_time)
    print(f"The alarm will go off at {alarm}:00")
main()