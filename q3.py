


class TreeNode:
    def __init__(self, salary=0, left=None, right=None):
        self.salary = salary
        self.left = left
        self.right = right


def count_fair_managers(root):
    def check(node):
        if node is None:
            return [0, 0, 0]

        left = check(node.left)
        right = check(node.right)

        salaries = left[0] + right[0] + [node.salary]

        total = 0
        for i in range(len(salaries)):
            total += salaries[i]

        count = len(salaries)
        fair = left[1] + right[1]

        if node.salary == total // count:
            fair += 1

        return salaries, fair, count

    if root is None:
        return 0

    ans = check(root)
    return ans[1]