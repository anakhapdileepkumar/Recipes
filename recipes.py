from collections import defaultdict, deque

def findAllRecipes(recipes, ingredients, supplies):
    indegree = {r: 0 for r in recipes}
    graph = defaultdict(list)
    
    
    for r, ing_list in zip(recipes, ingredients):
        for ing in ing_list:
            graph[ing].append(r)
            if ing not in recipes:
                continue
            indegree[r] += 1
    
    
    queue = deque(supplies)
    res = []
    
    while queue:
        item = queue.popleft()
        for nei in graph[item]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                res.append(nei)
                queue.append(nei)
    
    return res


recipes = ["bread", "sandwich", "burger"]
ingredients = [["flour", "water"], ["bread", "meat"], ["sandwich", "lettuce"]]
supplies = ["flour", "water", "meat", "lettuce"]

print(findAllRecipes(recipes, ingredients, supplies))
