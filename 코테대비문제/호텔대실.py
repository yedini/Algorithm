from heapq import heappush, heappop
def solution(book_time):
    answer = 1
    
    for i in range(len(book_time)):
        book_time[i][0] = int(book_time[i][0][:2])*60+int(book_time[i][0][3:])
        book_time[i][1] = int(book_time[i][1][:2])*60+int(book_time[i][1][3:])
    book_time.sort()
    
    heap = []
    for start, end in book_time:
        if not heap:
            heappush(heap, end+10)
            continue
        if heap[0]<=start:
            heappop(heap)
        else:
            answer += 1
        heappush(heap, end+10)
    return answer