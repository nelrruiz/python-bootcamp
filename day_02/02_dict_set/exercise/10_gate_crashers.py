invited = {"Ana", "Ben", "Carlo", "Dani"}
attended = {"Ben", "Carlo", "Ely"}

# TODO: Who are all the involved members?
print("Involved Members:", invited.union(attended))

# TODO: Who was absent?
print("Absent:", invited.difference(attended))

# TODO: Who gatecrashed?
print("Not enrolled but attended:", attended.difference(invited))

# TODO: Who was invited and attended
print("Attended properly:", invited.intersection(attended))
