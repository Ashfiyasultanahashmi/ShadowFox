#1. Create a list of your friends' names. The list should have at least 5 names. Create a list of tuples. Each tuple should contain a friend's name and the length of their name.
besties=["Iram", "Ashfiya", "Athufa", "Heena", "Hajira"]
friendsname_length=[(name, len(name)) for name in besties]
print("The List of tuples(name,length) is", friendsname_length)
