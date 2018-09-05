"""
Write a function to find the rectangular intersection of two given
love rectangles.

As with the example above, love rectangles are always "straight" and
never "diagonal." More rigorously: each side is parallel with either the
x-axis or the y-axis.

They are defined as dictionaries ↴ like this:

  my_rectangle = {

    # Coordinates of bottom-left corner
    'left_x'   : 1,
    'bottom_y' : 1,

    # Width and height
    'width'    : 6,
    'height'   : 3,

}

Your output rectangle should use this format as well.

"""

from collections import namedtuple

Rectangle = namedtuple('Rectangle', ['bottom', 'top', 'left', 'right'])


def rect_intersection(rect1: Rectangle, rect2: Rectangle) -> Rectangle:
    """
    Returns the intersection of two rectangles as a rectangle description.

    Returns None if they have no intersection.

    """
    if (rect1.bottom >= rect2.top
            or rect2.bottom >= rect1.top
            or rect1.left >= rect2.right
            or rect2.left >= rect1.right):
        return None

    left = max(rect1.left, rect2.left)
    bottom = max(rect1.bottom, rect2.bottom)
    top = min(rect1.top, rect1.top)
    right = min(rect1.right, rect2.right)

    assert bottom < top, f'{bottom} > {top}'
    assert left < right, f'{left} > {right}'

    return Rectangle(bottom, top, left, right)


def test(rect1, rect2, expected):
    result = rect_intersection(rect1, rect2)
    print(result)
    if expected is None:
        assert result is None
    else:
        assert result == expected


# None
test(Rectangle(1, 2, 1, 2), Rectangle(0, 1, 0, 1), None)

# None
test(Rectangle(1, 2, 1, 2), Rectangle(2, 3, 1, 2), None)

# None
test(Rectangle(1, 2, 1, 2), Rectangle(100, 200, 100, 200), None)

# None
test(Rectangle(100, 200, 100, 200), Rectangle(1, 2, 1, 2), None)

# Rectangle(1, 2, 1, 2)
test(Rectangle(1, 2, 1, 2), Rectangle(0, 2, 0, 2), Rectangle(1, 2, 1, 2))

# Rectangle(1, 2, 1, 2)
test(Rectangle(1, 2, 1, 2), Rectangle(1, 2, 1, 2), Rectangle(1, 2, 1, 2))

# Rectangle(2, 4, 5, 7)
test(Rectangle(1, 4, 1, 7), Rectangle(2, 6, 5, 8), Rectangle(2, 4, 5, 7))
