# https://leetcode.com/problems/relative-ranks/description/?envType=company&envId=google&favoriteSlug=google-six-months&difficulty=EASY&role=full-stack

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sortedScore = sorted(score, reverse=True)
        scoreRankMapping = dict()
        for i in range(len(sortedScore)):
            if i == 0:
                scoreRankMapping[sortedScore[i]] = "Gold Medal"
            elif i == 1:
                scoreRankMapping[sortedScore[i]] = "Silver Medal"
            elif i == 2:
                scoreRankMapping[sortedScore[i]] = "Bronze Medal"
            else:
                scoreRankMapping[sortedScore[i]] = str(i + 1)
                
        answer = []
        for eachScore in score:
            answer.append(scoreRankMapping[eachScore])
        return answer
