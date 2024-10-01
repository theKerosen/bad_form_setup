import os


class bee_movie_spam:
    def read_lines(self):
        lines = []
        with open(f"{os.getcwd()}/copy.txt", "r+") as f:
            for line in f:
                line = line.strip()
                elements = line.split("\n")
                lines.append(elements)
        return lines
