from datetime import datetime, timedelta
from time import sleep
from sys import argv
from subprocess import call


def main():
    custom_time = set_custom_time()
    study_durat = custom_time[0] if custom_time else 52
    break_durat = custom_time[1] if custom_time else 17
    isRunning = True
    studying = True
    while isRunning:
        alarm_time = get_alarm_date(studying, study_durat, break_durat)
        sleep_until_time_for_alarm(alarm_time, studying)
        studying = not studying
        turn_alarm_on(["break time", "it's time to study"][studying])
        input()


def set_custom_time():
    try:
        study_durat = int(argv[1])
        break_durat = int(argv[2])
        print(f"Timer set to {argv[1]}/{argv[2]}")
        return [study_durat, break_durat]
    except ValueError:
        print("Invalid format of custom time")
    except IndexError:
        print("No custom time provided. Timer set to 52/17")


def get_alarm_date(studying, study_durat, break_durat):
    ONE_MIN = timedelta(minutes=1)

    if studying:
        return datetime.now() + study_durat * ONE_MIN
    else:
        return datetime.now() + break_durat * ONE_MIN


def sleep_until_time_for_alarm(alarm_date, studying):
    """Sleep until current time >= alarm_time.
    """
    clear_screen = "\033[H\033[2J"
    sleep(2)
    while datetime.now() <= alarm_date:
        time_left = alarm_date - datetime.now()
        end = "of study left" if studying else "of break left"
        print(f"{clear_screen} {str(time_left)[:7]} {end}")
        sleep(1)


def turn_alarm_on(message):
    """Get speech output from entered message.
    """
    call(["spd-say", message])


if __name__ == "__main__":
    main()
