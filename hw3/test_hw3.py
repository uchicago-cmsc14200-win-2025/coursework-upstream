from graph import *
from wordgraphs import *

def test_task1_is_word_1() -> None:
    g = RealWordsGraph("web2", 4)
    assert g.is_word("code")

def test_task1_is_word_2() -> None:
    g = RealWordsGraph("web2", 4)
    assert g.is_word("abe")

def test_task1_is_word_3() -> None:
    g = RealWordsGraph("web2", 4)
    assert g.is_word("done")

def test_task1_is_not_word_1() -> None:
    g = RealWordsGraph("web2", 4)
    assert not g.is_word("abcd")

def test_task1_is_not_word_2() -> None:
    g = RealWordsGraph("web2", 4)
    assert not g.is_word("Abe")

def test_task1_is_not_word_3() -> None:
    g = RealWordsGraph("web2", 4)
    assert not g.is_word("field")

def test_task1_adjacent_1() -> None:
    g = RealWordsGraph("web2", 4)
    actual = g.adjacent("code")
    expected = {'bode', 'cade', 'cede', 'coda', 'codo', 'coke', 'cole', 'come',
                'cone', 'cope', 'core', 'cote', 'coue', 'cove', 'coze', 'dode',
                'gode', 'lode', 'mode', 'node', 'rode', 'tode', 'wode'}
    assert actual == expected

def test_task1_adjacent_2() -> None:
    g = RealWordsGraph("web2", 4)
    actual = g.adjacent("abcd")
    expected: set[str] = set()
    assert actual == expected

def test_task1_adjacent_3() -> None:
    g = RealWordsGraph("web2", 4)
    actual = g.adjacent("part")
    expected = {'palt', 'mart', 'pact', 'pert', 'park', 'dart', 'pari', 'paut',
                'parr', 'hart', 'past', 'pare', 'tart', 'bart', 'cart', 'pant',
                'port', 'para', 'sart', 'wart', 'pard'}
    assert actual == expected

def test_task1_degree_1() -> None:
    g = RealWordsGraph("web2", 4)
    assert g.degree("code") == 23

def test_task1_degree_2() -> None:
    g = RealWordsGraph("web2", 4)
    assert g.degree("abcd") == 0

def test_task1_degree_3() -> None:
    g = RealWordsGraph("web2", 4)
    assert g.degree("part") == 21

def test_task3_1() -> None:
    g = RealWordsGraph("web2", 4)
    actual = shortest_word_path(g, "long", "path")
    allowable = [['long', 'lone', 'lote', 'pote', 'pate', 'path'],
                 ['long', 'lone', 'lote', 'late', 'lath', 'path'],
                 ['long', 'lone', 'lote', 'late', 'pate', 'path'],
                 ['long', 'lone', 'lane', 'pane', 'pate', 'path'],
                 ['long', 'lone', 'lane', 'late', 'lath', 'path'],
                 ['long', 'lone', 'lane', 'late', 'pate', 'path'],
                 ['long', 'lone', 'pone', 'pote', 'pate', 'path'],
                 ['long', 'lone', 'pone', 'pane', 'pate', 'path'],
                 ['long', 'pong', 'pone', 'pote', 'pate', 'path'],
                 ['long', 'pong', 'pone', 'pane', 'pate', 'path'],
                 ['long', 'pong', 'pang', 'pane', 'pate', 'path'],
                 ['long', 'tong', 'tang', 'tanh', 'tath', 'path']]
                
    assert actual in allowable

def test_task3_2() -> None:
    g = RealWordsGraph("web2", 4)
    actual = shortest_word_path(g, "hide", "hare")
    allowable = [['hide', 'hade', 'hare'],
                 ['hide', 'hire', 'hare']]
                
    assert actual in allowable

def test_task3_3() -> None:
    g = RealWordsGraph("web2", 4)
    actual = shortest_word_path(g, "food", "gone")
    allowable = [['food', 'fond', 'gond', 'gone'],
                 ['food', 'good', 'gond', 'gone']]
                
    assert actual in allowable

def test_task4c_is_word_1() -> None:
    g = RealWordsLazyGraph("web2")
    assert g.is_word("parsimonious")

def test_task4c_is_word_2() -> None:
    g = RealWordsLazyGraph("web2")
    assert g.is_word("america")

def test_task4c_is_word_3() -> None:
    g = RealWordsLazyGraph("web2")
    assert g.is_word("meticulous")

def test_task4c_is_not_word_1() -> None:
    g = RealWordsLazyGraph("web2")
    assert not g.is_word("abcd")

def test_task4c_is_not_word_2() -> None:
    g = RealWordsLazyGraph("web2")
    assert not g.is_word("Chicago")

def test_task4c_is_not_word_3() -> None:
    g = RealWordsLazyGraph("web2")
    assert not g.is_word("miticulous")

def test_task4c_adjacent_1() -> None:
    g = RealWordsLazyGraph("web2")
    actual = g.adjacent("code")
    expected = {'bode', 'cade', 'cede', 'coda', 'codo', 'coke', 'cole', 'come',
                'cone', 'cope', 'core', 'cote', 'coue', 'cove', 'coze', 'dode',
                'gode', 'lode', 'mode', 'node', 'rode', 'tode', 'wode'}
    assert actual == expected

def test_task4c_adjacent_2() -> None:
    g = RealWordsLazyGraph("web2")
    actual = g.adjacent("abcdefghi")
    expected: set[str] = set()
    assert actual == expected

def test_task4c_adjacent_3() -> None:
    g = RealWordsLazyGraph("web2")
    actual = g.adjacent("unfailable")
    expected = {'unhailable', 'unmailable', 'unfailably', 'unvailable',
                'unbailable', 'unsailable', 'unfoilable'}
                
    assert actual == expected

def test_task4c_degree_1() -> None:
    g = RealWordsLazyGraph("web2")
    assert g.degree("code") == 23

def test_task4c_degree_2() -> None:
    g = RealWordsLazyGraph("web2")
    assert g.degree("abcdefghi") == 0

def test_task4c_degree_3() -> None:
    g = RealWordsLazyGraph("web2")
    assert g.degree("unfailable") == 7

