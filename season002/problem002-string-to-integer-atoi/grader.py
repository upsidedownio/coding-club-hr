import ast
from submissions.wonwoo import Solution, TreeNode


def main():
    testcaseFile = open('./testcases.txt', 'r')
    testcases = testcaseFile.read().split('\n\n')
    # print(testcases)

    # testcases.map(lambda t: print(t))
    for t in testcases:
        inputs = t.split('\n')
        nodes = ast.literal_eval(inputs[0])
        ans = Solution.inorderTraversal(root=nodes)
        print('my answer:', ans, 'answer:', ast.literal_eval(inputs[1]))


if __name__ == '__main__':
    main()