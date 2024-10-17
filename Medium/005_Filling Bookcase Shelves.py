# https://leetcode.com/problems/filling-bookcase-shelves/description/

class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:

        # Approach One
        def getMinHeightOfShelves(i, currentShelfWidth, shelfHeight, booksLength):
            if i == booksLength: return shelfHeight

            bookWidth, bookHeight = books[i]

            pickBook = float('inf')
            if currentShelfWidth >= bookWidth:
                pickBook = getMinHeightOfShelves(i+1, currentShelfWidth - bookWidth, max(shelfHeight, bookHeight), booksLength)
            skipBook = shelfHeight + getMinHeightOfShelves(i+1, shelfWidth - bookWidth, bookHeight, booksLength)

            return min(pickBook, skipBook)

        return getMinHeightOfShelves(0, shelfWidth, 0, len(books))

        
