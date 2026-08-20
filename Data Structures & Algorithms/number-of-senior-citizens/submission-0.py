class Solution:
    def countSeniors(self, details: List[str]) -> int:
        # parse the -3, -4 index of each str
        # convert to num and check
        # increment count of seniors and return ans

        senior_count = 0

        for person in details:
            age = int(person[-4:-2])
            if age > 60:
                senior_count += 1

        return senior_count