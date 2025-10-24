def solution(cipher,code):
    return "".join(list(cipher)[code-1::code])