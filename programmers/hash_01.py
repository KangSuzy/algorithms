def solution(participant, completion):
    answer = ''
    dic = {}
    # 완주한 선수 정보를 해시로 전환
    for person in completion:
        if person in dic:
            dic[person] = dic[person] + 1  # 동명이인의 경우
        else:
            dic[person] = 1

    # participant 리스트를 순회하면서 확인하기
    for person in participant:
        if person not in dic:  # dic 존재하지 않는다면 완주하지 못한사람
            return person
        if dic[person] == 0:  # 0이 되면 !
            return person
        dic[person] = dic[person] - 1  # 동명이인 value 값 -1

    return answer