from typing import Tuple, List, Union

class BST:
    """
    A class that represents a Binary Search Tree (BST).

    Attributes:
    ----------
    root: BST
        The root node of the BST.
    """

    # The root node of the BST
    root = None

    def __init__(self, username: str) -> None:
        """
        Constructor for the BST objects.

        Parameters:
        ----------
        username: str
            The username to be stored in a BST object.
        """
        self.username = username
        self.left = None
        self.right = None

    @staticmethod
    def add(username: str) -> None:
        """
        Creates a root if the BST does not have one yet, otherwise adds a new BST object at the right place in the mastodon_tree.

        Parameters:
        ----------
        username: str
            The username of the added node (vertex).
        """
        if BST.root is None:
            BST.root = BST(username)
        else:
            BST._add_recursive(BST.root, username)

    @staticmethod
    def _add_recursive(node: 'BST', username: str) -> None:
        """
        Helper method to add a new username to the BST recursively.

        Parameters:
        ----------
        node: BST
            The current node in the BST.
        username: str
            The username to be added.
        """
        if username < node.username:
            if node.left is None:
                node.left = BST(username)
            else:
                BST._add_recursive(node.left, username)
        else:
            if node.right is None:
                node.right = BST(username)
            else:
                BST._add_recursive(node.right, username)

    @staticmethod
    def iterative_search(root: 'BST', to_find: str) -> Union['BST', bool]:
        """
        Searches for a node in the BST using an iterative approach.

        Parameters:
        ----------
        root: BST
            The current root node for the search.
        to_find: str
            The username to find in the BST.

        Returns:
        -------
        Union[BST, bool]
            The found BST node or False if not found or root is None
        """
        current = root
        while current is not None:
            if to_find == current.username:
                return current
            elif to_find < current.username:
                current = current.left
            else:
                current = current.right
        return False

    @staticmethod
    def recursive_search(root: 'BST', to_find: str) -> Union['BST', bool]:
        """
        Searches for a node in the BST using a binary search approach.

        Parameters:
        ----------
        root: BST
            The current root node for the search.
        to_find: str
            The username to find in the BST.

        Returns:
        -------
        Union[BST, bool]
            The found BST node or False if not found or root is None.
        """
        if root is None:
            return False
        if to_find == root.username:
            return root
        elif to_find < root.username:
            return BST.recursive_search(root.left, to_find)
        else:
            return BST.recursive_search(root.right, to_find)

    @staticmethod
    def preorder() -> List[str]:
        """
        Performs a preorder Depth-First Search (DFS) on the BST.

        Returns:
        -------
        List[str]
            A list of the usernames in preorder.
        """
        return BST._preorder_recursive(BST.root)

    @staticmethod
    def _preorder_recursive(node: 'BST') -> List[str]:
        """
        Helper method to perform a preorder traversal recursively.

        Parameters:
        ----------
        node: BST
            The current node in the BST.

        Returns:
        -------
        List[str]
            A list of the usernames in preorder.
        """
        if node is None:
            return []
        return [node.username] + BST._preorder_recursive(node.left) + BST._preorder_recursive(node.right)

    @staticmethod
    def inorder() -> List[str]:
        """
        Performs an inorder Depth-First Search (DFS) on the BST.

        Returns:
        -------
        List[str]
            A list of the usernames in inorder.
        """
        return BST._inorder_recursive(BST.root)

    @staticmethod
    def _inorder_recursive(node: 'BST') -> List[str]:
        """
        Helper method to perform an inorder traversal recursively.

        Parameters:
        ----------
        node: BST
            The current node in the BST.

        Returns:
        -------
        List[str]
            A list of the usernames in inorder.
        """
        if node is None:
            return []
        return BST._inorder_recursive(node.left) + [node.username] + BST._inorder_recursive(node.right)

    @staticmethod
    def postorder() -> List[str]:
        """
        Performs a postorder Depth-First Search (DFS) on the BST.

        Returns:
        -------
        List[str]
            A list of the usernames in postorder.
        """
        return BST._postorder_recursive(BST.root)

    @staticmethod
    def _postorder_recursive(node: 'BST') -> List[str]:
        """
        Helper method to perform a postorder traversal recursively.

        Parameters:
        ----------
        node: BST
            The current node in the BST.

        Returns:
        -------
        List[str]
            A list of the usernames in postorder.
        """
        if node is None:
            return []
        return BST._postorder_recursive(node.left) + BST._postorder_recursive(node.right) + [node.username]



