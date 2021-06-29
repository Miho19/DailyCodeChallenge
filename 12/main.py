


def longest_sub(string, k):

    start = 0
    end = 0

    high = 0
    low = 0
    
    window = set()

    char_set = dict()
    # init dict with values from string
    for s in string:
        char_set.setdefault(s, 0)
    
    while(end < len(string)):

        window.add(string[end])
        char_set[string[end]] += 1
        # reduce window size until only k unique chars
        while(len(window) > k):
            char_set[string[start]] -= 1

            if(char_set[string[start]] == 0):
                window.remove(string[start])
            start += 1
        
        # update max
        if high - low < end - start:
            high = end
            low = start
        
        end += 1

    print(str(string[low:high + 1]))
   




longest_sub("abcba", 2)
longest_sub("aabbcc", 1)
longest_sub("aabbcc", 2)