# https://leetcode.com/problems/logger-rate-limiter/description/?envType=company&envId=google&favoriteSlug=google-three-months&difficulty=EASY&role=full-stack

class Logger:

    def __init__(self):
        self.messagesMap = dict()
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.messagesMap:
            self.messagesMap[message] = timestamp
            return True
        if timestamp - self.messagesMap[message] >= 10:
            self.messagesMap[message] = timestamp
            return True
        else:
            return False

        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
