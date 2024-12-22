from pathlib import Path
import sys
import textwrap

def main():
    year = sys.argv[1]
    base = Path('../../')
    for t in [(Path('src'), '.py'), (Path('tst'), '.py'), (Path('inputs'), '.txt')]:
        r, ext = t
        folder = base / r / Path(f'aoc{year}')
        folder.mkdir(exist_ok=True)
        if r != Path('inputs'):
            (folder / Path('__init__.py')).touch(exist_ok=True)
        for d in range(1, 26):
            file = folder / Path(f'{'test_' if r == Path('tst') else ''}day{d}{ext}')
            file.touch(exist_ok=True)
            if len(file.read_text()) == 0:
                if r == Path('src'):
                    file.write_text(textwrap.dedent(
                        f"""\
                        def pt1() -> int:
                            return -1
                        
                        
                        def pt2() -> int:
                            return -1
                        
                        
                        def main():
                            with open("../../inputs/aoc{2024}/day{d}.txt", "r") as f:
                                input = [line for line in f.readlines()]
                            print("Pt 1:", pt1())
                            print("Pt 2:", pt2())
                        
                        
                        if __name__ == "__main__":
                            main()
                        
                        """
                    ))
                elif r == Path('tst'):
                    file.write_text(textwrap.dedent(
                        f"""\
                        from src.aoc{year}.day{d} import *
                        
                        
                        ex1 = \"\"
                        
                        
                        def test_pt1():
                            val = pt1()
                            assert val == -1


                        def test_pt2():
                            val = pt2()
                            assert val == -1
                        
                        """
                    ))


if __name__ == "__main__":
    main()
