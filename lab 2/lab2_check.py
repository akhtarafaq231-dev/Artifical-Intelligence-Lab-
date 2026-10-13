
from lab2_model import StatefulAgent

agent = StatefulAgent()

percepts = [
    (29, True),
    (29, True),
    (20, True),
    (26, True),
    (19, True),
    (29, False)
]

print("Step | Previous | Percept | Target | Command")
print("-" * 60)

for step, (temp, occupied) in enumerate(percepts, 1):
    agent.sensor(temp, occupied)

    previous, target, send = agent.act()

    if send:
        command = "SEND"
    else:
        command = "NO COMMAND"

    print(
        f"{step} | {previous} | "
        f"{(temp, occupied)} | {target} | {command}"
    )