genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]


def get_melon_best_album(genre_array, play_array):
    leng = len(genre_array)
    genre_dict = {}
    index_play = {}

    for i in range(leng):
        genre = genre_array[i]
        play = play_array[i]
        if genre not in genre_dict:
            genre_dict[genre] = play
            index_play[genre] = [[i, play]]
        else:
            genre_dict[genre] += play
            index_play[genre].append([i, play])

    print(index_play)
    sorted_genre = sorted(genre_dict.items(), key=lambda item: item[1], reverse=True)
    result = []
    for genre, _value in sorted_genre:
        index = index_play[genre]
        sorted_paly_index = sorted(index, key=lambda item: item[1], reverse=True)
        print(sorted_paly_index)
        for i in range(len(sorted_paly_index)):
            if i > 1:
                break
            result.append((sorted_paly_index[i][0]))
    return result


print(get_melon_best_album(genres, plays))  # 결과로 [4, 1, 3, 0] 가 와야 합니다!