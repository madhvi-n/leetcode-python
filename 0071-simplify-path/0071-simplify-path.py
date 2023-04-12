class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for char in path.split("/"):
            if stack and char == "..":
                stack.pop()
            
            elif char not in [".", "", ".."]:
                stack.append(char)
                
        return "/" + "/".join(stack)