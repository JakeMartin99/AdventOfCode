from collections import defaultdict
from functools import partial
from multiprocessing import Manager, Pool, Queue, cpu_count


PHYSICAL_CORES = cpu_count() // 2


def evolve_secret(s: int) -> int:
    s1 = ((s * 64) ^ s) % 16777216 # 16777216 = 2**24
    s2 = ((s1 // 32) ^ s1) % 16777216
    s3 = ((s2 * 2048) ^ s2) % 16777216
    return s3


def final_secret(init_s: int) -> int:
    s = init_s
    for _ in range(2000):
        s = evolve_secret(s)
    return s


def seq_rewards(init_s: int, q: Queue) -> None:
    s, prices = init_s, [init_s % 10]
    for _ in range(2000):
        s = evolve_secret(s)
        prices.append(s % 10)
    deltas = [prices[i+1] - prices[i] for i in range(len(prices)-1)]
    rewards = {}
    for i in range(4, len(prices)):
        seq = "::".join(map(str, deltas[i-4:i]))
        if seq not in rewards:
            rewards[seq] = prices[i]
    q.put(rewards)


def pt1(lst: list[int]) -> int:
    with Pool(processes=PHYSICAL_CORES) as p:
        results: list[int] = p.imap_unordered(final_secret, lst)
        p.close()
        p.join()
        return sum(results)


def pt2(lst: list[int]) -> int:
    with Manager() as m:
        q = m.Queue()
        with Pool(processes=PHYSICAL_CORES) as p:
            list(p.imap_unordered(partial(seq_rewards, q=q), lst))
            p.close()
            p.join()
        results: list[defaultdict[str, int]] = [q.get() for _ in range(len(lst))]
    total_rewards = defaultdict(lambda: 0)
    for rewards in results:
        for seq, reward in rewards.items():
            total_rewards[seq] += reward
    return max(total_rewards.values())


def main():
    with open("../../inputs/aoc2024/day22.txt", "r") as f:
        lst = [int(line) for line in f.readlines()]
    print("Pt 1:", pt1(lst))
    print("Pt 2:", pt2(lst))


if __name__ == "__main__":
    main()
