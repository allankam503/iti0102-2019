def combo_string(s1: str, s2: str) -> str:
    """
    Return a new string of the form short + long + short.

    Given 2 strings, a and b, return a string of the form short+long+short,
    with the shorter string on the outside and the longer string on the inside.
    The strings will not be the same length, but they may be empty (length 0).

    combo_string('Hello', 'hi') → 'hiHellohi'
    combo_string('hi', 'Hello') → 'hiHellohi'
    combo_string('aaa', 'b') → 'baaab'

    :param s1:
    :param s2:
    :return:
    """
    if len(s1) > len(s2):
        result = s2 + s1 + s2
    else:
        result = s1 + s2 + s1
    return result