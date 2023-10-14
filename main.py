from run_program import Prog

if __name__ == "__main__":
    width = 1024
    height = 512
    title = "PolyDoom"

    Program = Prog(width, height, title)

    Program.run()