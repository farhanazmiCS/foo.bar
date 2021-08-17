# Solution "Skipping Work"
def solution(list1, list2):
    # Sorts the list
    list1.sort()
    list2.sort()

    def checkextra(sorted1, sorted2):
        # Base case 1: Checks if the first element on the list are the same
        if sorted1[0] != sorted2[0]:
            if len(sorted1) > len(sorted2):
                return sorted1[0]
            else:
                return sorted2[0]
        # Base case 2: 2nd list contains the extra element
        elif len(sorted1) == 1 and len(sorted2) == 2:
            if sorted1[0] == sorted2[0]:
                return sorted1[0]
            else:
                return sorted2[1]
        # Base case 3: 1st list contains the extra element
        elif len(sorted1) == 2 and len(sorted1) == 1:
            if sorted1[0] == sorted2[0]:
                return sorted2[0]
            else:
                return sorted1[1]
        # Recursive Case
        else:
            return checkextra(sorted1[1:len(sorted1)], sorted2[1:len(sorted2)])
    return checkextra(list1, list2)