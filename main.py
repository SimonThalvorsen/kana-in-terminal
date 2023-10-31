def main():
    q = input("(k)atakana or (h)iragana?\n>").lower()
    file = "katakana.txt" if q == 'k' else "hiragana.txt"
    points = 0
    total = 0
    with open(file, encoding="utf8") as f:
        for line in f:
            total += 1
            ans = input(line.split()[0].lower() + "= ")
            if ans == line.split()[1]:
                points += 1
                print("Correct! +1 point.")
    print(f"You got {points}/{total} correct.")


def oneline():
    print(
        f"You got {len([x for x in open('katakana.txt', encoding='utf8') if x.split()[1] == input(x.split()[0] + '= ')])}/46 correct.") \
        if input("(k)atakana or (h)iragana?\n>").lower() == 'k' else \
        print(
            f"You got {len([x for x in open('hiragana.txt', encoding='utf8') if x.split()[1] == input(x.split()[0] + '= ')])}/46 correct.")


if __name__ == '__main__':
    oneline()