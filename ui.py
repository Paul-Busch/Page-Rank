#name = input("Geben Sie hier Ihr Suchwort oder mehrere Suchwörter ein")

def search_for_word(data, word):
    with open(data) as f:
        lines = f.readlines()
        for line in lines:
            if word in line:
                print(line)


search_for_word("/Users/Paul/Documents/Uni/Master 5. Semester/Einführung in Python/Page-Rank/test.txt", "Test")