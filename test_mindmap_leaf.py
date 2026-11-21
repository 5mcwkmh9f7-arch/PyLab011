from mindmap_leaf import MindMapLeaf

leaf = MindMapLeaf("Jean-Luc Picard", "circle")
print(str(leaf))  # Should display "((Jean-Luc Picard))"
leaf.display(2)   # Should display "  ((Jean-Luc Picard))" with two spaces

print("MindMapLeaf tests completed!")
