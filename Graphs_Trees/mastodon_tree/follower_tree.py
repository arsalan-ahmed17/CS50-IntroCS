from binary_search_tree import BST

def main():
    usernames = ['TND_JK', 'Harrington_Alex', 'Dko', 'GeraldineDawn',
                 'Bret_Fisher', 'HxQ', 'mixtur', 'Zenithron', 'BryanBenson']

    # Adding usernames to the BST
    for username in usernames:
        BST.add(username)

    # Demonstrating iterative search
    print("Iterative Search for 'Harrington_Alex':")
    # Expected: Node with username 'Harrington_Alex'
    print(BST.iterative_search(BST.root, 'Harrington_Alex'))
    print("\nIterative Search for 'Harrington_Markus' (does not exist):")
    # Expected: False
    print(BST.iterative_search(BST.root, 'Harrington_Markus'))

    # Demonstrating recursive search
    print("\nRecursive Search for 'Dko':")
    # Expected: Node with username 'Dko'
    print(BST.recursive_search(BST.root, 'Dko'))
    print("\nRecursive Search for 'Eko' (does not exist):")
    # Expected: False
    print(BST.recursive_search(BST.root, 'Eko'))


    # Demonstrating preorder traversal
    print("\nPreorder Traversal:")
    # Expected: ['TND_JK', 'Harrington_Alex', 'Dko', 'Bret_Fisher', 'BryanBenson', 'GeraldineDawn', 'HxQ', 'mixtur', 'Zenithron']
    print(BST.preorder())

    # Demonstrating inorder traversal
    print("\nInorder Traversal:")
    # Expected: ['Bret_Fisher', 'BryanBenson', 'Dko', 'GeraldineDawn', 'Harrington_Alex', 'HxQ', 'TND_JK', 'Zenithron', 'mixtur']
    print(BST.inorder())

    # Demonstrating postorder traversal
    print("\nPostorder Traversal:")
    # Expected: ['BryanBenson', 'Bret_Fisher', 'GeraldineDawn', 'Dko', 'HxQ', 'Harrington_Alex', 'Zenithron', 'mixtur', 'TND_JK']
    print(BST.postorder())

if __name__ == '__main__':
    main()
