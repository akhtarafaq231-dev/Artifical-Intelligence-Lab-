"""Lab 2 - Task 3: Test script (trace).
Sir ke pattern wale agent ko test karta hai.
Run: python lab2_check.py
"""

from lab2_model import SimpleReflexAgent

agent = SimpleReflexAgent()

# repeated percepts, exact boundaries (20/26), mode transition, empty room
percepts = [(29, True), (29, True), (20, True),
            (26, True), (19, True), (29, False),
            (29, False), (24, True)]

print("step | percept      | prev_mode | target | command")
print("-" * 55)
for step, (temp, occupied) in enumerate(percepts, 1):
    agent.sensor(temp, occupied)
    old, target, send = agent.act()
    print(f"{step:>4} | {str((temp, occupied)):<12} | {str(old):<9} | "
          f"{target:<6} | {'SEND' if send else 'SKIP (repeat)'}")
