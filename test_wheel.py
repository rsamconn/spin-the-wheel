import random
from wheel import pair, load_list


def test_pair_counts_and_no_replacement():
    names = ["Alice", "Bob", "Carol"]
    roles = ["A", "B", "C", "D", "E", "F"]
    result = pair(names, roles, rng=random.Random(42))

    assert len(result) == len(names)
    assigned_roles = [r for _, r in result]
    assert len(set(assigned_roles)) == len(assigned_roles)
    for r in assigned_roles:
        assert r in roles
    assert [n for n, _ in result] == names


def test_pair_exact_size_lists():
    names = ["X", "Y"]
    roles = ["1", "2"]
    result = pair(names, roles, rng=random.Random(0))
    assert sorted(r for _, r in result) == roles


def test_load_list_strips_and_skips_blank_lines(tmp_path):
    f = tmp_path / "list.txt"
    f.write_text("Alice\n\nBob \n  \nCarol\n")
    assert load_list(f) == ["Alice", "Bob", "Carol"]


def test_example_files_load_correctly():
    names = load_list("names.txt")
    roles = load_list("roles.txt")
    assert names == ["Alice", "Bob", "Carol"]
    assert len(roles) == 6
    assert len(roles) >= len(names)
