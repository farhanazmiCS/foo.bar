# Solution "Elevator Maintenance"
def solution(list):

    # Key for sorting by MAJOR
    def major(element):
        return int(element.split('.')[0])

    # Key for sorting by MINOR
    def minor(element):
        try:
            return int(element.split('.')[1])
        except IndexError:
            return -1

    # Key for sorting by REVISION
    def revision(element):
        try:
            return int(element.split('.')[2])
        except IndexError:
            return -1

    # Sorts the ENTIRE list by MAJOR
    list = sorted(list, key=major)

    # Sorts sublists by REVISION 
    def sortRevision(list):
        for i in range(1, len(list)):
            # Try-Except is used as splitting an integer value (e.g 2) will lead to IndexError.
            try:
                if list[0].split('.')[1] != list[i].split('.')[1]:
                    return sorted(list[:i], key=revision) + sortRevision(list[i:])
                # Sorts the last MINOR sublist.
                elif i == len(list) - 1:
                    return sorted(list[:i+1], key=revision)
            # If element in the list cannot be split, set it to '0' (e.g 2 is actually 2.0).
            except IndexError:
                if '0' != list[i].split('.')[1]:
                    return sorted(list[:i], key=revision) + sortRevision(list[i:])
                elif i == len(list) - 1:
                    return sorted(list[:i+1], key=revision)
        return list

    # Sorts sublists by MINOR
    def sortMinor(list):
        # Loops through the ENTIRE list. If the MAJOR on the ith element does not match the major on index 0 (First), sort from the first element all the way to (i - 1), by MINOR.
        for i in range(1, len(list)):
            # Checks the MAJOR element. If list[0] == list[1], continue with iteration. Else, continue with iteration.
            if list[0].split('.')[0] != list[i].split('.')[0]:
                # Check takes the remaining unsorted list (by minor) as input
                return sortRevision(sorted(list[:i], key=minor)) + sortMinor(list[i:])
            # Sorts the last MAJOR sublist
            elif i == len(list) - 1:
                return sortRevision(sorted(list[:i+1], key=minor))
        return list

    return sortMinor(list)