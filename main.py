def load_words(filename):
    words = []
    with open(filename, "r") as f:
        for line in f:
            if line.strip() == "":
                continue
            words.append(line.strip())
    return words

def normalize(text):
    text_list = list(text)
    letters = [letter.lower() for letter in text_list if letter.isalpha()]
    return "".join(letters)

def set_signature(text):
    normalized = normalize(text)
    unique_set = set(normalized)
    return frozenset(unique_set)

def freq_signature(text):
    normalized = normalize(text)
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    count_list = []

    for letter in alphabet:
        count_list.append(normalized.count(letter))

    return tuple(count_list)

def is_anagram_using_sets(a, b):
    return set_signature(a) == set_signature(b)

def print_counterexamples():
    print("Set counterexamples:")
    print(f"1) aab and ab: {is_anagram_using_sets('aab', 'ab')}")
    print()
    print(f"2) mississippi and misp: {is_anagram_using_sets('mississippi', 'misp')}")
    print()
    print(f"3) adder and read: {is_anagram_using_sets('adder', 'read')}")

def is_anagram(a, b):
    return freq_signature(a) == freq_signature(b)

def group_anagrams(words):
    value_dict = {}
    for word in words:
        frequency_sig = freq_signature(word)
        if frequency_sig not in value_dict:
            value_dict[frequency_sig] = []
        value_dict[frequency_sig].append(word)
    return value_dict


def main():
    words_list = load_words("words.txt")
    print_counterexamples()
    value_dict = group_anagrams(words_list)


    words_loaded = len(words_list)
    anagram_groups = len(value_dict.keys())

    single_count = 0
    max_value = 0
    max_list = None
    for key, value in value_dict.items():
        if len(value) == 1:
            single_count += 1
        if len(value) > max_value:
            max_value = len(value)
            max_list = value
    sorted_groups = sorted(value_dict.values(), key=len, reverse=True)

    print()
    print("ANAGRAM GROUP REPORT")
    print(f"Total words loaded: {words_loaded}")
    print(f"Total anagram groups: {anagram_groups}")
    print(f"Singleton groups (size 1): {single_count}")
    print(f"Largest group size (size {max_value}): {max_list[0:2]}")
    print()
    print("Top 5:")
    print(f"size {len(sorted_groups[0])}: ex: {sorted_groups[0][0:2]}")
    print(f"size {len(sorted_groups[1])}: ex: {sorted_groups[1][0:2]}")
    print(f"size {len(sorted_groups[2])}: ex: {sorted_groups[2][0:2]}")
    print(f"size {len(sorted_groups[3])}: ex: {sorted_groups[3][0:2]}")
    print(f"size {len(sorted_groups[4])}: ex: {sorted_groups[4][0:2]}")
    print()

    print("x in my_set is O(1) because when iterating through a set, it takes the same amount of time/memory to go through it no matter how many items are in the set.")
    print("x in my_list is O(n) because when iterating through a list, the amount of values in it will determine how much time/memory it takes up.")
    print("Building a frequency signature in my project is O(n) because it iterates through a list once.")
    print("Because sets get rid of duplicates so any word which has the same letter more than once will be considered to have the same frequency signature no matter how many times the letter appears.")




if __name__ == "__main__":
    main()




