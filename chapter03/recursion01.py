import random
# TODO complete this code


class Box(object):
    def __init__(self, pile=None):
        self.label = "box"
        self.pile = pile

    def make_a_pile_to_look_through(self):
        return self.pile


class Key(object):
    def __init__(self):
        self.label = "key"


class Pile(object):
    def __init__(self, many_box: list):
        self.many_box = many_box

    def grab_a_box(self):
        box_num = len(self.many_box)
        grab_idx = random.randint(0, box_num)
        chosen_box = self.many_box.pop(grab_idx)
        return chosen_box


def look_for_key_by_loop(main_box):
    pile = main_box.make_a_pile_to_look_through()
    while pile is not None:
        box = pile.grab_a_box()
        if box.pile is None:
            continue
        for item in box.pile:
            if isinstance(item, Box):
                pile.append(item)
            elif isinstance(item, Key):
                print("found the key")
    return


def look_for_key_by_recursion(box):
    for item in box:
        if isinstance(item, Box):
            look_for_key_by_recursion(item)
        elif isinstance(item, Key):
            print("find the key")
    return


if __name__ == "__main__":
    box1 = Box()
    box2 = Box()
    key = Key()
    # build a pile
    box3 = Box(key)
    pile_list = Pile([box1, box2, box3])
    # build main box
    box4 = Box(pile_list)

    look_for_key_by_loop(box4)
    # by understanding the calling stack, you should know that
    # the "Pile" during recursion is actually stored in the "Stack"
    look_for_key_by_recursion(box4)