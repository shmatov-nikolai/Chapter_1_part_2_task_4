# A timestamp is three numbers: a number of hours, minutes and seconds.
# Given two timestamps, calculate how many seconds is between them. The
# moment of the first timestamp occurred before the moment of the second
# timestamp. ( 6, 1, 30, 6, 2, 10 result 40 sec.)

def differens_sec(hour, min, sec, hour_2, min_2, sec_2):
    transfer_sec = (hour*3600)+(min*60)+sec
    transfer_sec_2 = (hour_2*3600)+(min_2*60)+sec_2
    difference = transfer_sec - transfer_sec_2
    print(f"{hour, min, sec, hour_2, min_2, sec_2} difference result {abs(difference)} sec.")

differens_sec(6, 4, 30, 6, 2, 10)

