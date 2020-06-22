## Matthew Conover
## Assignment 7-8
## IS 3750

sandwich_orders=['tuna', 'blt', 'reuben', 'ham', 'turkey'] ## Initial list
finished_sandwiches = list()
for s in sandwich_orders: ##Print sandwiches and add them to finished
	print(f"The {s} sandwich has been finished")
	finished_sandwiches.append(s)

print("The following sandwiches were made")# Print finished list
for f in finished_sandwiches:
	print(f)
