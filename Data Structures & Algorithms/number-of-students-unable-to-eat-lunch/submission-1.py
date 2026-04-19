from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # students are in a queue FIFO
        # sandwiches are on a stack LIFO
        # count how many students refused a sandwich
        # when a student takes a sandwich
            # reset counter, pop sandwich, remove student
        # when a student refuses the sandwich
            # if counter reaches length of students
                # we are done, return length of students

        # use a queue for O(1) queue operations
        student_queue = deque(students)
        sandwich_stack = deque(sandwiches)
        refuse_counter = 0

        while refuse_counter < len(student_queue):
            if student_queue[0] == sandwich_stack[0]:
                student_queue.popleft()
                sandwich_stack.popleft()
                refuse_counter = 0
            else:
                student_queue.rotate(-1)
                refuse_counter += 1

        return len(student_queue)

