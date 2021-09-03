def solution(phone_book):
    hash_map = {}
    # phone_book 리스트를 해시로 변환
    for phone_num in phone_book:
        hash_map[phone_num] = 1

    for phone_num in phone_book:
        # 하나씩 늘려가면 비교
        temp = ''
        for num in phone_num:
            temp += num
            # 접두어가 존재하는 경우와 자기 자신과 같을 경우
            if temp in hash_map and temp != phone_num:
                return False
    return True