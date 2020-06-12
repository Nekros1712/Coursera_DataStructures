# python3

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def polyHash(lt, prime, multiplier):
    hash = 0
    for c in reversed(lt):
        hash = (hash * multiplier + ord(c)) % prime
    return hash


def computeHash(text, pat, prime, multiplier):
    h = [None] * (len(text) - pat + 1)
    S = text[len(text) - pat:]
    h[len(text) - pat] = polyHash(S, prime, multiplier)
    y = 1
    for i in range(pat):
        y = (y * multiplier) % prime
    for i in range(len(text) - pat - 1, -1, -1):
        h[i] = (multiplier * h[i + 1] + ord(text[i]) -
                y * ord(text[i + pat])) % prime
    return h


def get_occurrences(pattern, text):
    result = []
    prime = 1610612741
    multiplier = 263
    p_hash = polyHash(pattern, prime, multiplier)
    H = computeHash(text, len(pattern), prime, multiplier)

    for i in range(len(text) - len(pattern) + 1):
        if (p_hash == H[i]) and (text[i:i + len(pattern)] == pattern):
            result.append(i)
    return result

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))










    
