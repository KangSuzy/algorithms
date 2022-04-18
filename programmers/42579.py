def solution(genres, plays):
    # 장르별 총 재생수
    hash_map = {}
    answer = []

    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        if genre in hash_map:
            hash_map[genre]['plays'][i] = play
            hash_map[genre]['total_play'] += play
        else:
            hash_map[genre] = {
                # return 값이 결국 index 값이기 때문에
                'plays': {
                    i: play
                },
                'total_play': play
            }

    # total_plays 기준 장르별 sorting (내림차순)
    temp = sorted(hash_map.items(), key=lambda x: -x[1]['total_play'])

    # 각 곡별 sorting
    for item in temp:
        # index 별 plays 수를 기준으로 내림차순, 고유번호가 낮은 노래를 수록
        target = item[1]['plays']
        item[1]['plays'] = sorted(target.items(), key=lambda x: (-x[1], x[0]))

        temp = dict(temp)
    # print(temp)

    for key in temp:
        if len(temp[key]['plays']) >= 2:
            answer += [temp[key]['plays'][0][0], temp[key]['plays'][1][0]]
        # 장르에 속한 곡이 하나일 경우
        else:
            answer += [temp[key]['plays'][0][0]]
    return answer