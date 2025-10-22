def solution(rsp):
    result = ""
    win_pla = { "2" : "0", "0" : "5", "5" : "2"}
    return "".join(win_pla[attack] for attack in rsp )