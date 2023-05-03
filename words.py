import re

def word_count(filename):
    words_set = set()
    with open("Learned_Vocabulary.txt", 'r') as file:
        text = file.read()
        words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
        words_set.update(words)

    with open("Learned_Vocabulary.txt", 'w') as file:
        sorted_words = sorted(words_set)
        file.write("\n")

        for word in sorted_words:
            file.write(word + " ")
        file.write("\n")

    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
        words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
        words = [word for word in words if len(word) >= 5 and word not in words_set]
        freq = {}
        for word in words:
            freq[word] = freq.get(word, 0) + 1
        sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        N = 7

        md_table = "| Words" * N + "|\n"
        md_table += "| :---: " * N + "|\n"

        for i, (word, _) in enumerate(sorted_freq):
            md_table += f"| [{word}](https://translate.google.com/#view=home&op=translate&sl=en&tl=zh-CN&text={word}) "

            if(i % N == N - 1):
                md_table += '| \n'
        return md_table

if __name__ == '__main__':
    md_table = word_count('data/IELTS_Reading_2.txt')
    with open('out.md', 'w') as file:
        file.write(md_table)
