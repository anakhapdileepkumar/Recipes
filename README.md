# 🍳 Recipe Finder

## Problem Statement
You have a list of recipes and their ingredients.  
- You start with some ingredients in `supplies`.  
- Some ingredients may be other recipes you can make.  
- You can make a recipe only if **all its ingredients** are available.  
- Once made, a recipe becomes an ingredient for other recipes.  

Return all recipes you can create.


## Example
**Input:**
recipes = ["bread", "sandwich", "burger"]  
ingredients = [["flour", "water"], ["bread", "meat"], ["sandwich", "lettuce"]]  
supplies = ["flour", "water", "meat", "lettuce"]

**Output:**
["bread", "sandwich", "burger"]


## Approach
1. Start with the initial supplies.  
2. Use BFS/Topological Sort to check which recipes can be made.  
3. If all ingredients for a recipe are available, make it and add to supplies.  
4. Continue until no new recipes can be made.  
