class Union:
    def __init__(self, n):
        self.parents = [r for r in range(n)]
        self.rank = [0] * n
    
    def find(self, n):
        while n != self.parents[n]:
            self.parents[n] = self.parents[self.parents[n]]
            n = self.parents[n]
        return n

    def union(self, x, y):
        px, py = self.find(x), self.find(y)

        if self.rank[px] > self.rank[py]:
            self.parents[py] = px
        elif self.rank[px] < self.rank[py]:
            self.parents[px] = py
        else:
            self.parents[py] = px
            self.rank[px] += 1


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        accountUnions = Union(len(accounts))
        accountDeconstructed = {}

        for i in range(len(accounts)):
            for j in range(1, len(accounts[i])):
                if accounts[i][j] in accountDeconstructed:
                    accountUnions.union(i, accountDeconstructed[(accounts[i][j])]) 
                else:
                    accountDeconstructed[accounts[i][j]] = i
        
        emailGroups = {}
        for email, i in accountDeconstructed.items():
            accountOwnerName = accountUnions.find(i)
            if accountOwnerName not in emailGroups:
                emailGroups[accountOwnerName] = []

            emailGroups[accountOwnerName].append(email)
        
        finalFormat = []
        for name, emailList in emailGroups.items():
            row = [accounts[name][0]]
            row.extend(sorted(emailList))
            finalFormat.append(row)

        return finalFormat


        