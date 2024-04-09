class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        rotations = 0
        n = len(students)

        while rotations < n:
            if len(students) == 0 or len(sandwiches) == 0:
                break
                
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                rotations = 0
            else:
                students.append(students.pop(0))
                rotations += 1

        return len(students)







sol = Solution()
res = sol.countStudents([1,1,0,0], [0,1,0,1])
print(res)
