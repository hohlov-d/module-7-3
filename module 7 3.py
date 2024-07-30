class WordsFinder:
    def __init__(self, *file_name):
        self.file_names = [*file_name]
        self.file_name = file_name

    def get_all_words(self):
        all_words = {}
        words = []
        punktuation = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                for line in file:
                    line = line.lower()
                    for i in punktuation:
                        if i in line:
                            line = line.replace(i, ' ')
                    words.extend(line.split())
            all_words[file_name] = words
            return all_words

    def find(self, word):
        dict_ = self.get_all_words()
        results = []
        for name, words in dict_.items():
            for k in words:
                if word.lower() in k:
                    index = words.index(k)
                    results.append(self.file_name)
                    results.append(index + 1)
                    break
        return results

    def count(self, word):
        dict_ = self.get_all_words()
        results = []
        count = 0
        for name, words in dict_.items():
            for k in words:
                if word.lower() in k:
                    count += 1
        results.append(self.file_name)
        results.append(count)
        return results

finder1 = WordsFinder('Mother Goose.txt',)
print(finder1.get_all_words())
print(finder1.find('Child'))
print(finder1.count('Child'))







