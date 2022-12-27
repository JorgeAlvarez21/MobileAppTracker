"""Linked list pagination routing"""


class RouteNode:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent

    def __str__(self):
        return str(self.name)

    def __repr__(self):
        return str(self.name)


class PaginationRouting:
    def __init__(self, initial_route='home'):
        self.initial_route = initial_route
        self.node_tail = None
        self.node_head = RouteNode(initial_route)

    def addRoute(self, new_route):
        node_current = RouteNode(new_route)
        if self.node_head.parent is None:
            self.node_tail = self.node_head
            self.node_head = node_current
            self.node_head.parent = self.node_tail
        else:
            node_current.parent = self.node_head
            self.node_head = node_current

    def popRoute(self):
        node_current = self.node_head
        self.node_head = node_current.parent

    def viewAllRoutes(self):
        node_current = self.node_head
        while node_current.parent is not None:
            print(node_current.name)
            node_current = node_current.parent
        else:
            print(node_current.name)
            return str(node_current.name)

    def goBackToInitial(self):
        node_current = self.node_head
        self.node_head = self.node_tail
