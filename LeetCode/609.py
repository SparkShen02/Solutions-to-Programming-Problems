class Solution:
    '''
    Use a dictionary, with the contents of files stored as keys and the paths to files stored as values. 
    Time complexity: O(n), Space complexity: O(n). 
    '''
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content2file = {}
        for path in paths:
            path = path.split(' ')
            dir = path[0] + '/'
            for file in path[1:]:
                j = len(file) - 1
                while True:
                    if file[j] == ')':
                        break
                    j -= 1
                i = j
                while True:
                    if file[i] == '(':
                        break
                    i -= 1
                fileName, fileContent = file[:i], file[i+1:j+2]
            
                if fileContent not in content2file:
                    content2file[fileContent] = [dir + fileName]
                else:
                    content2file[fileContent].append(dir + fileName)
        
        ans = []
        for fileNames in content2file.values():
            if len(fileNames) > 1:
                ans.append(fileNames)
        return ans