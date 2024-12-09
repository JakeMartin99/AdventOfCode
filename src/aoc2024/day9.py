def _print_state(state: list[int]):
    print("\n")
    [print(i if i != -1 else '.', end='') for i in state]
    print()


def pt1(num_lst: list[int], verbose: bool = False) -> int:
    # Construct the initial disk state
    state, filenum, spaces = [], 0, 0
    for i in range(0, len(num_lst)):
        qty = num_lst[i]
        if i % 2 == 0:
            [state.append(filenum) for j in range(qty)]
            filenum += 1
        else:
            [state.append(-1) for j in range(qty)]
            spaces += qty
    if verbose: _print_state(state)

    # Identify empty numbers and "pop" values to move into them, in order
    idx, empties = len(state) - 1, []
    while spaces > 0:
        val = state[idx]
        if val != -1:
            empties.append(val)
            state[idx] = -1
        spaces -= 1
        idx -= 1
    if verbose: _print_state(empties)

    # Fill empty spaces with the "popped" numbers
    for e in empties:
        state[state.index(-1)] = e
    if verbose: _print_state(state)

    # Produce checksum
    return sum([pos * file for (pos, file) in enumerate(state) if file != -1])


def _blocks_to_state(blocks: dict[int, list[int]]) -> list[int]:
    state = [-2]*100000
    for f in blocks.keys():
        for (idx, size) in blocks[f]:
            state[idx:idx+size] = [f]*size
    return state[0:state.index(-2)]


def pt2(num_lst: list[int], verbose: bool = False) -> int:
    # Construct the initial disk state
    blocks, filenum, idx = {}, 0, 0
    blocks[-1] = []
    for i in range(0, len(num_lst)):
        qty = num_lst[i]
        if i % 2 == 0:
            blocks[filenum] = []
            blocks[filenum].append((idx, qty))
            filenum += 1
        else:
            blocks[-1].append((idx, qty))
        idx += qty
    if verbose: _print_state(_blocks_to_state(blocks))

    # Works backwards from the highest values to "pop" and move whole files forward
    for f in filter(lambda x: x != -1, sorted(blocks.keys(), reverse=True)):
        idx, size = blocks[f][0]
        for (e_loc, (e_idx, e_size)) in enumerate(blocks[-1]):
            if e_size == size and e_idx < idx:
                new_empty = blocks[f][0]
                blocks[f][0] = blocks[-1][e_loc]
                blocks[-1][e_loc] = new_empty
                blocks[-1].sort(key=lambda j: j[0])
                break
            elif e_size > size and e_idx < idx:
                new_empty = blocks[f][0]
                kept_empty_slice = (e_idx + size, e_size - size)
                blocks[f][0] = (e_idx, size)
                blocks[-1][e_loc] = new_empty
                blocks[-1].append(kept_empty_slice)
                blocks[-1].sort(key=lambda j: j[0])
                break
    state = _blocks_to_state(blocks)
    if verbose: _print_state(state)

    # Produce checksum
    return sum([pos * file for (pos, file) in enumerate(state) if file != -1])


def main():
    with open("../../inputs/aoc2024/day9.txt", "r") as f:
        num_lst = [list(map(int, line.strip())) for line in f.readlines()][0]
    print("Pt 1:", pt1(num_lst))
    print("Pt 2:", pt2(num_lst))


if __name__ == "__main__":
    main()
