import pytest
import json

from graph import GridGraph
from task1 import validate_grid_graph
from task2 import get_path_distance
from task3 import shortest_paths, trace_path


DATA_DIR = "data/"

@pytest.mark.parametrize("file_prefix ,expected",
    [("simple_2x2", True),
     ("simple_2x3", True),
     ("simple_3x2", True),
     ("simple_3x4", True),
     ("invalid_2x2", False),
     ("invalid_2x3", False),
     ("random_5x5", True)
     ]
)
def test_task1_valid(file_prefix: str, expected:bool) -> None:
    """Run a single test for each graph file to check if it's valid or not"""
    g = GridGraph()
    g.load_graph(f"{DATA_DIR}/{file_prefix}.json")
    assert validate_grid_graph(g) == expected
    

def test_task1_empty() -> None:
    """Verify that an empty Grid Graph is not a valid graph"""
    assert validate_grid_graph(GridGraph()) == False


@pytest.mark.parametrize("file_prefix, path, expected",
                         [
                          ('simple_2x2', 'ACDB', 18),
                          ('simple_2x2', 'ADBC', 14),
                          ('simple_2x3', 'AEBD', 6),
                          ('simple_3x4', 'ABCDHGFEIJKL', 57),
                          ('simple_3x4', 'ABFL', None),
                          ('random_5x5', 'EQVDUWFKZ', None),
                          ('random_5x5', 'EQVDUWFKPZ', 366)
                         ])
def test_task2_paths(file_prefix: str, path: str, expected: int) -> None:
    g = GridGraph()
    g.load_graph(f"{DATA_DIR}/{file_prefix}.json")
    assert get_path_distance(g, path)  == expected


@pytest.mark.parametrize("file_prefix, src_vertex",
                         [('simple_2x2', 'A'),
                          ('simple_2x3', 'A'),
                          ('simple_3x2', 'A'),
                          ('simple_3x4', 'A'),
                          ('random_5x5', 'W')]
                        )
def test_task3_shortest_paths(file_prefix: str, src_vertex: str) -> None:
    g = GridGraph()
    g.load_graph(f"{DATA_DIR}/{file_prefix}.json")
    with open(f"{DATA_DIR}/distances/{file_prefix}_sp_{src_vertex}.json") as fp:
        sp_dict = {k: tuple(v) for k,v in json.load(fp).items()}

    assert shortest_paths(g, src_vertex) == sp_dict


@pytest.mark.parametrize("file_prefix, src_vertex, dst_vertex, expected",
                         [('simple_2x2', 'A' , 'B', ('AB', 4)),
                          ('simple_2x3', 'A', 'F', ('AEF', 9)),
                          ('simple_3x2', 'A', 'F', ('ACF', 12)),
                          ('simple_3x4', 'A', 'L', ('ABGL', 7)),
                          ('random_5x5', 'W', 'Z', ('WFPZ', 68)),
                          ('random_5x5', 'W', 'E', ('WRQE', 18))
                         ]
)
def test_task3_trace(file_prefix: str, src_vertex: str, dst_vertex: str, expected: tuple[str, int]) -> None:
    g = GridGraph()
    g.load_graph(f"{DATA_DIR}/{file_prefix}.json")
    with open(f"{DATA_DIR}/distances/{file_prefix}_sp_{src_vertex}.json") as fp:
        sp_dict = {k: tuple(v) for k,v in json.load(fp).items()}

    sp_actual = shortest_paths(g, src_vertex)
    assert sp_actual == sp_dict

    assert trace_path(sp_actual, dst_vertex) == expected
