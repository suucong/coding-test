def solution(name):
    answer = 0
    for ch in name:
        answer += min(ord(ch) - ord('A'), ord('Z') - ord(ch) + 1)
        
    min_move = len(name) - 1
    for i in range(len(name)):
        next_i = i + 1
        while next_i < len(name) and name[next_i] == 'A':
            next_i += 1
        move = i + i + len(name) - next_i
        alt_move = i + 2 * (len(name) - next_i)
        min_move = min(min_move, move, alt_move)
        
    answer += min_move
    return answer