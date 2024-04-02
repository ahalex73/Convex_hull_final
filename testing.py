from graham_scan import *
from jarvis_march import *
# from monotone_chain import * 


def parse_eclipse_text_file():
    """ Gather the points of the eclipse data"""



def test_sqaure():
    known_square_convex_hull = {[0,0],[0,4],[4,4],[4,0]}

    assert find_convex_hull({[0,0],[0,4],[1,1],[2,1],[3,1],[1,2],[2,2],[3,2],[1,3],[2,3],[3,3],[4,4],[4,0]}) == known_square_convex_hull    # Graham scan
    #assert test_jarvis_march({[0,0],[0,4],[1,1],[2,1],[3,1],[1,2],[2,2],[3,2],[1,3],[2,3],[3,3],[4,4],[4,0]}) == known_square_convex_hull  # Jarvis March
    #assert andrew_scan({[0,0],[0,4],[1,1],[2,1],[3,1],[1,2],[2,2],[3,2],[1,3],[2,3],[3,3],[4,4],[4,0]}) == known_square_convex_hull        # Andrew Monotone-Chain



def test_circle():
    known_circle_convex_hull = {}


def test_eclipse():

    