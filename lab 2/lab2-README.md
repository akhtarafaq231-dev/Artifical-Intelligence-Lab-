# AI Lab 2: Intelligent Agents & PEAS Framework

## Files
- `lab2_percepts.py` — Task 3 (guided): simple reflex classroom agent — maps each percept to a mode, no memory
- `lab2_model.py` — Task 3 (extension): stateful agent — remembers the previous target mode and skips repeated commands
- `lab2_check.py` — Task 3 (test): runs the percept trace showing step, previous mode, percept, target mode, and SEND / NO COMMAND
- `Lab_2report.docx` — Full report: Task 1 PEAS specs, Task 2 environment classifications, Task 3 code, trace, explanation, and conclusion

## How to Run
```bash
python lab2_percepts.py
python lab2_check.py
```

## Requirements
- Python 3.x (no extra packages needed)

## Key Result
The stateful agent sends a command only when the target mode changes —
repeated percepts print `NO COMMAND`. See `Lab_2report.docx` for the full trace
and step-by-step explanation.
