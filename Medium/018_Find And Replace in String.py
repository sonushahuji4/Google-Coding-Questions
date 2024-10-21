# https://leetcode.com/problems/find-and-replace-in-string/


class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        # Create a list of tuples containing the index, source, and target
        replacements = sorted(zip(indices, sources, targets), reverse=True)
        
        # Convert the string into a list to manipulate it easily
        s_list = list(s)
        
        for index, src, tgt in replacements:
            # Check if the substring at the current index matches the source string
            if s[index:index+len(src)] == src:
                # Replace the matching part with the target string
                s_list[index:index+len(src)] = list(tgt)
        
        # Join the list back into a string
        return "".join(s_list)
