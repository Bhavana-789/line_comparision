def line_equality(x1, y1, x2, y2):
    """
    function to find equality of two lines
    :param x1:first coordinate of line1
    :param y1:second coordinate of line2
    :param x2:first coordinate of line2
    :param y2:second coordinate of line2
    :return:equality of lines
    """
    len1 = y1 - x1
    len2 = y2 - x2

    if len1 == len2:
        return "lines are equal"
    else:
        return "lines are not equal"


if __name__ == "__main__":
    output = line_equality(3, 8, 2, 4)
    print(output)
