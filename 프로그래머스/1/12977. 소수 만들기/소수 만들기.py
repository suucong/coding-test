def solution(nums):
    answer = 0
    max_num = 3000
    
    # 소수 판별 리스트 만들기
    prime_nums = [0] * max_num
    for i in range(2, max_num):
        if prime_nums[i] == 0:
            for j in range(i * i, max_num, i):
                prime_nums[j] = 1

    # 3개를 더하는 조합 반복문
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                sum_of_three = nums[i] + nums[j] + nums[k]
                if prime_nums[sum_of_three] == 0:
                    answer += 1
    return answer
