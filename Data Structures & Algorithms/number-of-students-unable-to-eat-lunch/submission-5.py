class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # loop through studends and pop stack accordingly 
        # run while refusal counter < len if pop then reset counter
        # when loop exits return length of students

        res = len(students)
        pref_map = Counter(students)

        for s in sandwiches:
            if pref_map[s] > 0:
                pref_map[s] -= 1
                res -= 1
            else:
                return res
        
        return res

        # DLL solution

        from collections import deque

        count = 0
        student_que = deque(students)
        sandwich_que = deque(sandwiches)

        while count < len(student_que):
            if student_que[0] == sandwich_que[0]:
                student_que.popleft()
                sandwich_que.popleft()
                count = 0
            else:
                student_que.rotate(-1)
                count += 1

        return len(student_que)

        # list solution

        refuse_counter = 0
        while refuse_counter < len(students):
            if students[0] == sandwiches[0]:
                del students[0]
                del sandwiches[0]
                refuse_counter = 0
            else:
                students.append(students.pop(0))
                refuse_counter += 1
        return len(students)