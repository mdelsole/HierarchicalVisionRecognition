import MarkovChain

# Our hierarchy is made up of a bunch of nodes. Nodes make up the layers, and layers make up the hierarchy


class Node(object):
    """ Each Node class has 2 main objects:
    1) Memory = Array of unique input patterns this node has seen from it's receptive field of lower nodes during
                training_datasets. These unique patterns will be refered to as c1, c2, ...
    2) Temporal Groups = Array of multiple subsets of Memory with no overlapping subsets. Each subset temporal
                         group will be represented as g1, g2, ...
        Example:
        memory = [c1, c2, c3, c4, c5]
        temporal_group = [ {c1, c3, c5}, {c2, c4} ] where g1 = {c1, c3, c5} and g2 = {c2, c4}
        NOTE: At nodes high in the hierarchy temporal groups will begin to represent complex objects.
              After understanding model/images/explanatory/object_manifolds.png one can think of a temporal group as an
              object manifold.
    :returns After training returns an active temporal group for each input pattern
    """
    def __init__(self):
        self.memory = []
        self.markov_graph = MarkovChain.MarkovChain()
        self.active_input_pattern_index = -1
        self.prev_active_input_pattern_index = -1

        self.temporal_groups = []
        self.active_temporal_group_index = -1

        # In the format (x1, y1, x2, y2) where (x1, y1) is the top left of the rectangle
        # and (x2, y2) is the bottom right of the rectangle. All rectangles are in the 4th
        # quadrant of the Euclidean plane where the negative y axis is positive.
        self.receptive_field_dimensions = None

    def add_unique_pattern(self, receptive_field):
        if len(self.memory) == 0:
            self.memory.append(receptive_field)
            self.active_input_pattern_index = len(self.memory) - 1
            return self.active_input_pattern_index, True
        else:
            for index, unique_pattern in enumerate(self.memory):
                if unique_pattern == receptive_field:
                    self.active_input_pattern_index = index
                    # already have this unique pattern
                    return self.active_input_pattern_index, False

            # otherwise receptive_field is a new pattern so add it
            self.memory.append(receptive_field)
            self.active_input_pattern_index = len(self.memory) - 1

            return self.active_input_pattern_index, True