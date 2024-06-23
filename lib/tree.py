class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    return self.depth_first_recursive(self.root, id)

  def depth_first_recursive(self, node, id):
    for child in node['children']:
      if child['id'] == id:
        return child
      else:
        return self.depth_first_recursive(child, id)
      

  def breadth_first_search(self, node, id):
    nodes_to_visit = [node]

    while len(nodes_to_visit) > 0:
      # 1. Remove the first node from the `nodes_to_visit` list
      node = nodes_to_visit.pop(0)
      # 2. Check to see if it's the node we're searching for
      if node['id'] == id:
        return node
      # 3. Add its children (if any) to the END of the `nodes_to_visit` list
      nodes_to_visit = nodes_to_visit + node['children']

    return None
