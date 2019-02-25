import heapq
import math

from Timer import timethis
from project_euler import sieve_of_eratosthenes


def main(n):

    primes, sieve = sieve_of_eratosthenes(n*10)
    print("sieve complete")
    prime_idx = 2
    changing_idx = 0
    base_in_power= [[2,1]]
    candidates = [4]
    number_of_candidates = 0
    next_entry = 3
    counter = 2

    while counter <= n:
        # print(counter)

        if changing_idx == 0 and number_of_candidates == 0:
            if candidates[0] < next_entry:
                base_in_power[changing_idx][1] += (base_in_power[changing_idx][1]+1)
                candidates[0] = base_in_power[0][0] ** (base_in_power [0][1] + 1)
            else:
                number_of_candidates += 1
                candidates.append(next_entry ** 2)
                base_in_power.append([primes[prime_idx], 1])
                prime_idx += 1
                next_entry = primes[prime_idx]


                changing_idx += 1
            counter += 1
        elif changing_idx == 0:
            if candidates[0] < candidates[1]:
                base_in_power[0][1] += (base_in_power[0][1] + 1)
                candidates[0] = base_in_power[0][0] ** (base_in_power[0][1] + 1)
            else:
                changing_idx += 1
                base_in_power[changing_idx][1] += base_in_power[changing_idx][1] + 1
                candidates[changing_idx] = base_in_power[changing_idx][0] ** (base_in_power[changing_idx][1] + 1)
            counter += 1
        elif changing_idx == number_of_candidates:
            if candidates[changing_idx] > candidates[changing_idx - 1]:
                changing_idx -= 1
                base_in_power[changing_idx][1] += base_in_power[changing_idx][1] + 1
                candidates[changing_idx] = base_in_power[changing_idx][0] ** (base_in_power[changing_idx][1] + 1)
            else:
                number_of_candidates += 1
                candidates.append(next_entry ** 2)
                base_in_power.append([primes[prime_idx], 1])
                prime_idx += 1
                next_entry = primes[prime_idx]


                changing_idx += 1
            counter += 1
        else:
            if candidates[changing_idx] > candidates[changing_idx - 1]:
                changing_idx -= 1
                base_in_power[changing_idx][1] += base_in_power[changing_idx][1] + 1
                candidates[changing_idx] = base_in_power[changing_idx][0] ** (base_in_power[changing_idx][1] + 1)
            elif candidates[changing_idx] > candidates[changing_idx + 1]:
                changing_idx += 1
                base_in_power[changing_idx][1] += base_in_power[changing_idx][1] + 1
                candidates[changing_idx] = base_in_power[changing_idx][0] ** (base_in_power[changing_idx][1] + 1)
            else:
                base_in_power[changing_idx][1] += base_in_power[changing_idx][1] + 1
                candidates[changing_idx] = base_in_power[changing_idx][0] ** (base_in_power[changing_idx][1] + 1)
            counter += 1
        changing_idx = candidates.index(min(candidates))
        # print(changing_idx)


        # for j in base_in_power:
        #     new_candidate = j[0] ** (j[1] + 1)
        #     if primes[prime_idx] <  new_candidate:
        #         base_in_power.append([primes[prime_idx],1])
        #         prime_idx +=1
        #         break
        #     else
    answer = 1
    answer_s = ""
    for i in base_in_power:
        answer *= i[0] ** i[1]
        answer_s += " " + str(i[0]) + "^"+  str(i[1]) + " x"

    print(answer_s)
    print(answer % 500500507)
@timethis
def main2(n):
    primes, sieve = sieve_of_eratosthenes(n * 15)
    print("sieve complete")
    prime_idx = 2
    changing_idx = 0
    base_in_power = [[2, 1]]
    candidates = [4]
    h = []
    heapq.heappush(h, 4)
    number_of_candidates = 0
    next_entry = 3
    counter = 2

    while counter <= n:
        # print(counter)
        changing_idx = candidates.index(h[0])
        if changing_idx == number_of_candidates and candidates[changing_idx] > next_entry:
            base_in_power.append([next_entry, 1])
            candidates.append(next_entry ** 2)
            heapq.heappush(h, next_entry ** 2)
            prime_idx += 1
            next_entry = primes[prime_idx]
            counter += 1
            number_of_candidates += 1
        else:
            base_in_power[changing_idx][1] += base_in_power[changing_idx][1] + 1
            candidates[changing_idx] = base_in_power[changing_idx][0] ** (base_in_power[changing_idx][1]+1)
            heapq.heappushpop(h, candidates[changing_idx])
            counter +=1
    answer = 1
    answer_s = ""

    for i in base_in_power:
        answer *= i[0] ** i[1]
        # answer_s += " " + str(i[0]) + "^"+  str(i[1]) + " x"

    # print(answer_s)
    print(answer % 500500507)

@timethis
def main3(n, MOD):
    primes, sieve = sieve_of_eratosthenes(50*n)
    primes_idx = 2
    heap = []
    heapq.heappush(heap, 2)
    print(heap)
    pre_mod = 2

    for i in range(1, n):
        temp = heap[0] * heap[0]
        if temp < primes[primes_idx]:
            pre_mod *= temp % MOD
            heapq.heappushpop(heap, temp)
        else:
            pre_mod *= primes[primes_idx]
            heapq.heappush(heap, primes[primes_idx])
            primes_idx += 1

    print("ksekinaei to mod") # 335.5031895637512
    print(pre_mod % MOD)


if __name__ == '__main__':
    main3(500500, 500500507)
