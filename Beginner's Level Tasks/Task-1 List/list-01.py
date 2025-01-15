#1. You have a list of superheroes representing the Justice League. Perform various tasks on them.
justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]
print(justice_league)

#Calculate the number of members in the Justice League. 
members_count = len(justice_league)
print(f"Number of members in the Justice League are: {members_count}")

#Batman recruited Batgirl and Nightwing as new members. Add them to your list. 
justice_league.extend(["Batgirl", "Nightwing"])
print(f"The Updated Justice League members are: {justice_league}")

#Wonder Woman is now the leader of the Justice League. Move her to the beginning of the list. 
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print(f"List of Justice League members when Wonder Woman is the leader: {justice_league}")

# Aquaman and Flash are having conflicts, and you need to separate them. Choose either "Green Lantern" or "Superman" and move them in between Aquaman and Flash. 
justice_league.remove("Superman")
flash_index = justice_league.index("Flash")
justice_league.insert(flash_index + 1, "Superman")
print(f"Justice league after Separating the Aquaman and Flash: {justice_league}")

# The Justice League faced a crisis, and Superman decided to assemble a new team. Replace the existing list with the following new members: "Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow". 
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print(f"New Justice League team members are: {justice_league}")

#Sort the Justice League alphabetically. The hero at the 0th index will become the new leader. 
justice_league.sort()
print(f"Sorted Justice League: {justice_league}")

#New leader of the justice league, after sorting will be
leader_of_justice_league = justice_league[0]
print(f"The new leader is: {leader_of_justice_league}")
