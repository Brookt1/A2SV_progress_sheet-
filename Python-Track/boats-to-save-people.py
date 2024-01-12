class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:


        people.sort()
        l,r=0,len(people)-1
        num_boat=0
        while l<=r:
            if people[l]+people[r]<=limit:
                l+=1
            r-=1
            num_boat+=1
        return num_boat


        
        