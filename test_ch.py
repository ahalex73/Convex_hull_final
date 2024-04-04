from graham_scan import *
from jarvis_march import *
from monotone_chain import * 
import pytest

def test_square():
    """Test if the convex hull of a square is computed correctly"""
    input_points = [(0,0),(0,4),(1,1),(2,1),(3,1),(1,2),(2,2),(3,2),(1,3),(2,3),(3,3),(4,4),(4,0)]
    known_square_convex_hull = [(0,0),(0,4),(4,4),(4,0),(0,0)] 
    
    graham_scan_result = find_convex_hull(input_points)
    #jarvis_march_result = jarvis_march_convex_hull(input_points)
    monotone_chain_result = monotone_chain(input_points)


    assert sorted(graham_scan_result) == sorted(known_square_convex_hull)
    #assert sorted(jarvis_march_result) == sorted(known_square_convex_hull)
    assert sorted(monotone_chain_result) == sorted(known_square_convex_hull)


# def test_square():
#     """ Test Convex Hull against Square"""
#     known_square_convex_hull = ((0,0),(0,4),(4,4),(4,0))
#     print(type(known_square_convex_hull))

#     result = find_convex_hull((0,0),(0,4),(1,1),(2,1),(3,1),(1,2),(2,2),(3,2),(1,3),(2,3),(3,3),(4,4),(4,0))
#     result = tuple(result)
#     print(type(result))

#     assert result == known_square_convex_hull
    
    # Graham scan
    #assert test_jarvis_march({(0,0),(0,4),(1,1),(2,1),(3,1),(1,2),(2,2),(3,2),(1,3),(2,3),(3,3),(4,4),(4,0))) == known_square_convex_hull  # Jarvis March
    #assert andrew_scan({(0,0),(0,4),(1,1),(2,1),(3,1),(1,2),(2,2),(3,2),(1,3),(2,3),(3,3),(4,4),(4,0))) == known_square_convex_hull        # Andrew Monotone-Chain



# def test_circle():
#     """ Test Convex hull against circle"""
#     known_circle_convex_hull = {}


# def test_eclipse():
#     """ Test convex hulls against an eclipse """
#     # Known convex hull of eclipse of 200 points - should just rank based off the -x -> +x space
#     known_eclipse = ((-0.447027, 0.434093), (-0.44663, 0.423787), (-0.44507, 0.40134), (-0.44497, 0.400227), (-0.444031, 0.390771),
#                     (-0.442417, 0.377094), (-0.440513, 0.363387), (-0.439449, 0.356473), (-0.43935, 0.355852), (-0.430483, 0.309305),
#                     (-0.416993, 0.255385), (-0.411568, 0.236606), (-0.409448, 0.229581), (-0.398604, 0.195836), (-0.389703, 0.170314),
#                     (-0.386223, 0.160763), (-0.368531, 0.115183), (-0.33343, 0.0353953), (-0.302844, -0.0262229), (-0.298749, -0.03404),
#                     (-0.294789, -0.0415137), (-0.294014, -0.042967), (-0.293888, -0.043202), (-0.244142, -0.13055), (-0.217054, -0.173955),
#                     (-0.211227, -0.18296), (-0.205689, -0.191415), (-0.195165, -0.207216), (-0.182942, -0.225142), (-0.165592, -0.249835),
#                     (-0.159419, -0.258416), (-0.153732, -0.266228), (-0.150469, -0.270672), (-0.149814, -0.27156), (-0.148661, -0.273121),
#                     (-0.144359, -0.278914), (-0.132329, -0.294858), (-0.117309, -0.314244), (-0.101911, -0.333536), (-0.0527011, -0.391396),
#                     (-0.0391724, -0.406322), (-0.0312701, -0.414849), (-0.0234989, -0.423097), (0.0228529, -0.469482), (0.0458289, -0.490688), (0.079156, -0.519309), (0.090717, -0.528633), (0.0914685, -0.529228), (0.0963835, -0.533087), (0.103443, -0.538529), (0.106484, -0.540835), (0.11372, -0.546233), (0.127032, -0.555824), (0.127933, -0.556458), (0.130393, -0.558175), (0.140931, -0.565358), (0.195985, -0.597968), (0.211212, -0.605407), (0.211658, -0.605613), (0.228336, -0.612865), (0.229553, -0.613357), (0.233258, -0.614821), (0.246924, -0.619789), (0.252701, -0.621675), (0.257757, -0.623218), (0.260667, -0.624057), (0.266909, -0.62574), (0.327497, -0.632039), (0.332302, -0.631593), (0.358123, -0.625981), (0.359229, -0.625602), (0.359352, -0.625559), (0.359394, -0.625544), (0.371568, -0.62044), (0.384419, -0.612941), (0.393548, -0.605962), (0.402166, -0.597774), (0.403408, -0.596442), (0.404525, -0.595206), (0.407435, -0.591817), (0.409209, -0.58962), (0.420336, -0.573036), (0.426359, -0.561332), (0.427154, -0.55959), (0.439037, -0.524164), (0.444145, -0.496441), (0.444619, -0.49272), (0.445141, -0.48815), (0.445552, -0.484069), (0.445828, -0.481009), (0.446452, -0.472543), (0.446848, -0.464934), (0.446925, -0.430854), (0.446804, -0.427668), (0.446545, -0.422099), (0.446404, -0.419515), (0.446131, -0.415033), (0.443047, -0.382145), (0.442565, -0.378252), (0.439235, -0.355133), (0.434396, -0.328096), (0.432744, -0.319905), (0.432421, -0.318349), (0.430886, -0.311146), (0.429439, -0.304611), (0.413466, -0.243039), (0.410211, -0.232091), (0.397663, -0.193056), (0.397301, -0.191991), (0.390118, -0.171467), (0.388949, -0.168227), (0.387895, -0.165326), (0.385229, -0.158077), (0.381446, -0.147997), (0.380234, -0.144816), (0.379505, -0.142912), (0.375726, -0.133176), (0.373927, -0.128613), (0.369632, -0.117893), (0.364773, -0.106044), (0.357251, -0.0882301), (0.355106, -0.083262), (0.350675, -0.0731386), (0.339687, -0.048805), (0.309691, 0.0129413), (0.286576, 0.0567512), (0.285258, 0.0591654), (0.279369, 0.0698488), (0.264068, 0.0968581), (0.25838, 0.106641), (0.246856, 0.126054), (0.238412, 0.139953), (0.180832, 0.228192), (0.169555, 0.24427), (0.156501, 0.262434), (0.149644, 0.27179), (0.131512, 0.295928), (0.113976, 0.31847), (0.0769624, 0.363579), (0.0539863, 0.389957), (0.00682875, 0.440333), (-0.0085661, 0.455698), (-0.00885851, 0.455984), (-0.025573, 0.472055), (-0.0452272, 0.490148), (-0.0879029, 0.526392), (-0.102256, 0.537622), (-0.106044, 0.540503), (-0.109041, 0.542757), (-0.109266, 0.542926), (-0.113695, 0.546215), (-0.143689, 0.56719), (-0.144809, 0.567929), (-0.165513, 0.580971), (-0.190197, 0.59495), (-0.220005, 0.60936), (-0.227176, 0.612391), (-0.241817, 0.618015), (-0.243657, 0.618665), (-0.267173, 0.625807), (-0.294316, 0.631033), (-0.29572, 0.631204), (-0.298069, 0.631468), (-0.312472, 0.632411), (-0.324299, 0.632244), (-0.33071, 0.63176), (-0.333439, 0.631463), (-0.351227, 0.628066), (-0.365732, 0.623104), (-0.376399, 0.617902), (-0.37941, 0.616155), (-0.383971, 0.613244), (-0.386024, 0.611823), (-0.389275, 0.609422), (-0.397739, 0.602199), (-0.397887, 0.602058), (-0.399005, 0.600983), (-0.400226, 0.599773), (-0.40727, 0.592016), (-0.410789, 0.587572), (-0.411599, 0.586488), (-0.41609, 0.580008), (-0.41665, 0.57914), (-0.418485, 0.576189), (-0.423296, 0.56759), (-0.423366, 0.567454), (-0.427773, 0.558197), (-0.428478, 0.556566), (-0.43829, 0.527183), (-0.438307, 0.527115), (-0.439658, 0.521518), (-0.439999, 0.520005), (-0.442858, 0.50512), (-0.443699, 0.499658), (-0.443902, 0.498227), (-0.44395, 0.497878), (-0.445203, 0.487558), (-0.445637, 0.483152), (-0.447027, 0.434093))
