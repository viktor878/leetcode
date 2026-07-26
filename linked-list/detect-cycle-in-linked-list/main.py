class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Create nodes
node1 = Node(3)
node2 = Node(2)
node3 = Node(0)
node4 = Node(-4)

# Link nodes
node1.next = node2
node2.next = node3
node3.next = node4

# Create a cycle
node4.next = node2

head = node1


# Print limited traversal
current = head
steps = 10

while current and steps > 0:
    print(current.data, end=" -> ")
    current = current.next
    steps -= 1

print("...")


class Solution:
    def hasCycle(self, head: Node) -> bool:
        p1 = head
        p2 = head

        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next

            if p1 == p2:
                return True

        return False


if __name__ == "__main__":
    sol = Solution()
    result = sol.hasCycle(head)

    if result:
        print("Cycle detected")
    else:
        print("No cycle")