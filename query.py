

class Query:

    and_items = []  # simple items

    def __init__(self, item):
        self.and_items = item


class AdvancedQuery(Query):

    complete_items = []
    or_items = []
    not_items = []

    def __init__(self, and_items, complete_items, or_items, not_items):
        self.and_items = and_items
        self.complete_items = complete_items
        self.or_items = or_items
        self.not_items = not_items
