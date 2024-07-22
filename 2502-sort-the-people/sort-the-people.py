class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        combined = list(zip(names, heights))
        sorted_combined= sorted(combined, key= lambda x:x[1], reverse = True )
        sorted_names= [names for names, heights in sorted_combined]
        return sorted_names