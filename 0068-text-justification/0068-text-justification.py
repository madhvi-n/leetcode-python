class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        """
        While iterating through words, 
        keep track of the words that we have added to the current line so far and their total length. 
        We will keep adding words to this line until we cannot add any more words without exceeding the maximum width.

        Once we have the words for a line, we will distribute the spaces between the words as evenly as possible. 
        If there are more spaces than can be distributed evenly, we will add the extra spaces to the leftmost slots.

        We will repeat this process until we have processed all the words in the input array. 
        The last line will be left-justified, so we don't need to distribute any spaces.
        """
        result = []
        current_line = []
        current_length = 0

        for word in words:
            # check if the current word can be added to the current line
            if current_length + len(word) + len(current_line) <= maxWidth:
                current_line.append(word)
                current_length += len(word)
            else:
                # distribute the spaces between the words on the current line
                num_spaces = maxWidth - current_length
                num_words = len(current_line)

                if num_words == 1:
                    # left-justify the line if it contains only one word
                    result.append(current_line[0] + ' ' * num_spaces)
                else:
                    spaces_between_words = num_spaces // (num_words - 1)
                    extra_spaces = num_spaces % (num_words - 1)

                    justified_line = ''
                    for i in range(num_words - 1):
                        justified_line += current_line[i]
                        justified_line += ' ' * spaces_between_words

                        if i < extra_spaces:
                            justified_line += ' '

                    justified_line += current_line[-1]
                    result.append(justified_line)

                # start a new line with the current word
                current_line = [word]
                current_length = len(word)

        # add the last line (left-justified)
        last_line = ' '.join(current_line)
        last_line += ' ' * (maxWidth - len(last_line))
        result.append(last_line)

        return result