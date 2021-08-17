# Solution "Skipping Work (Iterative)"
def solution(list1, list2):
    list1.sort()
    list2.sort()
    
    def checkextra(sorted1, sorted2):
        if len(sorted1) > len(sorted2):
            for i in range(len(sorted1)):
                if sorted1[i] != sorted2[i]:
                    return sorted1[i]
        elif len(sorted2) > len(sorted1):
            for i in range(len(sorted1)):
                if sorted2[i] != sorted1[i]:
                    return sorted2[i]
    return checkextra(list1, list2)
