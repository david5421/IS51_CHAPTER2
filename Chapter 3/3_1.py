state = "CA"
states = ("MD", "VA", "WV", "DE")

is_in_list = state in states

print(not(is_in_list) and "VA" in states )