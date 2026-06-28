class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.curr_page = 0
        self.length = 1

    def visit(self, url: str) -> None:
        self.curr_page += 1
        if self.curr_page == len(self.history):
            self.history.append(url)
            self.length += 1
        else:
            self.history[self.curr_page] = url
            self.length = self.curr_page + 1

    def back(self, steps: int) -> str:
        self.curr_page = max(0, self.curr_page - steps)
        return self.history[self.curr_page]

    def forward(self, steps: int) -> str:
        self.curr_page = min(self.length - 1, self.curr_page + steps)
        return self.history[self.curr_page]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)