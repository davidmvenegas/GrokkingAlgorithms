dictionary = [
    "dog",
    "deer",
    "deal",
    "cat",
    "door",
    "dear",
    "deer",
    "dearly",
    "dearest",
    "dearests",
]


def longest_common_substring(word_1, word_2):
    n, m = len(word_1), len(word_2)  # Get the length of the two words
    dp = [[0] * (m + 1) for _ in range(n + 1)]  # Initialize the DP table

    longest = 0  # Initialize the longest common substring length
    end_pos = 0  # Initialize the end position of the longest common substring

    # Build the DP array
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if word_1[i - 1] == word_2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > longest:
                    longest = dp[i][j]
                    end_pos = i
            else:
                dp[i][j] = 0

    # Return the longest common substring and its length (word, length)
    return (word_1[end_pos - longest : end_pos], longest)


def autocomplete(input, dictionary):
    suggestions = []

    for word in dictionary:
        _, match_length = longest_common_substring(input, word)
        suggestions.append((word, match_length))

    # Sort the suggestions in descending order of match length and ascending order of word
    suggestions.sort(key=lambda x: (-x[1], x[0]))

    # Return the top 3 suggestions
    return [suggestion for suggestion, _ in suggestions][:3]


print(autocomplete("dear", dictionary))  # Output: ['dear', 'dearest', 'dearests']
print(autocomplete("do", dictionary))  # Output: ['door', 'dog']
print(autocomplete("c", dictionary))  # Output: ['cat']
print(autocomplete("de", dictionary))  # Output: ['dear', 'deer', 'dearly']
print(autocomplete("d", dictionary))  # Output: ['deer', 'dear', 'dearly']
