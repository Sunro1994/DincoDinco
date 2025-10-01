# 속한 노래가 많이 재생된 장르를 먼저 수록
# 장르 내에서 많이 재생된 노래를 먼저 수록
# 장르 내에서 재생된 횟수가 같은 노래 중에는 고유 번호가 낮은 노래를 먼저 수록



def solution(genres, plays):
    answer = []
    dict = []
    for i in range(len(genres)):
        dict.append([genres[i], plays[i], i])

    print(dict)

    #총 재생횟수 계산
    genre_play_count = {}
    for genre, play, i in dict:
        if genre not in genre_play_count:
            genre_play_count[genre] = 0
        genre_play_count[genre] += play

    print(genre_play_count)

    sorted_genres = sorted(genre_play_count.keys(), key=lambda g: genre_play_count[g], reverse=True)
    print(sorted_genres)

    # 각 장르 내에서 노래를 재생 횟수 및 고유 번호 순으로 정렬하여 앨범에 추가
    for genre in sorted_genres:
        songs_in_genre = sorted([song for song in dict if song[0] == genre], key=lambda s: (-s[1], s[2]))
        answer.extend([song[2] for song in songs_in_genre[:2]])

    return answer

solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500])