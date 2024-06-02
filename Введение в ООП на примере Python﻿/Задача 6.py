class MinMaxWordFinder:
    def __init__(self):
        self.shortest_words_dict = {}
        self.longest_words_dict = {}

    def add_sentence(self, sentence):
        words = sentence.split()
        min_len = min(len(word) for word in words)
        max_len = max(len(word) for word in words)

        # Добавляем самые короткие слова
        for word in words:
            if len(word) == min_len:
                if word in self.shortest_words_dict:
                    self.shortest_words_dict[word] += 1
                else:
                    self.shortest_words_dict[word] = 1

        # Добавляем самые длинные слова
        for word in words:
            if len(word) == max_len:
                if word not in self.longest_words_dict:
                    self.longest_words_dict[word] = 1

    def shortest_words(self):
        return sorted(self.shortest_words_dict.keys())

    def longest_words(self):
        return sorted(self.longest_words_dict.keys())
    
finder = MinMaxWordFinder()
finder.add_sentence('hello abc world')
finder.add_sentence('def asdf qwert')
print(' '.join(finder.shortest_words()))
print(' '.join(finder.longest_words()))