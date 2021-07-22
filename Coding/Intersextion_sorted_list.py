# User function Template for python3

class Solution:

    # Function to return a list containing the union of the two arrays.
    def mergeArrays(self, a, b, n, m):
        '''
        :param a: given sorted array a
        :param n: size of sorted array a
        :param b: given sorted array b
        :param m: size of sorted array b
        :return:  The union of both arrays as a list
        '''
        # code here
        i = 0
        j = 0
        union = []
        while (i < n and j < m):
            if a[i] < b[j]:
                if a[i] not in union:
                    union.append(a[i])
                    i += 1
            elif a[i] > b[j]:
                if b[j] not in union:
                    union.append(b[j])
                    j += 1
            else:
                if a[i] not in union:
                    union.append(a[i])
                    i += 1
                    j += 1
        while (i < n):
            if a[i] not in union:
                union.append(a[i])
                i += 1
        while (j < m):
            if b[j] not in union:
                union.append(b[j])
                j += 1
        return union
