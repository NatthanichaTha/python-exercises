from input_utils import input_int
def totaldmg(DMG, ATK_time, duration):
    return int(duration/ATK_time)*DMG + DMG


DMG = input_int("insert DMG per attack: ")
ATK_time = float(input("insert attack intervel (in sec): "))
duration = input_int("insert duration (in sec): ")

print(totaldmg(DMG, ATK_time, duration))