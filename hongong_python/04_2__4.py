# 딕셔너리 선언

character = {
    'name' : '기사',
    'level' : '12',
    'items' : {
        'sword' : '불꽃의 검',
        'amror' : '풀플레이트',
    },
    'skill' : ['베기', '세게 베기', '아주 세게 베기']
}

# for 반복문 사용
for key in character:
    if type(character[key]) is dict:
        for dict_key in character[key]:
            print(dict_key, ":", character[key][dict_key])
    elif type(character[key]) is list:
        for item in character[key]:
            print(key, ":", item)
    else:
        print(key, ":", character[key])
