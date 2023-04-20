from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class TreeNode:
    value: int | None = field(repr=True, default=0)
    left: TreeNode | None = field(repr=True, default=None)
    right: TreeNode | None = field(repr=True, default=None)


def from_list(elements: list[int]) -> TreeNode:
    if not elements:
        return []
    root_node = TreeNode(value=elements[0])
    nodes = [root_node]

    for idx, el in enumerate(elements[1:]):
        if el is None:
            continue
        parent_node = nodes[idx // 2]
        is_left = (idx % 2 == 0)
        node = TreeNode(value=el)
        if is_left:
            parent_node.left = node
        else:
            parent_node.right = node
        nodes.append(node)

    return root_node


def to_list(tree: TreeNode | None, result: list[int] = None) -> list[int]:
    if result is None:
        result = []
    if not tree:
        return result
    
    #result.append(tree.value)
    if tree.left:
        result.append(tree.left.value)
    if tree.right:
        result.append(tree.right.value)
    to_list(tree.left, result)
    to_list(tree.right, result)

    return result


# 100. Same Tree (easy)
def is_same_tree(p: TreeNode | None, q: TreeNode | None) -> bool:
    if not p and not q:
        return True
    if not p or not q or p.value != q.value:
        return False
    
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)


# 226. Invert Binary Tree (easy)
def invert_tree(root: TreeNode | None) -> TreeNode | None:
    if not root:
        return root
    invert_tree(root.left)
    invert_tree(root.right)
    root.left, root.right = root.right, root.left

    return root
