# Let's return to the previous task. In the variable rate, we have the electricity tariff — 1.68. But now we need to
# calculate the day and night tariff. The night tariff is calculated as half of the day tariff, that is, the rate must
# be divided by 2. The value_day variable contains the daytime meter readings, and the value_night variable has the
# nighttime meter readings. Again, set them to a reasonable integer number of kilowatts. Calculate and put the
# electricity bill into the variable payment but with the day and night tariffs.

rate = 1.68
value_day = 5
value_night = 5
payment = value_day * rate + value_night * rate / 2
