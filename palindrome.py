#!//usr/bin/env python
import sys
import argparse

def palindrome(word: str) -> bool:
    for i in range(len(word) // 2):
        if word[i] != word[-i - 1]:
            return False
    return True

def test_palindrome() -> None:
    assert palindrome("kajak") == True
    assert palindrome("avggva") == True
    assert palindrome("kajka") == False


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("word")
    args = parser.parse_args()
    if palindrome(args.word):
        print(f"{args.word} is a palindrome.")
        return 0
    print(f"{args.word} is not a palindrome.")
    return 0


if __name__ == "__main__":
    main()
