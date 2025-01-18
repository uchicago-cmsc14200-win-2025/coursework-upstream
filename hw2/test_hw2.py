import pytest
from task1 import *
from task3 import *
from trees import *

def test_task1_1() -> None:
    m = Matrix(3, 3)
    
    for r in range(3):
        for c in range(3):
            assert m.in_bounds((r, c))
            assert m.get((r, c)) == 0
        
    assert not m.in_bounds((-1, 0))
    assert not m.in_bounds((3, 0))
    assert not m.in_bounds((0, -1))
    assert not m.in_bounds((0, 3))
    
    with pytest.raises(IndexError):
        m.get((-1, 0))
    with pytest.raises(IndexError):
        m.get((3, 0))
    with pytest.raises(IndexError):
        m.get((0, -1))
    with pytest.raises(IndexError):
        m.get((0, 3))
        
    assert m.rows == 3
    assert m.columns == 3
    
    assert m.horiz_symm
    assert m.vert_symm
    assert m.maj_diag_symm

def test_task1_2() -> None:
    m = Matrix(4, 4)
    
    for r in range(4):
        for c in range(4):
            assert m.in_bounds((r, c))
            assert m.get((r, c)) == 0
        
    assert not m.in_bounds((-1, 0))
    assert not m.in_bounds((4, 0))
    assert not m.in_bounds((0, -1))
    assert not m.in_bounds((0, 4))
    
    with pytest.raises(IndexError):
        m.get((-1, 0))
    with pytest.raises(IndexError):
        m.get((4, 0))
    with pytest.raises(IndexError):
        m.get((0, -1))
    with pytest.raises(IndexError):
        m.get((0, 4))
    
    assert m.rows == 4
    assert m.columns == 4
    
    assert m.horiz_symm
    assert m.vert_symm
    assert m.maj_diag_symm

def test_task1_3() -> None:
    m = Matrix(4, 7)
    
    for r in range(4):
        for c in range(7):
            assert m.in_bounds((r, c))
            assert m.get((r, c)) == 0
        
    assert not m.in_bounds((-1, 0))
    assert not m.in_bounds((4, 0))
    assert not m.in_bounds((0, -1))
    assert not m.in_bounds((0, 7))
    
    with pytest.raises(IndexError):
        m.get((-1, 0))
    with pytest.raises(IndexError):
        m.get((4, 0))
    with pytest.raises(IndexError):
        m.get((0, -1))
    with pytest.raises(IndexError):
        m.get((0, 7))
    
    assert m.rows == 4
    assert m.columns == 7
    
    assert m.horiz_symm
    assert m.vert_symm
    assert not m.maj_diag_symm

def test_task1_4() -> None:
    l = [[1,  2,  3,  4],
         [5,  6,  7,  8],
         [9, 10, 11, 12]]
    m = Matrix(len(l), len(l[0]))
    
    for r in range(len(l)):
        for c in range(len(l[0])):
            m.set((r, c), l[r][c])
    
    for r in range(len(l)):
        for c in range(len(l[0])):
            assert m.get((r, c)) == l[r][c]
        
    assert m.rows == len(l)
    assert m.columns == len(l[0])
        
    assert not m.horiz_symm
    assert not m.vert_symm
    assert not m.maj_diag_symm

def test_task1_5() -> None:
    l = [[1,  2,  3,  4],
         [5,  6,  7,  8],
         [1,  2,  3,  4]]
    m = Matrix(len(l), len(l[0]))
    
    for r in range(len(l)):
        for c in range(len(l[0])):
            m.set((r, c), l[r][c])
    
    for r in range(len(l)):
        for c in range(len(l[0])):
            assert m.get((r, c)) == l[r][c]
        
    assert m.rows == len(l)
    assert m.columns == len(l[0])
        
    assert m.horiz_symm
    assert not m.vert_symm
    assert not m.maj_diag_symm

def test_task1_6() -> None:
    l = [[ 1,  2,  3,  4],
         [ 5,  6,  7,  8],
         [ 9, 10, 11, 12],
         [13, 14, 15, 16]]
    m = Matrix(len(l), len(l[0]))
    
    for r in range(len(l)):
        for c in range(len(l[0])):
            m.set((r, c), l[r][c])
    
    for r in range(len(l)):
        for c in range(len(l[0])):
            assert m.get((r, c)) == l[r][c]
        
    assert m.rows == len(l)
    assert m.columns == len(l[0])
        
    assert not m.horiz_symm
    assert not m.vert_symm
    assert not m.maj_diag_symm

def test_task1_7() -> None:
    l = [[1,  2,  3,  4],
         [5,  6,  7,  8],
         [5,  6,  7,  8],
         [1,  2,  3,  4]]
    m = Matrix(len(l), len(l[0]))
    
    for r in range(len(l)):
        for c in range(len(l[0])):
            m.set((r, c), l[r][c])
    
    for r in range(len(l)):
        for c in range(len(l[0])):
            assert m.get((r, c)) == l[r][c]
        
    assert m.rows == len(l)
    assert m.columns == len(l[0])
        
    assert m.horiz_symm
    assert not m.vert_symm
    assert not m.maj_diag_symm

def test_task1_8() -> None:
    l = [[ 1,  2,  3,  4,  3,  2,  1],
         [ 8,  9, 10, 11, 10,  9,  8],
         [16, 17, 18, 19, 18, 17, 16]]
    m = Matrix(len(l), len(l[0]))
    
    for r in range(len(l)):
        for c in range(len(l[0])):
            m.set((r, c), l[r][c])
    
    for r in range(len(l)):
        for c in range(len(l[0])):
            assert m.get((r, c)) == l[r][c]
        
    assert m.rows == len(l)
    assert m.columns == len(l[0])
        
    assert not m.horiz_symm
    assert m.vert_symm
    assert not m.maj_diag_symm

def test_task1_9() -> None:
    l = [[ 1,  2,  3,  3,  2,  1],
         [ 8,  9, 10, 10,  9,  8],
         [16, 17, 18, 18, 17, 16]]
    m = Matrix(len(l), len(l[0]))
    
    for r in range(len(l)):
        for c in range(len(l[0])):
            m.set((r, c), l[r][c])
    
    for r in range(len(l)):
        for c in range(len(l[0])):
            assert m.get((r, c)) == l[r][c]
        
    assert m.rows == len(l)
    assert m.columns == len(l[0])
        
    assert not m.horiz_symm
    assert m.vert_symm
    assert not m.maj_diag_symm

def test_task1_10() -> None:
    l = [[ 1,  2,  3,  4,  5],
         [ 2,  6,  7,  8,  9],
         [ 3,  7, 10, 11, 12],
         [ 4,  8, 11, 13, 14],
         [ 5,  9, 12, 14, 15]]
    m = Matrix(len(l), len(l[0]))
    
    for r in range(len(l)):
        for c in range(len(l[0])):
            m.set((r, c), l[r][c])
    
    for r in range(len(l)):
        for c in range(len(l[0])):
            assert m.get((r, c)) == l[r][c]
        
    assert m.rows == len(l)
    assert m.columns == len(l[0])
        
    assert not m.horiz_symm
    assert not m.vert_symm
    assert m.maj_diag_symm

def test_task1_11() -> None:
    l = [[ 1,  2,  3,  4],
         [ 2,  6,  7,  8],
         [ 3,  7, 10, 11],
         [ 4,  8, 11, 13]]
    m = Matrix(len(l), len(l[0]))
    
    for r in range(len(l)):
        for c in range(len(l[0])):
            m.set((r, c), l[r][c])
    
    for r in range(len(l)):
        for c in range(len(l[0])):
            assert m.get((r, c)) == l[r][c]
        
    assert m.rows == len(l)
    assert m.columns == len(l[0])
        
    assert not m.horiz_symm
    assert not m.vert_symm
    assert m.maj_diag_symm


def test_task3_1() -> None:
    c = RGBConstant((10, 20, 30))
    assert c.is_const()
    assert c.num_nodes() == 1
    assert c.eval() == (10, 20, 30)
    assert str(c) == "Color(10, 20, 30)"

def test_task3_2() -> None:
    c1 = RGBConstant((100, 50, 7))
    c2 = RGBConstant((200, 10, 2))
    op = Blend(c1, c2)
    assert not op.is_const()
    assert op.num_nodes() == 3
    assert op.eval() == (150, 30, 4)
    assert str(op) == "Blend(Color(100, 50, 7), Color(200, 10, 2))"

def test_task3_3() -> None:
    c1 = RGBConstant((10, 20, 30))
    c2 = RGBConstant((40, 50, 60))
    c3 = RGBConstant((70, 80, 90))
    op = Blend(c1, Blend(c2, c3))
    assert not op.is_const()
    assert op.num_nodes() == 5
    assert op.eval() == (32, 42, 52)
    assert str(op) == "Blend(Color(10, 20, 30), Blend(Color(40, 50, 60), " + \
                      "Color(70, 80, 90)))"

def test_task3_4() -> None:
    c = RGBConstant((100, 150, 255))
    op = Invert(c)
    assert not op.is_const()
    assert op.num_nodes() == 2
    assert op.eval() == (155, 105, 0)
    assert str(op) == "Invert(Color(100, 150, 255))"

def test_task3_5() -> None:
    c1 = RGBConstant((10, 20, 30))
    c2 = RGBConstant((30, 20, 10))
    op = ChooseBrighter(c1, c2)
    assert not op.is_const()
    assert op.num_nodes() == 3
    assert op.eval() == (30, 20, 10)
    assert str(op) == "ChooseBrighter(Color(10, 20, 30), Color(30, 20, 10))"

def test_task3_6() -> None:
    c1 = RGBConstant((30, 20, 10))
    c2 = RGBConstant((10, 20, 30))
    op = ChooseBrighter(c1, c2)
    assert not op.is_const()
    assert op.num_nodes() == 3
    assert op.eval() == (30, 20, 10)
    assert str(op) == "ChooseBrighter(Color(30, 20, 10), Color(10, 20, 30))"

def test_task3_7() -> None:
    red = RGBConstant((255, 0, 0))
    green = RGBConstant((0, 255, 0))
    blend = Blend(red, green)
    blue = RGBConstant((0, 0, 255))
    bright = ChooseBrighter(blend, blue)
    invert = Invert(bright)
    
    assert invert.eval() == (128, 128, 255)
    assert str(invert) == "Invert(ChooseBrighter(Blend(Color(255, 0, 0), " + \
                          "Color(0, 255, 0)), Color(0, 0, 255)))"

