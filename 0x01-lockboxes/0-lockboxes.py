<<<<<<< HEAD
#!/usr/bin/env python3
'''Task 0: Lockboxes
'''
def canUnlockAll(boxes):
    # Number of boxes
    n = len(boxes)
    # Set to keep track of unlocked boxes
    unlocked = [False] * n
    unlocked[0] = True  # First box is unlocked by default
    # Queue for BFS approach
    queue = [0]  # Start with the first box
    
    while queue:
        current_box = queue.pop(0)
        for key in boxes[current_box]:
            if key < n and not unlocked[key]:
                unlocked[key] = True
                queue.append(key)
    
    # Check if all boxes are unlocked
    return all(unlocked)

# Example usage:
if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))  # True

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))  # True

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))  # False
=======
#!/usr/bin/python3
def canUnlockAll(boxes):
    # Initialize the list to track visited boxes
    n = len(boxes)
    visited = [False] * n
    visited[0] = True  # The first box is unlocked

    # Stack for DFS
    stack = [0]

    # Perform DFS
    while stack:
        box = stack.pop()

        for key in boxes[box]:
            if key < n and not visited[key]:
                visited[key] = True
                stack.append(key)

    # Check if all boxes are visited
    return all(visited)
>>>>>>> 740a6efa1160d5676113e91ede2a8e3b5a73244a
