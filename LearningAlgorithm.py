class CommonCorticalAlgorithmV1(object):
    """ 1st version of common learning algorithm.
    :param network: hierarchical connected layers
    """

    # Defining a static variable time_step
    time_step = 0

    def __init__(self, network, time_steps=0):
        self.network = network
        self.time_steps = time_steps
        self.learning_phase = True
        self.prev_active_input_pattern_index = -1

    def learn_one_time_step(self, input_layer):
        """
        :param input_layer: 2D int array where '1' is black and '0' is white
        """
        # start at the bottom layer
        for i in range(len(self.network.layers)):
            current_layer = self.network.layers[i]
            if i == 0:
                # we are at the bottom most layer
                # 1) iterate through nodes in this layer
                nodes = current_layer.nodes
                for r in range(len(nodes)):
                    for c in range(len(nodes[0])):
                        # 2) get receptive field from input layer
                        # print('nodes[' + str(r) + '][' + str(c) + '].receptive_field_dimensions = '
                        #       + str(nodes[r][c].receptive_field_dimensions))
                        r_initial = int(nodes[r][c].receptive_field_dimensions[0])
                        r_final = int(nodes[r][c].receptive_field_dimensions[2] + 1)  # range(1, 3) = 1, 2
                        c_initial = int(nodes[r][c].receptive_field_dimensions[1])
                        c_final = int(nodes[r][c].receptive_field_dimensions[3] + 1)

                        current_node_receptive_field = set()
                        for x in range(r_initial, r_final):
                            for y in range(c_initial, c_final):
                                if input_layer[x, y] == 1:
                                    current_node_receptive_field.add((x, y))

                        # 3) if you find a unique receptive field add it to the node's memory
                        cur_active_input_pattern_index, ret = nodes[r][c].add_unique_pattern(current_node_receptive_field)

                        # TODO remove these before merge
                        if nodes[r][c].prev_active_input_pattern_index != -1:
                            # print(nodes[r][c].prev_active_input_pattern_index, cur_active_input_pattern_index, "........................................................................")
                            nodes[r][c].markov_graph.connect(nodes[r][c].prev_active_input_pattern_index, cur_active_input_pattern_index)
                        # CommonCorticalAlgorithmV1.time_step == 9 because we have to print the mk graph for the last pattern
                        if CommonCorticalAlgorithmV1.time_step == self.time_steps:
                            # print('Markov Graph for patch no =', r, ',', c)
                            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                            nodes[r][c].markov_graph.draw_graph(r, c, 1)
                        nodes[r][c].prev_active_input_pattern_index = cur_active_input_pattern_index

        # self._learn_transitional_probabilities(input_layer)
        # TODO: _form_temporal_groups()
        CommonCorticalAlgorithmV1.time_step += 1
        return

    def switch_to_sensing_mode(self):
        self.learning_phase = False
        # this function may be unnecessary

    def categorize_current_image(self):
        # check if learning_phase is turned off
        # TODO: categorize current input image
        return None