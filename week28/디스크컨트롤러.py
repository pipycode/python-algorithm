from heapq import heappush, heappop
def solution(jobs):
    answer = 0
    jobs.sort(key = lambda x:[x[0], x[1]])
    
    job_idx = 0
    while job_idx < len(jobs):
        work_place = [[jobs[job_idx][1], jobs[job_idx][0]]]
        time = jobs[job_idx][0]
        job_idx += 1
        while work_place:
            # 0. workplace의 작업을 완료한다.
            end_job = heappop(work_place)
            time += end_job[0]

            # 1. 작업시간 계산
            answer += (time - end_job[1])

            # 2. 작업이 끝나기 전 들어온 요청들을 work_place로 옮긴다.
            while job_idx < len(jobs) and jobs[job_idx][0] <= time:
                heappush(work_place, [jobs[job_idx][1], jobs[job_idx][0]])
                job_idx += 1

    return answer // len(jobs)

#9 13 18 25 28 // 5 = 17 