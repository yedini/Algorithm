# LRU: 가장 사용한지 오래된 것을 내보내는 알고리즘
# cache miss: 캐시 크기가 0인 경우, 아직 cache에 없는 값인 경우.
# city가 캐시 메모리에 있을 경우
# -> 지금의 city가 가장 최근에 사용된 것 -> 맨 마지막에 빠지도록 위치 변경, answer += 1
# city가 캐시 메모리에 없을 경우
# -> 캐시에 빈 공간이 있으면 캐시에 city 보관
# -> 없으면 사용된지 오래된 city는 빼고 현재 city를 캐시에 보관

def solution(cacheSize, cities):
    answer = 0
    i=0   # 캐시 인덱스
    cache = []
    # 캐시 사이즈가 0: city 하나 당 cache miss 발생
    if cacheSize == 0:
        return len(cities) * 5
    for c in cities:
        city = c.upper()
        if city in cache: # 이미 있는 city
            cache.remove(city) # 가장 첫번째 같은 city 값을 삭제
            cache.append(city)
            answer += 1
        else: # 캐시에 없는 city: cache miss
            answer += 5
            # 캐시에 빈공간이 있으면 추가
            if i < cacheSize: 
                cache.append(city)
                i+=1
            # 빈공간이 없으면: 내부 city 빼기
            else:
                cache.pop(0)
                cache.append(city)
    return answer