from collections import deque, defaultdict
import math

# Graph where nodes are connected if they differ by one letter
# Is there a path from beginWord, along the words in wordList, and ending at endWord?
#
# How to detect edges (= words that are one letter away?)
# Mask one char at a time
# Hash all words with char at that index masked
# Collisions = neighboring nodes
#
# How to find least path after building graph?
# Djikstra's probably idk

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        wordLen = len(beginWord)

        # Turn strings into lists bc string splicing is inefficient as balls
        #beginWord = tuple(beginWord)
        #endWord = tuple(endWord)
        #for i in range(len(wordList)):
        #    wordList[i] = tuple(wordList[i])

        # Mask the letter at given index
        # E.g. mask("hello", 2) = "he_lo"
        def mask(word, idx):
            return word[:idx] + '_' + word[(idx + 1):]
        
        # Build graph adjacencies list
        # Caveat: rather than connecting nodes to each other,
        #   connect them to the masked string
        adj = {}

        # Iterate, masking each char individually
        for idx in range(wordLen):
            for word in wordList:
                
                masked = mask(word, idx)
                
                if masked not in adj:
                    adj[masked] = []
                
                adj[masked].append(word)

        # Wacky implementation of Djikstra's
        todo = deque()
        visited = set()
        dists = defaultdict(lambda: math.inf)
        
        # BFS
        todo.append(beginWord)
        dists[beginWord] = 1 # Starts at 1 because the transition sequence from beginWord -> beginWord is length 1
        while todo:
            
            # Visit next node in queue
            word = todo.popleft()
            visited.add(word)
            distFromBegin = dists[word]

            # Visit all neighbors (1 char away)
            for idx in range(len(word)):
                
                masked = mask(word, idx)
                if masked not in adj: continue
                
                # Update distance and add to queue (unless we found endWord, then terminate)
                for neighbor in adj[masked]:
                    dists[neighbor] = min(dists[neighbor], distFromBegin + 1)
                    
                    if neighbor == endWord:
                        return dists[neighbor]
                    elif neighbor not in visited:
                        todo.append(neighbor)
                
        return 0