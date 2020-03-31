import array
from StdSuites import null

match_score = 1
mismatch_score = -1
gap_penalty = -2


def scoring(match, mismatch, gap):
    # This method will be used to initialize the scoring scheme. If match, mismatch
    # and gap scores are given, then the scheme will be updated accordingly. If not
    # provided, default values of +1, -1 and -1 will be assigned to match, mismatch
    # and gap, respectively.

    if match == null or match <= 0:
        match = 1

    if mismatch == null or mismatch >= 0:
        mismatch = -1

    if gap == null or gap >= 0:
        gap = -1
# end of def scoring(match, mismatch, gap):


def greatest(val1, val2, val3):
    # Find the greatest value among given 3
    if val1 < val2:
        if val2 < val3:
            return val3
        else:
            return val2
    else:
        if val1 < val3:
            return val3
        else:
            return val1
# end of def greatest(val1, val2, val3):


def back_track_max_scores(panel, i, j, str1, str2):
    if i == 0 and j == 0:
        print str2 + ' vs ' + str1 + '\n'
        print '****************'
    else:
        cell = panel[i][j]
        for back_track in cell['back_track']:
            if back_track['x'] < i and back_track['y'] < j:
                new_str_1 = str1 + cell['x_axis_nec']
                new_str_2 = str2 + cell['y_axis_nec']
            elif back_track['x'] < i:
                if cell['is_edge']:
                    new_str_1 = str1 + cell['value']
                else:
                    new_str_1 = str1 + cell['x_axis_nec']
                # end of if
                new_str_2 = str2 + '_'
            elif back_track['y'] < j:
                new_str_1 = str1 + '_'
                if cell['is_edge']:
                    new_str_2 = str2 + cell['value']
                else:
                    new_str_2 = str2 + cell['y_axis_nec']
                # end of if
            # end of if
            back_track_max_scores(panel, back_track['x'], back_track['y'], new_str_1, new_str_2)
        # end of for back_track in cell['back_track']:
    # end of if
# end of def back_track_max_scores(panel, i, j, str1, str2):


# end of def back_track():


def needle(seq1, seq2):
    # When the two sequences are passed to this method, this method will perform
    # alignment according to the Needleman-Wunsch algorithm for Global Alignment
    # and print out one or more best alignments.
    panel = []

    for i in range(0, len(seq1) + 1):
        row = []
        for j in range(0, len(seq2) + 1):
            if i > 0:
                x_axis_nec = seq1[i - 1]
                if j == 0:
                    cell_value = i * gap_penalty
            else:
                x_axis_nec = 'Edge'
            # end of if

            if j > 0:
                y_axis_nec = seq2[j - 1]
                if i == 0:
                    cell_value = j * gap_penalty
            else:
                y_axis_nec = 'Edge'
            # end of if

            if i == 0 and j == 0:
                cell_value = 0
            # end of if

            cell = {}
            if x_axis_nec != 'Edge' and y_axis_nec != 'Edge':
                cell['is_edge'] = False
                cell['x_axis_nec'] = x_axis_nec
                cell['y_axis_nec'] = y_axis_nec
            elif x_axis_nec == 'Edge' and y_axis_nec == 'Edge':
                cell['is_edge'] = True
                cell['cell_value'] = 0
                cell['back_track'] = []
            else:
                if x_axis_nec == 'Edge':
                    value = y_axis_nec
                    x_back_track = i
                    y_back_track = j - 1
                else:
                    value = x_axis_nec
                    x_back_track = i - 1
                    y_back_track = j
                # end of if
                cell['is_edge'] = True
                cell['value'] = value
                cell['cell_value'] = cell_value
                cell['back_track'] = [{'x': x_back_track, 'y': y_back_track}]
            row.append(cell)
        # enf of for j in range of seq2
        panel.append(row)
    # end of for i in range of seq1

    for i in range(1, len(panel)):
        for j in range(1, len(panel[i])):
            if panel[i][j]['x_axis_nec'] == panel[i][j]['y_axis_nec']:
                diagonal_displacement = match_score
            else:
                diagonal_displacement = mismatch_score
            # end of if

            from_diagonal = int(panel[i - 1][j - 1]['cell_value']) + diagonal_displacement
            from_top = int(panel[i][j - 1]['cell_value']) + gap_penalty
            from_left = int(panel[i - 1][j]['cell_value']) + gap_penalty

            back_track = []
            greatest_match = greatest(from_diagonal, from_top, from_left)
            if greatest_match == from_diagonal:
                back_track.append({'x': i - 1, 'y': j - 1})
            if greatest_match == from_top:
                back_track.append({'x': i, 'y': j - 1})
            if greatest_match == from_left:
                back_track.append({'x': i - 1, 'y': j})
            # en of if(s)
            panel[i][j]['cell_value'] = greatest_match
            panel[i][j]['back_track'] = back_track

        # end of for j in range(1, len(panel[i])):
    # end of for i in range(1, len(panel)):

    if len(panel) > 0:
        last_row = panel[len(panel) - 1]
        if len(last_row) > 0:
            back_track_max_scores(panel, len(panel) - 1, len(last_row) - 1, '', '')

    # for row in panel:
    #     for cell in row:
    #         print cell['cell_value']
    #         print cell['back_track']
    #     #
    #     print '****'
# end of def needle(seq1, seq2):


needle('AAAC', 'AGC')
