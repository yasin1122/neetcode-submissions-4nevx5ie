class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # loop through studends and pop stack accordingly 
        # run while refusal counter < len if pop then reset counter
        # when loop exits return length of students

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