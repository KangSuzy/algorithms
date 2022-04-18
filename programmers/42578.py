def solution(clothes):
    # 2차원 배열로 주어진 의상의 종류를 key 값으로 가지는 해시 생성
    hash_map = {}
    for cloth in clothes:
        name =  cloth[0] # 의상의 이름
        category = cloth[1] # 의상의 종류
        if category in hash_map:
            hash_map[category].append(name) # 의상의 종류가 존재하면 의상의 이름을 추가
        else:
            hash_map[category] = [name] # 의상의 종류가 존재하지 않는다면 원소 길이가 1

    # (한 category의 옷 수 + 1)*(한 category의 옷 수 + 1)*(한 category의 옷 수 + 1) ... -1
    answer = 1
    for key in hash_map:
        answer *=(len(hash_map[key])+1)
    return answer -1