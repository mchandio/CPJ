# Generated from grammar/CPJ.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,52,430,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,1,0,1,0,5,
        0,81,8,0,10,0,12,0,84,9,0,1,0,1,0,1,1,1,1,1,1,3,1,91,8,1,1,2,1,2,
        1,2,1,2,3,2,97,8,2,1,2,1,2,1,2,1,2,1,2,3,2,104,8,2,1,3,1,3,1,3,5,
        3,109,8,3,10,3,12,3,112,9,3,1,4,1,4,5,4,116,8,4,10,4,12,4,119,9,
        4,1,4,4,4,122,8,4,11,4,12,4,123,1,4,1,4,1,4,3,4,129,8,4,1,5,1,5,
        1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,4,7,142,8,7,11,7,12,7,143,1,
        7,1,7,1,7,1,7,1,7,5,7,151,8,7,10,7,12,7,154,9,7,1,7,1,7,4,7,158,
        8,7,11,7,12,7,159,1,7,1,7,1,7,5,7,165,8,7,10,7,12,7,168,9,7,3,7,
        170,8,7,1,8,1,8,1,8,1,8,1,8,1,8,3,8,178,8,8,1,8,4,8,181,8,8,11,8,
        12,8,182,3,8,185,8,8,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,3,10,195,
        8,10,1,11,1,11,1,11,1,11,1,11,1,11,4,11,203,8,11,11,11,12,11,204,
        1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,5,12,217,8,12,
        10,12,12,12,220,9,12,1,12,4,12,223,8,12,11,12,12,12,224,1,12,1,12,
        1,12,1,12,3,12,231,8,12,1,13,1,13,1,13,5,13,236,8,13,10,13,12,13,
        239,9,13,1,13,3,13,242,8,13,1,14,1,14,3,14,246,8,14,1,14,1,14,1,
        15,1,15,1,15,1,15,1,16,1,16,1,16,3,16,257,8,16,1,16,1,16,1,16,1,
        16,3,16,263,8,16,1,16,1,16,1,16,1,16,3,16,269,8,16,1,16,1,16,1,16,
        1,16,3,16,275,8,16,1,16,3,16,278,8,16,1,17,1,17,1,17,5,17,283,8,
        17,10,17,12,17,286,9,17,1,18,1,18,3,18,290,8,18,1,19,1,19,1,20,1,
        20,1,21,1,21,1,22,1,22,1,22,5,22,301,8,22,10,22,12,22,304,9,22,1,
        23,1,23,1,23,5,23,309,8,23,10,23,12,23,312,9,23,1,24,1,24,1,24,5,
        24,317,8,24,10,24,12,24,320,9,24,1,25,1,25,1,25,5,25,325,8,25,10,
        25,12,25,328,9,25,1,26,1,26,1,26,5,26,333,8,26,10,26,12,26,336,9,
        26,1,27,1,27,1,27,5,27,341,8,27,10,27,12,27,344,9,27,1,28,1,28,1,
        28,5,28,349,8,28,10,28,12,28,352,9,28,1,29,1,29,1,29,5,29,357,8,
        29,10,29,12,29,360,9,29,1,30,1,30,1,30,5,30,365,8,30,10,30,12,30,
        368,9,30,1,31,1,31,1,31,5,31,373,8,31,10,31,12,31,376,9,31,1,32,
        1,32,1,32,3,32,381,8,32,1,33,1,33,1,33,3,33,386,8,33,1,34,1,34,1,
        34,1,34,1,34,1,34,1,34,1,34,3,34,396,8,34,1,34,3,34,399,8,34,3,34,
        401,8,34,1,35,1,35,1,35,5,35,406,8,35,10,35,12,35,409,9,35,1,36,
        1,36,1,36,3,36,414,8,36,1,36,1,36,3,36,418,8,36,1,37,1,37,1,37,5,
        37,423,8,37,10,37,12,37,426,9,37,1,38,1,38,1,38,0,0,39,0,2,4,6,8,
        10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,
        54,56,58,60,62,64,66,68,70,72,74,76,0,9,1,0,49,50,1,0,25,26,2,0,
        21,24,42,43,1,0,27,28,1,0,14,15,1,0,16,18,2,0,14,15,20,20,1,0,4,
        6,1,0,44,49,450,0,82,1,0,0,0,2,90,1,0,0,0,4,92,1,0,0,0,6,105,1,0,
        0,0,8,128,1,0,0,0,10,130,1,0,0,0,12,132,1,0,0,0,14,169,1,0,0,0,16,
        184,1,0,0,0,18,186,1,0,0,0,20,191,1,0,0,0,22,202,1,0,0,0,24,208,
        1,0,0,0,26,232,1,0,0,0,28,243,1,0,0,0,30,249,1,0,0,0,32,277,1,0,
        0,0,34,279,1,0,0,0,36,289,1,0,0,0,38,291,1,0,0,0,40,293,1,0,0,0,
        42,295,1,0,0,0,44,297,1,0,0,0,46,305,1,0,0,0,48,313,1,0,0,0,50,321,
        1,0,0,0,52,329,1,0,0,0,54,337,1,0,0,0,56,345,1,0,0,0,58,353,1,0,
        0,0,60,361,1,0,0,0,62,369,1,0,0,0,64,380,1,0,0,0,66,382,1,0,0,0,
        68,400,1,0,0,0,70,402,1,0,0,0,72,410,1,0,0,0,74,419,1,0,0,0,76,427,
        1,0,0,0,78,81,3,2,1,0,79,81,5,4,0,0,80,78,1,0,0,0,80,79,1,0,0,0,
        81,84,1,0,0,0,82,80,1,0,0,0,82,83,1,0,0,0,83,85,1,0,0,0,84,82,1,
        0,0,0,85,86,5,0,0,1,86,1,1,0,0,0,87,91,3,14,7,0,88,91,3,4,2,0,89,
        91,3,12,6,0,90,87,1,0,0,0,90,88,1,0,0,0,90,89,1,0,0,0,91,3,1,0,0,
        0,92,93,5,32,0,0,93,94,5,50,0,0,94,96,5,7,0,0,95,97,3,6,3,0,96,95,
        1,0,0,0,96,97,1,0,0,0,97,98,1,0,0,0,98,99,5,8,0,0,99,103,5,9,0,0,
        100,101,5,4,0,0,101,104,3,8,4,0,102,104,3,8,4,0,103,100,1,0,0,0,
        103,102,1,0,0,0,104,5,1,0,0,0,105,110,5,50,0,0,106,107,5,10,0,0,
        107,109,5,50,0,0,108,106,1,0,0,0,109,112,1,0,0,0,110,108,1,0,0,0,
        110,111,1,0,0,0,111,7,1,0,0,0,112,110,1,0,0,0,113,117,5,5,0,0,114,
        116,5,4,0,0,115,114,1,0,0,0,116,119,1,0,0,0,117,115,1,0,0,0,117,
        118,1,0,0,0,118,121,1,0,0,0,119,117,1,0,0,0,120,122,3,2,1,0,121,
        120,1,0,0,0,122,123,1,0,0,0,123,121,1,0,0,0,123,124,1,0,0,0,124,
        125,1,0,0,0,125,126,5,6,0,0,126,129,1,0,0,0,127,129,3,10,5,0,128,
        113,1,0,0,0,128,127,1,0,0,0,129,9,1,0,0,0,130,131,3,12,6,0,131,11,
        1,0,0,0,132,133,3,40,20,0,133,134,5,4,0,0,134,13,1,0,0,0,135,136,
        5,34,0,0,136,137,5,50,0,0,137,138,5,9,0,0,138,139,5,4,0,0,139,141,
        5,5,0,0,140,142,3,16,8,0,141,140,1,0,0,0,142,143,1,0,0,0,143,141,
        1,0,0,0,143,144,1,0,0,0,144,145,1,0,0,0,145,146,5,6,0,0,146,170,
        1,0,0,0,147,148,5,33,0,0,148,152,5,11,0,0,149,151,5,4,0,0,150,149,
        1,0,0,0,151,154,1,0,0,0,152,150,1,0,0,0,152,153,1,0,0,0,153,155,
        1,0,0,0,154,152,1,0,0,0,155,157,5,5,0,0,156,158,3,16,8,0,157,156,
        1,0,0,0,158,159,1,0,0,0,159,157,1,0,0,0,159,160,1,0,0,0,160,161,
        1,0,0,0,161,162,5,6,0,0,162,166,5,12,0,0,163,165,5,4,0,0,164,163,
        1,0,0,0,165,168,1,0,0,0,166,164,1,0,0,0,166,167,1,0,0,0,167,170,
        1,0,0,0,168,166,1,0,0,0,169,135,1,0,0,0,169,147,1,0,0,0,170,15,1,
        0,0,0,171,185,3,20,10,0,172,185,3,32,16,0,173,185,3,72,36,0,174,
        185,3,18,9,0,175,177,3,40,20,0,176,178,5,4,0,0,177,176,1,0,0,0,177,
        178,1,0,0,0,178,185,1,0,0,0,179,181,5,4,0,0,180,179,1,0,0,0,181,
        182,1,0,0,0,182,180,1,0,0,0,182,183,1,0,0,0,183,185,1,0,0,0,184,
        171,1,0,0,0,184,172,1,0,0,0,184,173,1,0,0,0,184,174,1,0,0,0,184,
        175,1,0,0,0,184,180,1,0,0,0,185,17,1,0,0,0,186,187,5,50,0,0,187,
        188,5,9,0,0,188,189,3,40,20,0,189,190,5,4,0,0,190,19,1,0,0,0,191,
        194,5,35,0,0,192,195,3,22,11,0,193,195,3,24,12,0,194,192,1,0,0,0,
        194,193,1,0,0,0,195,21,1,0,0,0,196,197,5,50,0,0,197,198,5,9,0,0,
        198,203,5,50,0,0,199,200,5,50,0,0,200,201,5,1,0,0,201,203,5,50,0,
        0,202,196,1,0,0,0,202,199,1,0,0,0,203,204,1,0,0,0,204,202,1,0,0,
        0,204,205,1,0,0,0,205,206,1,0,0,0,206,207,5,4,0,0,207,23,1,0,0,0,
        208,230,5,11,0,0,209,210,3,26,13,0,210,211,5,12,0,0,211,212,5,4,
        0,0,212,231,1,0,0,0,213,214,5,4,0,0,214,218,5,5,0,0,215,217,5,4,
        0,0,216,215,1,0,0,0,217,220,1,0,0,0,218,216,1,0,0,0,218,219,1,0,
        0,0,219,222,1,0,0,0,220,218,1,0,0,0,221,223,3,28,14,0,222,221,1,
        0,0,0,223,224,1,0,0,0,224,222,1,0,0,0,224,225,1,0,0,0,225,226,1,
        0,0,0,226,227,5,6,0,0,227,228,5,12,0,0,228,229,5,4,0,0,229,231,1,
        0,0,0,230,209,1,0,0,0,230,213,1,0,0,0,231,25,1,0,0,0,232,237,3,30,
        15,0,233,234,5,10,0,0,234,236,3,30,15,0,235,233,1,0,0,0,236,239,
        1,0,0,0,237,235,1,0,0,0,237,238,1,0,0,0,238,241,1,0,0,0,239,237,
        1,0,0,0,240,242,5,10,0,0,241,240,1,0,0,0,241,242,1,0,0,0,242,27,
        1,0,0,0,243,245,3,30,15,0,244,246,5,10,0,0,245,244,1,0,0,0,245,246,
        1,0,0,0,246,247,1,0,0,0,247,248,5,4,0,0,248,29,1,0,0,0,249,250,7,
        0,0,0,250,251,5,9,0,0,251,252,7,0,0,0,252,31,1,0,0,0,253,254,5,36,
        0,0,254,256,5,7,0,0,255,257,3,34,17,0,256,255,1,0,0,0,256,257,1,
        0,0,0,257,258,1,0,0,0,258,278,5,8,0,0,259,260,5,37,0,0,260,262,5,
        7,0,0,261,263,3,34,17,0,262,261,1,0,0,0,262,263,1,0,0,0,263,264,
        1,0,0,0,264,278,5,8,0,0,265,266,5,38,0,0,266,268,5,7,0,0,267,269,
        3,34,17,0,268,267,1,0,0,0,268,269,1,0,0,0,269,270,1,0,0,0,270,278,
        5,8,0,0,271,272,5,39,0,0,272,274,5,7,0,0,273,275,3,34,17,0,274,273,
        1,0,0,0,274,275,1,0,0,0,275,276,1,0,0,0,276,278,5,8,0,0,277,253,
        1,0,0,0,277,259,1,0,0,0,277,265,1,0,0,0,277,271,1,0,0,0,278,33,1,
        0,0,0,279,284,3,36,18,0,280,281,5,10,0,0,281,283,3,36,18,0,282,280,
        1,0,0,0,283,286,1,0,0,0,284,282,1,0,0,0,284,285,1,0,0,0,285,35,1,
        0,0,0,286,284,1,0,0,0,287,290,5,49,0,0,288,290,3,40,20,0,289,287,
        1,0,0,0,289,288,1,0,0,0,290,37,1,0,0,0,291,292,3,40,20,0,292,39,
        1,0,0,0,293,294,3,42,21,0,294,41,1,0,0,0,295,296,3,44,22,0,296,43,
        1,0,0,0,297,302,3,46,23,0,298,299,5,2,0,0,299,301,3,46,23,0,300,
        298,1,0,0,0,301,304,1,0,0,0,302,300,1,0,0,0,302,303,1,0,0,0,303,
        45,1,0,0,0,304,302,1,0,0,0,305,310,3,48,24,0,306,307,5,3,0,0,307,
        309,3,48,24,0,308,306,1,0,0,0,309,312,1,0,0,0,310,308,1,0,0,0,310,
        311,1,0,0,0,311,47,1,0,0,0,312,310,1,0,0,0,313,318,3,50,25,0,314,
        315,7,1,0,0,315,317,3,50,25,0,316,314,1,0,0,0,317,320,1,0,0,0,318,
        316,1,0,0,0,318,319,1,0,0,0,319,49,1,0,0,0,320,318,1,0,0,0,321,326,
        3,52,26,0,322,323,7,2,0,0,323,325,3,52,26,0,324,322,1,0,0,0,325,
        328,1,0,0,0,326,324,1,0,0,0,326,327,1,0,0,0,327,51,1,0,0,0,328,326,
        1,0,0,0,329,334,3,54,27,0,330,331,5,29,0,0,331,333,3,54,27,0,332,
        330,1,0,0,0,333,336,1,0,0,0,334,332,1,0,0,0,334,335,1,0,0,0,335,
        53,1,0,0,0,336,334,1,0,0,0,337,342,3,56,28,0,338,339,5,30,0,0,339,
        341,3,56,28,0,340,338,1,0,0,0,341,344,1,0,0,0,342,340,1,0,0,0,342,
        343,1,0,0,0,343,55,1,0,0,0,344,342,1,0,0,0,345,350,3,58,29,0,346,
        347,5,31,0,0,347,349,3,58,29,0,348,346,1,0,0,0,349,352,1,0,0,0,350,
        348,1,0,0,0,350,351,1,0,0,0,351,57,1,0,0,0,352,350,1,0,0,0,353,358,
        3,60,30,0,354,355,7,3,0,0,355,357,3,60,30,0,356,354,1,0,0,0,357,
        360,1,0,0,0,358,356,1,0,0,0,358,359,1,0,0,0,359,59,1,0,0,0,360,358,
        1,0,0,0,361,366,3,62,31,0,362,363,7,4,0,0,363,365,3,62,31,0,364,
        362,1,0,0,0,365,368,1,0,0,0,366,364,1,0,0,0,366,367,1,0,0,0,367,
        61,1,0,0,0,368,366,1,0,0,0,369,374,3,64,32,0,370,371,7,5,0,0,371,
        373,3,64,32,0,372,370,1,0,0,0,373,376,1,0,0,0,374,372,1,0,0,0,374,
        375,1,0,0,0,375,63,1,0,0,0,376,374,1,0,0,0,377,378,7,6,0,0,378,381,
        3,64,32,0,379,381,3,66,33,0,380,377,1,0,0,0,380,379,1,0,0,0,381,
        65,1,0,0,0,382,385,3,68,34,0,383,384,5,19,0,0,384,386,3,64,32,0,
        385,383,1,0,0,0,385,386,1,0,0,0,386,67,1,0,0,0,387,388,5,7,0,0,388,
        389,3,40,20,0,389,390,5,8,0,0,390,401,1,0,0,0,391,401,3,76,38,0,
        392,398,3,74,37,0,393,395,5,7,0,0,394,396,3,70,35,0,395,394,1,0,
        0,0,395,396,1,0,0,0,396,397,1,0,0,0,397,399,5,8,0,0,398,393,1,0,
        0,0,398,399,1,0,0,0,399,401,1,0,0,0,400,387,1,0,0,0,400,391,1,0,
        0,0,400,392,1,0,0,0,401,69,1,0,0,0,402,407,3,40,20,0,403,404,5,10,
        0,0,404,406,3,40,20,0,405,403,1,0,0,0,406,409,1,0,0,0,407,405,1,
        0,0,0,407,408,1,0,0,0,408,71,1,0,0,0,409,407,1,0,0,0,410,411,3,74,
        37,0,411,413,5,7,0,0,412,414,3,70,35,0,413,412,1,0,0,0,413,414,1,
        0,0,0,414,415,1,0,0,0,415,417,5,8,0,0,416,418,7,7,0,0,417,416,1,
        0,0,0,417,418,1,0,0,0,418,73,1,0,0,0,419,424,5,50,0,0,420,421,5,
        13,0,0,421,423,5,50,0,0,422,420,1,0,0,0,423,426,1,0,0,0,424,422,
        1,0,0,0,424,425,1,0,0,0,425,75,1,0,0,0,426,424,1,0,0,0,427,428,7,
        8,0,0,428,77,1,0,0,0,52,80,82,90,96,103,110,117,123,128,143,152,
        159,166,169,177,182,184,194,202,204,218,224,230,237,241,245,256,
        262,268,274,277,284,289,302,310,318,326,334,342,350,358,366,374,
        380,385,395,398,400,407,413,417,424
    ]

class CPJParser ( Parser ):

    grammarFileName = "CPJ.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'or'", "'and'", "<INVALID>", "'<INDENT>'", 
                     "'<DEDENT>'", "'('", "')'", "':'", "','", "'{'", "'}'", 
                     "'.'", "'+'", "'-'", "'*'", "'/'", "'%'", "'**'", "'~'", 
                     "'<'", "'>'", "'<='", "'>='", "'=='", "'!='", "'<<'", 
                     "'>>'", "'|'", "'^'", "'&'", "<INVALID>", "'GUI'", 
                     "<INVALID>", "<INVALID>", "'addTextField'", "'addButton'", 
                     "'addCheckBox'", "'addSlider'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "NEWLINE", "INDENT", "DEDENT", "LPAREN", "RPAREN", 
                      "COLON", "COMMA", "LBRACE", "RBRACE", "DOT", "PLUS", 
                      "MINUS", "STAR", "DIV", "MOD", "POW", "TILDE", "LT", 
                      "GT", "LE", "GE", "EQ", "NEQ", "LSHIFT", "RSHIFT", 
                      "BITOR", "BITXOR", "BITAND", "DEF", "GUI_CAP", "GUI_KW", 
                      "TYPES_KW", "ADD_TEXT", "ADD_BTN", "ADD_CHECK", "ADD_SLIDER", 
                      "OR", "AND", "IN", "IS", "TRUE", "FALSE", "NULL", 
                      "Float", "Integer", "StringLiteral", "Identifier", 
                      "COMMENT", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_funcDef = 2
    RULE_paramList = 3
    RULE_suite = 4
    RULE_simpleStmt = 5
    RULE_exprStmt = 6
    RULE_guiBlock = 7
    RULE_guiBody = 8
    RULE_guiProp = 9
    RULE_typesLine = 10
    RULE_typesTokens = 11
    RULE_typesDict = 12
    RULE_typeEntries = 13
    RULE_typeLine = 14
    RULE_typeEntry = 15
    RULE_widgetStmt = 16
    RULE_args = 17
    RULE_arg = 18
    RULE_exprNoNewline = 19
    RULE_expression = 20
    RULE_lambdaExpr = 21
    RULE_logicalOr = 22
    RULE_logicalAnd = 23
    RULE_equality = 24
    RULE_comparison = 25
    RULE_bitwiseOr = 26
    RULE_bitwiseXor = 27
    RULE_bitwiseAnd = 28
    RULE_shift = 29
    RULE_sum = 30
    RULE_term = 31
    RULE_factor = 32
    RULE_power = 33
    RULE_atom = 34
    RULE_argList = 35
    RULE_callStmt = 36
    RULE_dottedName = 37
    RULE_literal = 38

    ruleNames =  [ "program", "statement", "funcDef", "paramList", "suite", 
                   "simpleStmt", "exprStmt", "guiBlock", "guiBody", "guiProp", 
                   "typesLine", "typesTokens", "typesDict", "typeEntries", 
                   "typeLine", "typeEntry", "widgetStmt", "args", "arg", 
                   "exprNoNewline", "expression", "lambdaExpr", "logicalOr", 
                   "logicalAnd", "equality", "comparison", "bitwiseOr", 
                   "bitwiseXor", "bitwiseAnd", "shift", "sum", "term", "factor", 
                   "power", "atom", "argList", "callStmt", "dottedName", 
                   "literal" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    NEWLINE=4
    INDENT=5
    DEDENT=6
    LPAREN=7
    RPAREN=8
    COLON=9
    COMMA=10
    LBRACE=11
    RBRACE=12
    DOT=13
    PLUS=14
    MINUS=15
    STAR=16
    DIV=17
    MOD=18
    POW=19
    TILDE=20
    LT=21
    GT=22
    LE=23
    GE=24
    EQ=25
    NEQ=26
    LSHIFT=27
    RSHIFT=28
    BITOR=29
    BITXOR=30
    BITAND=31
    DEF=32
    GUI_CAP=33
    GUI_KW=34
    TYPES_KW=35
    ADD_TEXT=36
    ADD_BTN=37
    ADD_CHECK=38
    ADD_SLIDER=39
    OR=40
    AND=41
    IN=42
    IS=43
    TRUE=44
    FALSE=45
    NULL=46
    Float=47
    Integer=48
    StringLiteral=49
    Identifier=50
    COMMENT=51
    WS=52

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(CPJParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CPJParser.StatementContext)
            else:
                return self.getTypedRuleContext(CPJParser.StatementContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(CPJParser.NEWLINE)
            else:
                return self.getToken(CPJParser.NEWLINE, i)

        def getRuleIndex(self):
            return CPJParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = CPJParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2234237693509776) != 0):
                self.state = 80
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [7, 14, 15, 20, 32, 33, 34, 44, 45, 46, 47, 48, 49, 50]:
                    self.state = 78
                    self.statement()
                    pass
                elif token in [4]:
                    self.state = 79
                    self.match(CPJParser.NEWLINE)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 84
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 85
            self.match(CPJParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def guiBlock(self):
            return self.getTypedRuleContext(CPJParser.GuiBlockContext,0)


        def funcDef(self):
            return self.getTypedRuleContext(CPJParser.FuncDefContext,0)


        def exprStmt(self):
            return self.getTypedRuleContext(CPJParser.ExprStmtContext,0)


        def getRuleIndex(self):
            return CPJParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = CPJParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 90
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [33, 34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 87
                self.guiBlock()
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 2)
                self.state = 88
                self.funcDef()
                pass
            elif token in [7, 14, 15, 20, 44, 45, 46, 47, 48, 49, 50]:
                self.enterOuterAlt(localctx, 3)
                self.state = 89
                self.exprStmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncDefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEF(self):
            return self.getToken(CPJParser.DEF, 0)

        def Identifier(self):
            return self.getToken(CPJParser.Identifier, 0)

        def LPAREN(self):
            return self.getToken(CPJParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(CPJParser.RPAREN, 0)

        def COLON(self):
            return self.getToken(CPJParser.COLON, 0)

        def NEWLINE(self):
            return self.getToken(CPJParser.NEWLINE, 0)

        def suite(self):
            return self.getTypedRuleContext(CPJParser.SuiteContext,0)


        def paramList(self):
            return self.getTypedRuleContext(CPJParser.ParamListContext,0)


        def getRuleIndex(self):
            return CPJParser.RULE_funcDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncDef" ):
                listener.enterFuncDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncDef" ):
                listener.exitFuncDef(self)




    def funcDef(self):

        localctx = CPJParser.FuncDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_funcDef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.match(CPJParser.DEF)
            self.state = 93
            self.match(CPJParser.Identifier)
            self.state = 94
            self.match(CPJParser.LPAREN)
            self.state = 96
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==50:
                self.state = 95
                self.paramList()


            self.state = 98
            self.match(CPJParser.RPAREN)
            self.state = 99
            self.match(CPJParser.COLON)
            self.state = 103
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.state = 100
                self.match(CPJParser.NEWLINE)
                self.state = 101
                self.suite()
                pass
            elif token in [5, 7, 14, 15, 20, 44, 45, 46, 47, 48, 49, 50]:
                self.state = 102
                self.suite()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self, i:int=None):
            if i is None:
                return self.getTokens(CPJParser.Identifier)
            else:
                return self.getToken(CPJParser.Identifier, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CPJParser.COMMA)
            else:
                return self.getToken(CPJParser.COMMA, i)

        def getRuleIndex(self):
            return CPJParser.RULE_paramList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParamList" ):
                listener.enterParamList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParamList" ):
                listener.exitParamList(self)




    def paramList(self):

        localctx = CPJParser.ParamListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_paramList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.match(CPJParser.Identifier)
            self.state = 110
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 106
                self.match(CPJParser.COMMA)
                self.state = 107
                self.match(CPJParser.Identifier)
                self.state = 112
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SuiteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INDENT(self):
            return self.getToken(CPJParser.INDENT, 0)

        def DEDENT(self):
            return self.getToken(CPJParser.DEDENT, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(CPJParser.NEWLINE)
            else:
                return self.getToken(CPJParser.NEWLINE, i)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CPJParser.StatementContext)
            else:
                return self.getTypedRuleContext(CPJParser.StatementContext,i)


        def simpleStmt(self):
            return self.getTypedRuleContext(CPJParser.SimpleStmtContext,0)


        def getRuleIndex(self):
            return CPJParser.RULE_suite

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSuite" ):
                listener.enterSuite(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSuite" ):
                listener.exitSuite(self)




    def suite(self):

        localctx = CPJParser.SuiteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_suite)
        self._la = 0 # Token type
        try:
            self.state = 128
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 113
                self.match(CPJParser.INDENT)
                self.state = 117
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==4:
                    self.state = 114
                    self.match(CPJParser.NEWLINE)
                    self.state = 119
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 121 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 120
                    self.statement()
                    self.state = 123 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 2234237693509760) != 0)):
                        break

                self.state = 125
                self.match(CPJParser.DEDENT)
                pass
            elif token in [7, 14, 15, 20, 44, 45, 46, 47, 48, 49, 50]:
                self.enterOuterAlt(localctx, 2)
                self.state = 127
                self.simpleStmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SimpleStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprStmt(self):
            return self.getTypedRuleContext(CPJParser.ExprStmtContext,0)


        def getRuleIndex(self):
            return CPJParser.RULE_simpleStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimpleStmt" ):
                listener.enterSimpleStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimpleStmt" ):
                listener.exitSimpleStmt(self)




    def simpleStmt(self):

        localctx = CPJParser.SimpleStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_simpleStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.exprStmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(CPJParser.ExpressionContext,0)


        def NEWLINE(self):
            return self.getToken(CPJParser.NEWLINE, 0)

        def getRuleIndex(self):
            return CPJParser.RULE_exprStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprStmt" ):
                listener.enterExprStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprStmt" ):
                listener.exitExprStmt(self)




    def exprStmt(self):

        localctx = CPJParser.ExprStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_exprStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.expression()
            self.state = 133
            self.match(CPJParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GuiBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GUI_KW(self):
            return self.getToken(CPJParser.GUI_KW, 0)

        def Identifier(self):
            return self.getToken(CPJParser.Identifier, 0)

        def COLON(self):
            return self.getToken(CPJParser.COLON, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(CPJParser.NEWLINE)
            else:
                return self.getToken(CPJParser.NEWLINE, i)

        def INDENT(self):
            return self.getToken(CPJParser.INDENT, 0)

        def DEDENT(self):
            return self.getToken(CPJParser.DEDENT, 0)

        def guiBody(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CPJParser.GuiBodyContext)
            else:
                return self.getTypedRuleContext(CPJParser.GuiBodyContext,i)


        def GUI_CAP(self):
            return self.getToken(CPJParser.GUI_CAP, 0)

        def LBRACE(self):
            return self.getToken(CPJParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(CPJParser.RBRACE, 0)

        def getRuleIndex(self):
            return CPJParser.RULE_guiBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGuiBlock" ):
                listener.enterGuiBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGuiBlock" ):
                listener.exitGuiBlock(self)




    def guiBlock(self):

        localctx = CPJParser.GuiBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_guiBlock)
        self._la = 0 # Token type
        try:
            self.state = 169
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 135
                self.match(CPJParser.GUI_KW)
                self.state = 136
                self.match(CPJParser.Identifier)
                self.state = 137
                self.match(CPJParser.COLON)
                self.state = 138
                self.match(CPJParser.NEWLINE)
                self.state = 139
                self.match(CPJParser.INDENT)
                self.state = 141 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 140
                    self.guiBody()
                    self.state = 143 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 2235272780628112) != 0)):
                        break

                self.state = 145
                self.match(CPJParser.DEDENT)
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 2)
                self.state = 147
                self.match(CPJParser.GUI_CAP)
                self.state = 148
                self.match(CPJParser.LBRACE)
                self.state = 152
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==4:
                    self.state = 149
                    self.match(CPJParser.NEWLINE)
                    self.state = 154
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 155
                self.match(CPJParser.INDENT)
                self.state = 157 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 156
                    self.guiBody()
                    self.state = 159 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 2235272780628112) != 0)):
                        break

                self.state = 161
                self.match(CPJParser.DEDENT)
                self.state = 162
                self.match(CPJParser.RBRACE)
                self.state = 166
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 163
                        self.match(CPJParser.NEWLINE) 
                    self.state = 168
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GuiBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typesLine(self):
            return self.getTypedRuleContext(CPJParser.TypesLineContext,0)


        def widgetStmt(self):
            return self.getTypedRuleContext(CPJParser.WidgetStmtContext,0)


        def callStmt(self):
            return self.getTypedRuleContext(CPJParser.CallStmtContext,0)


        def guiProp(self):
            return self.getTypedRuleContext(CPJParser.GuiPropContext,0)


        def expression(self):
            return self.getTypedRuleContext(CPJParser.ExpressionContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(CPJParser.NEWLINE)
            else:
                return self.getToken(CPJParser.NEWLINE, i)

        def getRuleIndex(self):
            return CPJParser.RULE_guiBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGuiBody" ):
                listener.enterGuiBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGuiBody" ):
                listener.exitGuiBody(self)




    def guiBody(self):

        localctx = CPJParser.GuiBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_guiBody)
        try:
            self.state = 184
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 171
                self.typesLine()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 172
                self.widgetStmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 173
                self.callStmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 174
                self.guiProp()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 175
                self.expression()
                self.state = 177
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                if la_ == 1:
                    self.state = 176
                    self.match(CPJParser.NEWLINE)


                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 180 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 179
                        self.match(CPJParser.NEWLINE)

                    else:
                        raise NoViableAltException(self)
                    self.state = 182 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GuiPropContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(CPJParser.Identifier, 0)

        def COLON(self):
            return self.getToken(CPJParser.COLON, 0)

        def expression(self):
            return self.getTypedRuleContext(CPJParser.ExpressionContext,0)


        def NEWLINE(self):
            return self.getToken(CPJParser.NEWLINE, 0)

        def getRuleIndex(self):
            return CPJParser.RULE_guiProp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGuiProp" ):
                listener.enterGuiProp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGuiProp" ):
                listener.exitGuiProp(self)




    def guiProp(self):

        localctx = CPJParser.GuiPropContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_guiProp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.match(CPJParser.Identifier)
            self.state = 187
            self.match(CPJParser.COLON)
            self.state = 188
            self.expression()
            self.state = 189
            self.match(CPJParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypesLineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPES_KW(self):
            return self.getToken(CPJParser.TYPES_KW, 0)

        def typesTokens(self):
            return self.getTypedRuleContext(CPJParser.TypesTokensContext,0)


        def typesDict(self):
            return self.getTypedRuleContext(CPJParser.TypesDictContext,0)


        def getRuleIndex(self):
            return CPJParser.RULE_typesLine

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypesLine" ):
                listener.enterTypesLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypesLine" ):
                listener.exitTypesLine(self)




    def typesLine(self):

        localctx = CPJParser.TypesLineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_typesLine)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.match(CPJParser.TYPES_KW)
            self.state = 194
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [50]:
                self.state = 192
                self.typesTokens()
                pass
            elif token in [11]:
                self.state = 193
                self.typesDict()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypesTokensContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(CPJParser.NEWLINE, 0)

        def Identifier(self, i:int=None):
            if i is None:
                return self.getTokens(CPJParser.Identifier)
            else:
                return self.getToken(CPJParser.Identifier, i)

        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(CPJParser.COLON)
            else:
                return self.getToken(CPJParser.COLON, i)

        def getRuleIndex(self):
            return CPJParser.RULE_typesTokens

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypesTokens" ):
                listener.enterTypesTokens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypesTokens" ):
                listener.exitTypesTokens(self)




    def typesTokens(self):

        localctx = CPJParser.TypesTokensContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_typesTokens)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 202
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
                if la_ == 1:
                    self.state = 196
                    self.match(CPJParser.Identifier)
                    self.state = 197
                    self.match(CPJParser.COLON)
                    self.state = 198
                    self.match(CPJParser.Identifier)
                    pass

                elif la_ == 2:
                    self.state = 199
                    self.match(CPJParser.Identifier)
                    self.state = 200
                    self.match(CPJParser.T__0)
                    self.state = 201
                    self.match(CPJParser.Identifier)
                    pass


                self.state = 204 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==50):
                    break

            self.state = 206
            self.match(CPJParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypesDictContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(CPJParser.LBRACE, 0)

        def typeEntries(self):
            return self.getTypedRuleContext(CPJParser.TypeEntriesContext,0)


        def RBRACE(self):
            return self.getToken(CPJParser.RBRACE, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(CPJParser.NEWLINE)
            else:
                return self.getToken(CPJParser.NEWLINE, i)

        def INDENT(self):
            return self.getToken(CPJParser.INDENT, 0)

        def DEDENT(self):
            return self.getToken(CPJParser.DEDENT, 0)

        def typeLine(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CPJParser.TypeLineContext)
            else:
                return self.getTypedRuleContext(CPJParser.TypeLineContext,i)


        def getRuleIndex(self):
            return CPJParser.RULE_typesDict

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypesDict" ):
                listener.enterTypesDict(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypesDict" ):
                listener.exitTypesDict(self)




    def typesDict(self):

        localctx = CPJParser.TypesDictContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_typesDict)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.match(CPJParser.LBRACE)
            self.state = 230
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [49, 50]:
                self.state = 209
                self.typeEntries()
                self.state = 210
                self.match(CPJParser.RBRACE)
                self.state = 211
                self.match(CPJParser.NEWLINE)
                pass
            elif token in [4]:
                self.state = 213
                self.match(CPJParser.NEWLINE)
                self.state = 214
                self.match(CPJParser.INDENT)
                self.state = 218
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==4:
                    self.state = 215
                    self.match(CPJParser.NEWLINE)
                    self.state = 220
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 222 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 221
                    self.typeLine()
                    self.state = 224 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==49 or _la==50):
                        break

                self.state = 226
                self.match(CPJParser.DEDENT)
                self.state = 227
                self.match(CPJParser.RBRACE)
                self.state = 228
                self.match(CPJParser.NEWLINE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeEntriesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeEntry(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CPJParser.TypeEntryContext)
            else:
                return self.getTypedRuleContext(CPJParser.TypeEntryContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CPJParser.COMMA)
            else:
                return self.getToken(CPJParser.COMMA, i)

        def getRuleIndex(self):
            return CPJParser.RULE_typeEntries

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeEntries" ):
                listener.enterTypeEntries(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeEntries" ):
                listener.exitTypeEntries(self)




    def typeEntries(self):

        localctx = CPJParser.TypeEntriesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_typeEntries)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.typeEntry()
            self.state = 237
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 233
                    self.match(CPJParser.COMMA)
                    self.state = 234
                    self.typeEntry() 
                self.state = 239
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

            self.state = 241
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 240
                self.match(CPJParser.COMMA)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeLineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeEntry(self):
            return self.getTypedRuleContext(CPJParser.TypeEntryContext,0)


        def NEWLINE(self):
            return self.getToken(CPJParser.NEWLINE, 0)

        def COMMA(self):
            return self.getToken(CPJParser.COMMA, 0)

        def getRuleIndex(self):
            return CPJParser.RULE_typeLine

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeLine" ):
                listener.enterTypeLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeLine" ):
                listener.exitTypeLine(self)




    def typeLine(self):

        localctx = CPJParser.TypeLineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_typeLine)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self.typeEntry()
            self.state = 245
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 244
                self.match(CPJParser.COMMA)


            self.state = 247
            self.match(CPJParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeEntryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(CPJParser.COLON, 0)

        def StringLiteral(self, i:int=None):
            if i is None:
                return self.getTokens(CPJParser.StringLiteral)
            else:
                return self.getToken(CPJParser.StringLiteral, i)

        def Identifier(self, i:int=None):
            if i is None:
                return self.getTokens(CPJParser.Identifier)
            else:
                return self.getToken(CPJParser.Identifier, i)

        def getRuleIndex(self):
            return CPJParser.RULE_typeEntry

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeEntry" ):
                listener.enterTypeEntry(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeEntry" ):
                listener.exitTypeEntry(self)




    def typeEntry(self):

        localctx = CPJParser.TypeEntryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_typeEntry)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            _la = self._input.LA(1)
            if not(_la==49 or _la==50):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 250
            self.match(CPJParser.COLON)
            self.state = 251
            _la = self._input.LA(1)
            if not(_la==49 or _la==50):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WidgetStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD_TEXT(self):
            return self.getToken(CPJParser.ADD_TEXT, 0)

        def LPAREN(self):
            return self.getToken(CPJParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(CPJParser.RPAREN, 0)

        def args(self):
            return self.getTypedRuleContext(CPJParser.ArgsContext,0)


        def ADD_BTN(self):
            return self.getToken(CPJParser.ADD_BTN, 0)

        def ADD_CHECK(self):
            return self.getToken(CPJParser.ADD_CHECK, 0)

        def ADD_SLIDER(self):
            return self.getToken(CPJParser.ADD_SLIDER, 0)

        def getRuleIndex(self):
            return CPJParser.RULE_widgetStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWidgetStmt" ):
                listener.enterWidgetStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWidgetStmt" ):
                listener.exitWidgetStmt(self)




    def widgetStmt(self):

        localctx = CPJParser.WidgetStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_widgetStmt)
        self._la = 0 # Token type
        try:
            self.state = 277
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [36]:
                self.enterOuterAlt(localctx, 1)
                self.state = 253
                self.match(CPJParser.ADD_TEXT)
                self.state = 254
                self.match(CPJParser.LPAREN)
                self.state = 256
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2234207628738688) != 0):
                    self.state = 255
                    self.args()


                self.state = 258
                self.match(CPJParser.RPAREN)
                pass
            elif token in [37]:
                self.enterOuterAlt(localctx, 2)
                self.state = 259
                self.match(CPJParser.ADD_BTN)
                self.state = 260
                self.match(CPJParser.LPAREN)
                self.state = 262
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2234207628738688) != 0):
                    self.state = 261
                    self.args()


                self.state = 264
                self.match(CPJParser.RPAREN)
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 3)
                self.state = 265
                self.match(CPJParser.ADD_CHECK)
                self.state = 266
                self.match(CPJParser.LPAREN)
                self.state = 268
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2234207628738688) != 0):
                    self.state = 267
                    self.args()


                self.state = 270
                self.match(CPJParser.RPAREN)
                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 4)
                self.state = 271
                self.match(CPJParser.ADD_SLIDER)
                self.state = 272
                self.match(CPJParser.LPAREN)
                self.state = 274
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2234207628738688) != 0):
                    self.state = 273
                    self.args()


                self.state = 276
                self.match(CPJParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arg(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CPJParser.ArgContext)
            else:
                return self.getTypedRuleContext(CPJParser.ArgContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CPJParser.COMMA)
            else:
                return self.getToken(CPJParser.COMMA, i)

        def getRuleIndex(self):
            return CPJParser.RULE_args

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgs" ):
                listener.enterArgs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgs" ):
                listener.exitArgs(self)




    def args(self):

        localctx = CPJParser.ArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            self.arg()
            self.state = 284
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 280
                self.match(CPJParser.COMMA)
                self.state = 281
                self.arg()
                self.state = 286
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def StringLiteral(self):
            return self.getToken(CPJParser.StringLiteral, 0)

        def expression(self):
            return self.getTypedRuleContext(CPJParser.ExpressionContext,0)


        def getRuleIndex(self):
            return CPJParser.RULE_arg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArg" ):
                listener.enterArg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArg" ):
                listener.exitArg(self)




    def arg(self):

        localctx = CPJParser.ArgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_arg)
        try:
            self.state = 289
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 287
                self.match(CPJParser.StringLiteral)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 288
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprNoNewlineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(CPJParser.ExpressionContext,0)


        def getRuleIndex(self):
            return CPJParser.RULE_exprNoNewline

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprNoNewline" ):
                listener.enterExprNoNewline(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprNoNewline" ):
                listener.exitExprNoNewline(self)




    def exprNoNewline(self):

        localctx = CPJParser.ExprNoNewlineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_exprNoNewline)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 291
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lambdaExpr(self):
            return self.getTypedRuleContext(CPJParser.LambdaExprContext,0)


        def getRuleIndex(self):
            return CPJParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = CPJParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 293
            self.lambdaExpr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LambdaExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicalOr(self):
            return self.getTypedRuleContext(CPJParser.LogicalOrContext,0)


        def getRuleIndex(self):
            return CPJParser.RULE_lambdaExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLambdaExpr" ):
                listener.enterLambdaExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLambdaExpr" ):
                listener.exitLambdaExpr(self)




    def lambdaExpr(self):

        localctx = CPJParser.LambdaExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_lambdaExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            self.logicalOr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalOrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicalAnd(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CPJParser.LogicalAndContext)
            else:
                return self.getTypedRuleContext(CPJParser.LogicalAndContext,i)


        def getRuleIndex(self):
            return CPJParser.RULE_logicalOr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalOr" ):
                listener.enterLogicalOr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalOr" ):
                listener.exitLogicalOr(self)




    def logicalOr(self):

        localctx = CPJParser.LogicalOrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_logicalOr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297
            self.logicalAnd()
            self.state = 302
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 298
                self.match(CPJParser.T__1)
                self.state = 299
                self.logicalAnd()
                self.state = 304
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalAndContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def equality(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CPJParser.EqualityContext)
            else:
                return self.getTypedRuleContext(CPJParser.EqualityContext,i)


        def getRuleIndex(self):
            return CPJParser.RULE_logicalAnd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalAnd" ):
                listener.enterLogicalAnd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalAnd" ):
                listener.exitLogicalAnd(self)




    def logicalAnd(self):

        localctx = CPJParser.LogicalAndContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_logicalAnd)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            self.equality()
            self.state = 310
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 306
                self.match(CPJParser.T__2)
                self.state = 307
                self.equality()
                self.state = 312
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EqualityContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comparison(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CPJParser.ComparisonContext)
            else:
                return self.getTypedRuleContext(CPJParser.ComparisonContext,i)


        def EQ(self, i:int=None):
            if i is None:
                return self.getTokens(CPJParser.EQ)
            else:
                return self.getToken(CPJParser.EQ, i)

        def NEQ(self, i:int=None):
            if i is None:
                return self.getTokens(CPJParser.NEQ)
            else:
                return self.getToken(CPJParser.NEQ, i)

        def getRuleIndex(self):
            return CPJParser.RULE_equality

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEquality" ):
                listener.enterEquality(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEquality" ):
                listener.exitEquality(self)




    def equality(self):

        localctx = CPJParser.EqualityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_equality)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 313
            self.comparison()
            self.state = 318
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==25 or _la==26:
                self.state = 314
                _la = self._input.LA(1)
                if not(_la==25 or _la==26):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 315
                self.comparison()
                self.state = 320
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparisonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bitwiseOr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CPJParser.BitwiseOrContext)
            else:
                return self.getTypedRuleContext(CPJParser.BitwiseOrContext,i)


        def LT(self, i:int=None):
            if i is None:
                return self.getTokens(CPJParser.LT)
            else:
                return self.getToken(CPJParser.LT, i)

        def GT(self, i:int=None):
            if i is None:
                return self.getTokens(CPJParser.GT)
            else:
                return self.getToken(CPJParser.GT, i)

        def LE(self, i:int=None):
            if i is None:
                return self.getTokens(CPJParser.LE)
            else:
                return self.getToken(CPJParser.LE, i)

        def GE(self, i:int=None):
            if i is None:
                return self.getTokens(CPJParser.GE)
            else:
                return self.getToken(CPJParser.GE, i)

        def IN(self, i:int=None):
            if i is None:
                return self.getTokens(CPJParser.IN)
            else:
                return self.getToken(CPJParser.IN, i)

        def IS(self, i:int=None):
            if i is None:
                return self.getTokens(CPJParser.IS)
            else:
                return self.getToken(CPJParser.IS, i)

        def getRuleIndex(self):
            return CPJParser.RULE_comparison

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparison" ):
                listener.enterComparison(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparison" ):
                listener.exitComparison(self)




    def comparison(self):

        localctx = CPJParser.ComparisonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_comparison)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 321
            self.bitwiseOr()
            self.state = 326
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 13194170990592) != 0):
                self.state = 322
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 13194170990592) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 323
                self.bitwiseOr()
                self.state = 328
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BitwiseOrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bitwiseXor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CPJParser.BitwiseXorContext)
            else:
                return self.getTypedRuleContext(CPJParser.BitwiseXorContext,i)


        def BITOR(self, i:int=None):
            if i is None:
                return self.getTokens(CPJParser.BITOR)
            else:
                return self.getToken(CPJParser.BITOR, i)

        def getRuleIndex(self):
            return CPJParser.RULE_bitwiseOr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBitwiseOr" ):
                listener.enterBitwiseOr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBitwiseOr" ):
                listener.exitBitwiseOr(self)




    def bitwiseOr(self):

        localctx = CPJParser.BitwiseOrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_bitwiseOr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 329
            self.bitwiseXor()
            self.state = 334
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==29:
                self.state = 330
                self.match(CPJParser.BITOR)
                self.state = 331
                self.bitwiseXor()
                self.state = 336
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BitwiseXorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bitwiseAnd(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CPJParser.BitwiseAndContext)
            else:
                return self.getTypedRuleContext(CPJParser.BitwiseAndContext,i)


        def BITXOR(self, i:int=None):
            if i is None:
                return self.getTokens(CPJParser.BITXOR)
            else:
                return self.getToken(CPJParser.BITXOR, i)

        def getRuleIndex(self):
            return CPJParser.RULE_bitwiseXor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBitwiseXor" ):
                listener.enterBitwiseXor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBitwiseXor" ):
                listener.exitBitwiseXor(self)




    def bitwiseXor(self):

        localctx = CPJParser.BitwiseXorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_bitwiseXor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 337
            self.bitwiseAnd()
            self.state = 342
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==30:
                self.state = 338
                self.match(CPJParser.BITXOR)
                self.state = 339
                self.bitwiseAnd()
                self.state = 344
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BitwiseAndContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def shift(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CPJParser.ShiftContext)
            else:
                return self.getTypedRuleContext(CPJParser.ShiftContext,i)


        def BITAND(self, i:int=None):
            if i is None:
                return self.getTokens(CPJParser.BITAND)
            else:
                return self.getToken(CPJParser.BITAND, i)

        def getRuleIndex(self):
            return CPJParser.RULE_bitwiseAnd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBitwiseAnd" ):
                listener.enterBitwiseAnd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBitwiseAnd" ):
                listener.exitBitwiseAnd(self)




    def bitwiseAnd(self):

        localctx = CPJParser.BitwiseAndContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_bitwiseAnd)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 345
            self.shift()
            self.state = 350
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==31:
                self.state = 346
                self.match(CPJParser.BITAND)
                self.state = 347
                self.shift()
                self.state = 352
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ShiftContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sum_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CPJParser.SumContext)
            else:
                return self.getTypedRuleContext(CPJParser.SumContext,i)


        def LSHIFT(self, i:int=None):
            if i is None:
                return self.getTokens(CPJParser.LSHIFT)
            else:
                return self.getToken(CPJParser.LSHIFT, i)

        def RSHIFT(self, i:int=None):
            if i is None:
                return self.getTokens(CPJParser.RSHIFT)
            else:
                return self.getToken(CPJParser.RSHIFT, i)

        def getRuleIndex(self):
            return CPJParser.RULE_shift

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterShift" ):
                listener.enterShift(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitShift" ):
                listener.exitShift(self)




    def shift(self):

        localctx = CPJParser.ShiftContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_shift)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 353
            self.sum_()
            self.state = 358
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==27 or _la==28:
                self.state = 354
                _la = self._input.LA(1)
                if not(_la==27 or _la==28):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 355
                self.sum_()
                self.state = 360
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SumContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CPJParser.TermContext)
            else:
                return self.getTypedRuleContext(CPJParser.TermContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(CPJParser.PLUS)
            else:
                return self.getToken(CPJParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(CPJParser.MINUS)
            else:
                return self.getToken(CPJParser.MINUS, i)

        def getRuleIndex(self):
            return CPJParser.RULE_sum

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSum" ):
                listener.enterSum(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSum" ):
                listener.exitSum(self)




    def sum_(self):

        localctx = CPJParser.SumContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_sum)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 361
            self.term()
            self.state = 366
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,41,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 362
                    _la = self._input.LA(1)
                    if not(_la==14 or _la==15):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 363
                    self.term() 
                self.state = 368
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,41,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CPJParser.FactorContext)
            else:
                return self.getTypedRuleContext(CPJParser.FactorContext,i)


        def STAR(self, i:int=None):
            if i is None:
                return self.getTokens(CPJParser.STAR)
            else:
                return self.getToken(CPJParser.STAR, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(CPJParser.DIV)
            else:
                return self.getToken(CPJParser.DIV, i)

        def MOD(self, i:int=None):
            if i is None:
                return self.getTokens(CPJParser.MOD)
            else:
                return self.getToken(CPJParser.MOD, i)

        def getRuleIndex(self):
            return CPJParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)




    def term(self):

        localctx = CPJParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 369
            self.factor()
            self.state = 374
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 458752) != 0):
                self.state = 370
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 458752) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 371
                self.factor()
                self.state = 376
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(CPJParser.FactorContext,0)


        def PLUS(self):
            return self.getToken(CPJParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(CPJParser.MINUS, 0)

        def TILDE(self):
            return self.getToken(CPJParser.TILDE, 0)

        def power(self):
            return self.getTypedRuleContext(CPJParser.PowerContext,0)


        def getRuleIndex(self):
            return CPJParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)




    def factor(self):

        localctx = CPJParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.state = 380
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14, 15, 20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 377
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1097728) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 378
                self.factor()
                pass
            elif token in [7, 44, 45, 46, 47, 48, 49, 50]:
                self.enterOuterAlt(localctx, 2)
                self.state = 379
                self.power()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PowerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom(self):
            return self.getTypedRuleContext(CPJParser.AtomContext,0)


        def POW(self):
            return self.getToken(CPJParser.POW, 0)

        def factor(self):
            return self.getTypedRuleContext(CPJParser.FactorContext,0)


        def getRuleIndex(self):
            return CPJParser.RULE_power

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPower" ):
                listener.enterPower(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPower" ):
                listener.exitPower(self)




    def power(self):

        localctx = CPJParser.PowerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_power)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 382
            self.atom()
            self.state = 385
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
                self.state = 383
                self.match(CPJParser.POW)
                self.state = 384
                self.factor()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(CPJParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(CPJParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(CPJParser.RPAREN, 0)

        def literal(self):
            return self.getTypedRuleContext(CPJParser.LiteralContext,0)


        def dottedName(self):
            return self.getTypedRuleContext(CPJParser.DottedNameContext,0)


        def argList(self):
            return self.getTypedRuleContext(CPJParser.ArgListContext,0)


        def getRuleIndex(self):
            return CPJParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)




    def atom(self):

        localctx = CPJParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_atom)
        self._la = 0 # Token type
        try:
            self.state = 400
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 387
                self.match(CPJParser.LPAREN)
                self.state = 388
                self.expression()
                self.state = 389
                self.match(CPJParser.RPAREN)
                pass
            elif token in [44, 45, 46, 47, 48, 49]:
                self.enterOuterAlt(localctx, 2)
                self.state = 391
                self.literal()
                pass
            elif token in [50]:
                self.enterOuterAlt(localctx, 3)
                self.state = 392
                self.dottedName()
                self.state = 398
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
                if la_ == 1:
                    self.state = 393
                    self.match(CPJParser.LPAREN)
                    self.state = 395
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2234207628738688) != 0):
                        self.state = 394
                        self.argList()


                    self.state = 397
                    self.match(CPJParser.RPAREN)


                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CPJParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(CPJParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CPJParser.COMMA)
            else:
                return self.getToken(CPJParser.COMMA, i)

        def getRuleIndex(self):
            return CPJParser.RULE_argList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgList" ):
                listener.enterArgList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgList" ):
                listener.exitArgList(self)




    def argList(self):

        localctx = CPJParser.ArgListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_argList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 402
            self.expression()
            self.state = 407
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 403
                self.match(CPJParser.COMMA)
                self.state = 404
                self.expression()
                self.state = 409
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dottedName(self):
            return self.getTypedRuleContext(CPJParser.DottedNameContext,0)


        def LPAREN(self):
            return self.getToken(CPJParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(CPJParser.RPAREN, 0)

        def argList(self):
            return self.getTypedRuleContext(CPJParser.ArgListContext,0)


        def NEWLINE(self):
            return self.getToken(CPJParser.NEWLINE, 0)

        def INDENT(self):
            return self.getToken(CPJParser.INDENT, 0)

        def DEDENT(self):
            return self.getToken(CPJParser.DEDENT, 0)

        def getRuleIndex(self):
            return CPJParser.RULE_callStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCallStmt" ):
                listener.enterCallStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCallStmt" ):
                listener.exitCallStmt(self)




    def callStmt(self):

        localctx = CPJParser.CallStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_callStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 410
            self.dottedName()
            self.state = 411
            self.match(CPJParser.LPAREN)
            self.state = 413
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2234207628738688) != 0):
                self.state = 412
                self.argList()


            self.state = 415
            self.match(CPJParser.RPAREN)
            self.state = 417
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.state = 416
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 112) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DottedNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self, i:int=None):
            if i is None:
                return self.getTokens(CPJParser.Identifier)
            else:
                return self.getToken(CPJParser.Identifier, i)

        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(CPJParser.DOT)
            else:
                return self.getToken(CPJParser.DOT, i)

        def getRuleIndex(self):
            return CPJParser.RULE_dottedName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDottedName" ):
                listener.enterDottedName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDottedName" ):
                listener.exitDottedName(self)




    def dottedName(self):

        localctx = CPJParser.DottedNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_dottedName)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 419
            self.match(CPJParser.Identifier)
            self.state = 424
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13:
                self.state = 420
                self.match(CPJParser.DOT)
                self.state = 421
                self.match(CPJParser.Identifier)
                self.state = 426
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Integer(self):
            return self.getToken(CPJParser.Integer, 0)

        def Float(self):
            return self.getToken(CPJParser.Float, 0)

        def StringLiteral(self):
            return self.getToken(CPJParser.StringLiteral, 0)

        def TRUE(self):
            return self.getToken(CPJParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(CPJParser.FALSE, 0)

        def NULL(self):
            return self.getToken(CPJParser.NULL, 0)

        def getRuleIndex(self):
            return CPJParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)




    def literal(self):

        localctx = CPJParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 427
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1108307720798208) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





