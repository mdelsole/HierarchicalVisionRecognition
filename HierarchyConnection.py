class ConnectTypes(object):
    @staticmethod
    def rectangle_connect(input_cells, layer, x_axis_overlap, y_axis_overlap):
        """connects an rectangle portion of an input layer to a layer of nodes
        :param input_cells: 2D int array where '1' is black and '0' is white
        :param layer: layer to connect input_cells to
        :param x_axis_overlap: number of input cells to overlap along x axis input cells
        :param y_axis_overlap: number of input cells to overlap along y axis input cells
        """
        top_row_length = len(layer.nodes)
        top_col_length = len(layer.nodes[0])
        bot_row_length = len(input_cells)
        bot_col_length = len(input_cells[0])

        for row_top in range(top_row_length):
            row_receptive_field = ConnectTypes.__update_receptive_field_dimension_length(
                top_row_length, bot_row_length, row_top, y_axis_overlap)
            row_b_initial = row_receptive_field[0]
            row_b_final = row_receptive_field[1]

            for col_top in range(top_col_length):
                col_receptive_field = ConnectTypes.__update_receptive_field_dimension_length(
                    top_col_length, bot_col_length, col_top, x_axis_overlap)
                col_b_initial = col_receptive_field[0]
                col_b_final = col_receptive_field[1]

                # actually add connection dimensions from bottom input cells receptive field to top layer node
                layer.nodes[row_top][col_top].receptive_field_dimensions = (row_b_initial, col_b_initial, row_b_final,
                                                                            col_b_final)
                # print('layer.nodes[' + str(row_top) + '][' + str(col_top) + '].receptive_field_dimensions = ' + \
                #       str(layer.nodes[row_top][col_top].receptive_field_dimensions))

    @staticmethod
    def __update_receptive_field_dimension_length(top_length, bot_length, top_index, overlap=False):
        if top_length > bot_length:
            raise ValueError('top_length must be <= bot_length')

        if top_index < bot_length % top_length:
            b_initial = top_index * (bot_length / top_length) + top_index
            b_final = (top_index + 1) * (bot_length / top_length) + (top_index + 1) - 1  # -1 of next row b_initial
        else:
            b_initial = top_index * (bot_length / top_length) + bot_length % top_length
            b_final = (top_index + 1) * (bot_length / top_length) + bot_length % top_length - 1

        without_overlap = (b_initial, b_final)

        # TODO if overlap==0 this should pose no effect but it does.
        if overlap:

            new_b_initial = without_overlap[0] - overlap
            if new_b_initial < 0:
                new_b_initial = 0

            new_b_final = without_overlap[1] + overlap
            if new_b_final > bot_length - 1:
                new_b_final = bot_length - 1

            return (new_b_initial, new_b_final)

        return without_overlap