
from matplotlib.colors import LinearSegmentedColormap
from numpy import nan, inf

# Used to reconstruct the colormap in pycam02ucs.cm.viscm
parameters = {'xp': [-3.3554044380815924, -37.47613934621805, -30.586375566690492, -13.526008112622264, 2.222023383440728],
              'yp': [-18.471128608923863, -4.691601049868751, 2.854330708661422, 16.30577427821521, 1.8700787401574814],
              'min_Jp': 15.067114094,
              'max_Jp': 97.9530201342}

cm_data = [[ 0.07709451,  0.12147455,  0.22706729],
       [ 0.07845587,  0.12518534,  0.22952556],
       [ 0.07981767,  0.12887264,  0.23199289],
       [ 0.08116407,  0.13254313,  0.23446213],
       [ 0.08250356,  0.13619509,  0.23693723],
       [ 0.08383211,  0.1398309 ,  0.23941655],
       [ 0.08514678,  0.14345243,  0.24189903],
       [ 0.08645459,  0.14705837,  0.24438769],
       [ 0.08774196,  0.15065372,  0.24687722],
       [ 0.08902614,  0.15423398,  0.2493746 ],
       [ 0.09028372,  0.15780685,  0.25187093],
       [ 0.09153733,  0.16136627,  0.25437498],
       [ 0.09276661,  0.16491879,  0.25687933],
       [ 0.09398699,  0.16846051,  0.25938974],
       [ 0.09518516,  0.17199572,  0.26190163],
       [ 0.09636979,  0.17552248,  0.26441814],
       [ 0.09753381,  0.17904319,  0.26693701],
       [ 0.09868017,  0.18255747,  0.26945933],
       [ 0.09980693,  0.18606622,  0.27198458],
       [ 0.10091248,  0.18957025,  0.27451238],
       [ 0.10199884,  0.19306937,  0.2770434 ],
       [ 0.10306104,  0.19656517,  0.27957627],
       [ 0.1041038 ,  0.20005678,  0.28211241],
       [ 0.10512011,  0.20354622,  0.28464991],
       [ 0.106116  ,  0.20703228,  0.28719045],
       [ 0.10708391,  0.21051703,  0.28973205],
       [ 0.10802962,  0.21399934,  0.29227625],
       [ 0.10894661,  0.21748097,  0.29482137],
       [ 0.10983877,  0.2209612 ,  0.2973684 ],
       [ 0.11070237,  0.22444111,  0.29991639],
       [ 0.11153756,  0.22792082,  0.30246538],
       [ 0.11234533,  0.23140029,  0.30501554],
       [ 0.11312008,  0.23488092,  0.30756556],
       [ 0.11386965,  0.23836115,  0.31011712],
       [ 0.11458043,  0.24184403,  0.31266719],
       [ 0.11526947,  0.24532608,  0.31521931],
       [ 0.1159127 ,  0.24881244,  0.31776839],
       [ 0.11653566,  0.25229796,  0.32031955],
       [ 0.11711101,  0.25578829,  0.32286719],
       [ 0.11766094,  0.25927905,  0.32541558],
       [ 0.11816953,  0.2627735 ,  0.32796151],
       [ 0.11864268,  0.26627053,  0.33050597],
       [ 0.11908246,  0.26976983,  0.33304918],
       [ 0.11947506,  0.27327407,  0.33558847],
       [ 0.11984105,  0.27677942,  0.3381274 ],
       [ 0.1201523 ,  0.28029117,  0.34066079],
       [ 0.12043183,  0.28380507,  0.34319253],
       [ 0.12066875,  0.28732317,  0.34572052],
       [ 0.12085789,  0.29084637,  0.34824372],
       [ 0.12101548,  0.29437183,  0.35076464],
       [ 0.12111366,  0.29790441,  0.35327846],
       [ 0.12117465,  0.30144024,  0.35578864],
       [ 0.12119377,  0.30498014,  0.35829416],
       [ 0.12115412,  0.30852689,  0.36079212],
       [ 0.12107751,  0.31207684,  0.36328573],
       [ 0.12094878,  0.31563247,  0.36577237],
       [ 0.12076508,  0.31919414,  0.36825136],
       [ 0.12054105,  0.3227595 ,  0.3707247 ],
       [ 0.12025905,  0.32633125,  0.37318941],
       [ 0.11992142,  0.32990895,  0.3756456 ],
       [ 0.11953989,  0.33349074,  0.37809474],
       [ 0.11910001,  0.33707874,  0.38053437],
       [ 0.11859842,  0.3406733 ,  0.3829637 ],
       [ 0.11804926,  0.3442723 ,  0.38538451],
       [ 0.11744807,  0.34787632,  0.38779581],
       [ 0.11677265,  0.35148832,  0.39019399],
       [ 0.11604597,  0.355105  ,  0.3925821 ],
       [ 0.11526685,  0.35872645,  0.39495957],
       [ 0.11442318,  0.36235418,  0.39732425],
       [ 0.11350984,  0.36598869,  0.39967502],
       [ 0.11254059,  0.36962808,  0.40201344],
       [ 0.11151429,  0.3732724 ,  0.4043389 ],
       [ 0.11042605,  0.37692215,  0.40665022],
       [ 0.10925967,  0.38057913,  0.40894458],
       [ 0.10803357,  0.38424096,  0.4112241 ],
       [ 0.10674694,  0.38790765,  0.4134881 ],
       [ 0.10539911,  0.39157917,  0.41573588],
       [ 0.10398952,  0.39525548,  0.41796671],
       [ 0.10250398,  0.39893799,  0.42017788],
       [ 0.10095333,  0.4026254 ,  0.42237017],
       [ 0.09934172,  0.40631718,  0.42454336],
       [ 0.09766981,  0.41001318,  0.42669667],
       [ 0.09593871,  0.41371326,  0.42882926],
       [ 0.09415005,  0.41741722,  0.43094032],
       [ 0.0923061 ,  0.42112485,  0.43302896],
       [ 0.09040991,  0.42483589,  0.43509433],
       [ 0.08846541,  0.42855005,  0.43713553],
       [ 0.08647764,  0.43226699,  0.43915164],
       [ 0.08445293,  0.43598636,  0.44114175],
       [ 0.08239909,  0.43970772,  0.44310493],
       [ 0.08032574,  0.44343061,  0.44504024],
       [ 0.07824453,  0.44715451,  0.44694674],
       [ 0.07616954,  0.45087884,  0.44882349],
       [ 0.07411756,  0.45460297,  0.45066957],
       [ 0.07210848,  0.45832621,  0.45248407],
       [ 0.07016564,  0.46204779,  0.4542661 ],
       [ 0.06831614,  0.4657669 ,  0.4560148 ],
       [ 0.06659104,  0.46948263,  0.45772935],
       [ 0.06502547,  0.47319403,  0.45940899],
       [ 0.06363665,  0.47690148,  0.46104927],
       [ 0.0624868 ,  0.48060258,  0.46265263],
       [ 0.06162351,  0.484296  ,  0.46421879],
       [ 0.06109438,  0.48798046,  0.46574734],
       [ 0.0609235 ,  0.49165616,  0.46723304],
       [ 0.06117802,  0.4953203 ,  0.46867955],
       [ 0.06190383,  0.49897112,  0.47008771],
       [ 0.06311442,  0.50260861,  0.47145175],
       [ 0.06485932,  0.50622965,  0.4727771 ],
       [ 0.06714971,  0.50983306,  0.4740621 ],
       [ 0.06999296,  0.51341722,  0.4753067 ],
       [ 0.07339273,  0.51697987,  0.47651402],
       [ 0.0773329 ,  0.52051968,  0.47768288],
       [ 0.08179843,  0.5240344 ,  0.47881746],
       [ 0.08676155,  0.52752246,  0.47991889],
       [ 0.09219141,  0.53098217,  0.48098974],
       [ 0.09805384,  0.53441172,  0.48203535],
       [ 0.10431154,  0.53781002,  0.48305575],
       [ 0.11092647,  0.54117556,  0.48405837],
       [ 0.11785994,  0.54450742,  0.48504714],
       [ 0.12507553,  0.54780491,  0.48602513],
       [ 0.13253507,  0.55106752,  0.48699922],
       [ 0.14020357,  0.55429513,  0.48797407],
       [ 0.1480484 ,  0.55748785,  0.48895423],
       [ 0.15603763,  0.56064614,  0.4899452 ],
       [ 0.16414256,  0.5637707 ,  0.49095165],
       [ 0.17233692,  0.56686244,  0.49197796],
       [ 0.18059602,  0.56992257,  0.49302873],
       [ 0.18889935,  0.57295235,  0.49410728],
       [ 0.1972286 ,  0.57595318,  0.49521673],
       [ 0.20556461,  0.5789268 ,  0.49636129],
       [ 0.2138956 ,  0.58187463,  0.49754234],
       [ 0.22221032,  0.58479822,  0.49876168],
       [ 0.23049435,  0.58769957,  0.50002289],
       [ 0.23874329,  0.59057995,  0.50132566],
       [ 0.24694995,  0.59344092,  0.50267129],
       [ 0.25510518,  0.59628441,  0.50406203],
       [ 0.26321004,  0.5991113 ,  0.50549639],
       [ 0.27125586,  0.60192358,  0.50697684],
       [ 0.27924433,  0.60472213,  0.50850207],
       [ 0.28717174,  0.60750842,  0.51007291],
       [ 0.29503732,  0.61028363,  0.51168924],
       [ 0.3028414 ,  0.61304876,  0.51335063],
       [ 0.31058241,  0.61580506,  0.51505741],
       [ 0.31826219,  0.6185533 ,  0.51680877],
       [ 0.32588026,  0.62129454,  0.51860477],
       [ 0.3334375 ,  0.62402966,  0.52044504],
       [ 0.34093642,  0.6267592 ,  0.52232871],
       [ 0.34837472,  0.6294845 ,  0.52425651],
       [ 0.35575899,  0.63220536,  0.52622637],
       [ 0.3630837 ,  0.63492362,  0.52824001],
       [ 0.37035613,  0.63763889,  0.53029526],
       [ 0.3775757 ,  0.6403521 ,  0.53239233],
       [ 0.38474193,  0.64306415,  0.53453141],
       [ 0.39186018,  0.64577484,  0.53671102],
       [ 0.39892846,  0.6484853 ,  0.5389318 ],
       [ 0.40594903,  0.65119584,  0.54119315],
       [ 0.41292548,  0.65390647,  0.54349421],
       [ 0.4198564 ,  0.65661816,  0.5458354 ],
       [ 0.4267436 ,  0.65933122,  0.54821633],
       [ 0.43359043,  0.6620456 ,  0.55063622],
       [ 0.44039717,  0.66476185,  0.55309509],
       [ 0.44716274,  0.66748083,  0.55559325],
       [ 0.45389149,  0.67020219,  0.55812977],
       [ 0.46058444,  0.67292626,  0.56070449],
       [ 0.46724102,  0.67565372,  0.56331763],
       [ 0.47386233,  0.67838487,  0.56596899],
       [ 0.48045103,  0.6811196 ,  0.5686581 ],
       [ 0.48700805,  0.68385822,  0.57138488],
       [ 0.49353346,  0.68660118,  0.57414937],
       [ 0.50002727,  0.68934897,  0.57695163],
       [ 0.50649218,  0.6921014 ,  0.57979125],
       [ 0.51292899,  0.69485872,  0.58266818],
       [ 0.51933849,  0.69762117,  0.58558236],
       [ 0.52572035,  0.70038925,  0.58853391],
       [ 0.53207549,  0.70316318,  0.59152274],
       [ 0.53840562,  0.70594289,  0.59454869],
       [ 0.54471138,  0.70872863,  0.59761175],
       [ 0.55099344,  0.71152059,  0.6007119 ],
       [ 0.55725239,  0.714319  ,  0.60384914],
       [ 0.56348749,  0.71712445,  0.6070236 ],
       [ 0.56970053,  0.7199368 ,  0.61023515],
       [ 0.57589225,  0.7227562 ,  0.61348378],
       [ 0.58206316,  0.72558286,  0.61676951],
       [ 0.58821375,  0.72841698,  0.62009236],
       [ 0.5943445 ,  0.73125875,  0.62345234],
       [ 0.60045586,  0.73410839,  0.6268495 ],
       [ 0.60654732,  0.73696637,  0.63028385],
       [ 0.6126201 ,  0.73983264,  0.63375538],
       [ 0.61867478,  0.74270736,  0.63726412],
       [ 0.62471171,  0.74559072,  0.64081008],
       [ 0.63073126,  0.74848291,  0.64439328],
       [ 0.63673377,  0.75138415,  0.64801373],
       [ 0.64271954,  0.75429461,  0.65167145],
       [ 0.6486889 ,  0.75721451,  0.65536643],
       [ 0.65464213,  0.76014403,  0.65909868],
       [ 0.66057951,  0.76308339,  0.66286818],
       [ 0.66650074,  0.76603296,  0.66667486],
       [ 0.67240658,  0.76899279,  0.67051874],
       [ 0.67829738,  0.77196303,  0.6743998 ],
       [ 0.68417337,  0.77494389,  0.67831798],
       [ 0.69003478,  0.77793558,  0.68227325],
       [ 0.69588181,  0.78093828,  0.68626554],
       [ 0.70171469,  0.7839522 ,  0.69029478],
       [ 0.7075336 ,  0.78697755,  0.69436089],
       [ 0.71333877,  0.79001452,  0.69846376],
       [ 0.71913036,  0.79306331,  0.70260329],
       [ 0.72490859,  0.79612412,  0.70677936],
       [ 0.73067363,  0.79919716,  0.71099182],
       [ 0.73642568,  0.80228262,  0.71524052],
       [ 0.74216492,  0.80538069,  0.7195253 ],
       [ 0.74789154,  0.80849158,  0.72384598],
       [ 0.75360573,  0.81161547,  0.72820236],
       [ 0.75930769,  0.81475256,  0.73259422],
       [ 0.76499763,  0.81790304,  0.73702135],
       [ 0.77067574,  0.82106708,  0.74148348],
       [ 0.77634223,  0.82424488,  0.74598037],
       [ 0.78199734,  0.82743661,  0.75051174],
       [ 0.7876413 ,  0.83064244,  0.75507729],
       [ 0.79327436,  0.83386255,  0.75967672],
       [ 0.79889676,  0.83709708,  0.76430972],
       [ 0.80450881,  0.8403462 ,  0.76897594],
       [ 0.81011078,  0.84361006,  0.77367503],
       [ 0.81570301,  0.84688878,  0.77840664],
       [ 0.82128582,  0.85018251,  0.78317039],
       [ 0.82685959,  0.85349134,  0.7879659 ],
       [ 0.83242472,  0.8568154 ,  0.79279279],
       [ 0.83798091,  0.86015507,  0.79765021],
       [ 0.84352904,  0.86351027,  0.80253799],
       [ 0.84906984,  0.86688095,  0.80745587],
       [ 0.85460388,  0.87026713,  0.81240346],
       [ 0.86013175,  0.87366884,  0.8173804 ],
       [ 0.86565412,  0.87708605,  0.82238633],
       [ 0.8711717 ,  0.88051871,  0.82742096],
       [ 0.87668527,  0.88396675,  0.83248404],
       [ 0.88219567,  0.88743005,  0.8375754 ],
       [ 0.88770294,  0.89090887,  0.84269429],
       [ 0.893208  ,  0.89440305,  0.8478407 ],
       [ 0.89871267,  0.89791196,  0.8530155 ],
       [ 0.90421799,  0.90143534,  0.85821916],
       [ 0.90972502,  0.90497288,  0.86345247],
       [ 0.91523472,  0.90852426,  0.86871657],
       [ 0.92074786,  0.91208919,  0.874013  ],
       [ 0.92626282,  0.91566851,  0.87934182],
       [ 0.93178195,  0.91926096,  0.88470769],
       [ 0.93730486,  0.92286656,  0.89011401],
       [ 0.94283031,  0.92648555,  0.8955648 ],
       [ 0.94835599,  0.9301186 ,  0.90106463],
       [ 0.95387619,  0.93376794,  0.90661588],
       [ 0.95938714,  0.93743473,  0.9122242 ],
       [ 0.96488325,  0.941121  ,  0.91789383],
       [ 0.97035725,  0.94482979,  0.92362639],
       [ 0.97580126,  0.94856468,  0.92942023],
       [ 0.98120661,  0.95233028,  0.93526756],
       [ 0.98657146,  0.95612801,  0.94116434],
       [ 0.99189439,  0.95995979,  0.9471004 ],
       [ 0.99717742,  0.96382622,  0.95306421]]

test_cm = LinearSegmentedColormap.from_list(__file__, cm_data)


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import numpy as np

    try:
        from pycam02ucs.cm.viscm import viscm
        viscm(test_cm)
    except ImportError:
        print("pycam02ucs not found, falling back on simple display")
        plt.imshow(np.linspace(0, 100, 256)[None, :], aspect='auto',
                   cmap=test_cm)
    plt.show()