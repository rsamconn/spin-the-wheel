# Spin the Wheel

A small tool that randomly pairs each item from a smaller list with a unique item from a larger list, without replacement. Available as a command-line script or a simple interactive web app.

## Command-line usage

```
python3 wheel.py <small_list_file> <large_list_file>
```

Each file should contain one item per line. The large list must have at least as many items as the small list. The script prints each pairing to the screen.

Example:

```
python3 wheel.py example_small-lists/names.txt example_big-lists/roles.txt
```

## Web app

Open `index.html` in a browser. Paste your small list and big list into the two boxes (one item per line) and click **Spin!** to see the pairings.

## Example lists

- `example_small-lists/` — example "small list" files, e.g. names of people or teams
- `example_big-lists/` — example "big list" files, e.g. roles, positions, or states to be paired with the small list

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
