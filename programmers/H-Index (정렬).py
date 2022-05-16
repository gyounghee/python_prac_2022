# H-Index

def solution(citations):
    citations.sort(reverse = True)
    for i in range(len(citations)):
        if i+1 > citations[i]:
            return i
    return len(citations)


# TEST CASE Ⅰ
citations = [3, 0, 6, 1, 5]
print(solution(citations))     # 3

# TEST CASE Ⅱ
citations = [10, 10, 10, 10, 10]
print(solution(citations))     # 5

# TEST CASE Ⅲ
citations = [0, 0, 0, 0, 0]
print(solution(citations))     # 0

# TEST CASE Ⅳ
citations = [6, 5, 5, 5, 5, 2, 1, 0]
print(solution(citations))     # 5
