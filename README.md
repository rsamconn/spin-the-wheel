# Spin the Wheel

A small command-line tool that randomly pairs each item from a smaller list with a unique item from a larger list, without replacement.

## Usage

```
python3 wheel.py <small_list_file> <large_list_file>
```

Each file should contain one item per line. The large list must have at least as many items as the small list. The script prints each pairing to the screen.

Example:

```
python3 wheel.py names.txt roles.txt
```

## Example use cases

1. **Team roles** — pair team members with meeting roles (Scrum Master, Note Taker, etc.)
2. **Restaurant picker** — pair days of the week with restaurants to try
3. **Chore assignment** — pair housemates with weekly chores
4. **Secret Santa / gift exchange** — pair participants with people to buy gifts for
5. **Project ideas** — pair students or teams with topics/projects to work on

## Tests

Run the test suite with:

```
python3 -m pytest -q
```
