class Solution:
    def isVeg(self, cur, need):
        if need == 0:
            return True
        return cur == need

    def filterRestaurants(self, restaurants, veganFriendly: int, maxPrice: int, maxDistance: int):
        ret = []
        for i in restaurants:
            if self.isVeg(i[2], veganFriendly) and i[3] <= maxPrice and i[4] <= maxDistance:
                ret.append(i)
        return [i[0] for i in sorted(ret, key=lambda x: x[1])[::-1]]


restaurants = [[99380,58446,1,83633,92294],[7675,87008,0,79179,32217],[4808,97343,1,12183,22157],[87795,23664,0,24579,84497],[79932,5685,0,89043,53549],[64765,82218,0,70934,31434],[68424,31515,0,42604,55878],[23150,4222,1,39953,46389],[4033,60234,1,50620,57384],[65391,62057,1,94880,85866],[21455,57308,0,88586,92103],[68805,43093,1,74544,6292],[4075,50338,0,62272,25759],[51123,71181,1,23393,29668],[67413,7815,0,53893,59413],[98267,76295,0,25961,6085],[74247,81314,1,9660,92448],[68989,52728,0,18555,29495],[90240,52354,1,27286,13423],[85816,50992,1,4304,78454],[10047,26474,1,46136,91451],[5599,84656,1,77580,40075],[57067,38437,0,98259,22118],[67394,74255,0,86212,90486],[1653,74743,0,57117,28195],[29114,57537,0,989,57185],[20882,72003,1,67688,96342],[60567,96884,0,81240,75055],[51203,25178,1,41528,15061],[84566,15508,0,63421,6732],[72809,50337,1,73351,7245],[13854,60819,1,7627,75821],[42956,94831,1,16404,40709],[60059,6268,0,37772,69662],[14859,77790,0,84780,10663],[56148,56426,0,55430,46654],[73347,76820,0,91882,75474],[64565,65442,1,38489,98502],[60552,61242,0,27381,77236],[70461,25223,0,8148,36313],[96295,1805,1,58785,87435],[22998,27319,1,71509,39676],[19052,11137,0,69555,11828],[86427,21842,0,53387,22052],[27949,99669,1,33138,44471],[86502,20102,0,54339,43030],[97555,99988,0,98801,98262],[95186,30268,0,82852,38334],[7456,14687,0,81916,88742],[3977,55903,0,67874,4425],[22824,89878,0,70431,57613],[95021,96278,1,82439,19211],[47737,52550,0,99313,88399],[73820,64928,1,15992,65812],[98089,37785,0,38455,82949],[68916,99860,0,37507,7201],[12095,48543,1,15024,87602],[66070,59009,1,93077,4507],[7293,72362,1,44390,45703],[32133,36780,1,34647,99684],[98873,8861,0,53514,49892],[61594,21253,1,60065,56946],[29050,59845,0,96396,66545],[51713,49796,0,26330,81271],[17459,4921,0,59876,46037],[46203,89430,0,33222,31587],[41901,40603,0,88276,33445],[56961,59646,1,85465,44671],[94130,92510,0,92326,97673],[1627,35220,1,91524,20269],[30304,78302,1,81058,50477],[642,30971,0,29103,87598],[15711,25158,0,25309,95703],[82491,30266,0,54265,95936],[44818,18889,0,61113,83044],[78253,28379,0,81259,4501],[93266,99839,0,4730,24595],[46334,8249,1,74909,78278],[28434,89092,1,51268,38148],[22486,77863,1,40453,36602],[76323,47501,0,28863,15649],[96447,49531,0,47189,37231],[46087,78252,1,6909,68674],[7454,11841,1,44419,68888],[46749,70828,0,39993,68093],[37432,50628,1,21871,19497],[70350,13135,0,86264,29163],[91609,39650,1,55301,34545],[66034,82346,1,40502,58012],[58629,7399,1,73443,53770],[34,75652,0,39046,80769],[65681,23759,0,14779,31347],[47561,58723,1,86855,37944],[19696,36371,0,95455,16901],[89101,64082,1,71773,30428],[46181,4948,0,15412,24095],[65138,59622,0,53239,8013],[75161,95902,0,9479,39834],[1467,82599,1,31790,80480],[96711,30266,0,94077,17105],[72646,76097,1,17325,76274],[91112,19526,0,46369,88237],[7337,48760,0,96650,89352],[87140,65048,1,12066,4586],[90158,92383,1,18000,50133],[84782,34846,0,4986,68775],[4980,24157,0,80415,94371],[36974,69052,0,99619,75517],[39967,24208,0,77745,14043],[62718,19477,1,15110,72752],[11020,88802,1,17387,30213],[29804,44078,1,45670,74233],[93648,87733,0,74491,8628],[95983,35792,0,1895,97944],[71646,85944,1,78017,38582],[73242,22310,0,64292,72257],[21965,47536,1,90585,72414],[56269,65474,1,45168,53515],[12820,89005,0,12941,29991],[42580,27046,0,92032,79046],[77010,93092,0,77734,46147],[29021,99150,1,49390,6758],[88021,6699,1,99882,94871],[77268,98365,1,86577,75969],[49147,91511,0,13555,43071],[23534,45614,1,61187,20822],[95616,22970,1,92459,61859],[24797,3465,0,25959,87394],[84049,24056,0,78332,96966],[97823,80201,0,11721,25003],[59357,33749,0,52233,35335],[55275,97688,0,59235,16270],[9118,27779,0,28527,4026],[22959,53984,1,57629,43411],[23321,88424,0,55110,12166],[49962,91065,1,47441,11319],[67798,89174,1,69419,88858],[73092,90580,0,25689,36576],[46766,47101,0,24592,32237],[55743,42548,1,88158,79491],[57742,60663,0,96159,72350],[99940,4666,0,44884,10138],[56528,33118,0,7599,40775],[12332,40783,0,56395,47355],[67833,10898,1,9472,57992],[62661,21495,0,75014,138],[69902,3903,0,27643,42978],[78296,12020,1,53774,66799],[85978,49570,1,49637,57408],[36928,67446,1,24957,18359],[70584,82519,1,71085,12421],[95622,63881,1,51970,94197],[24217,86539,0,11131,64536],[89689,7850,1,20282,76037],[96621,17968,0,67285,9032],[97161,51584,0,68269,51407],[46550,91176,1,22817,53331],[77772,35971,0,97097,77445],[49137,80172,0,98813,91218],[38372,37705,1,19116,26979],[61030,5097,1,15054,94690],[88330,11497,0,83516,85192],[8722,65249,0,63802,60564],[80773,51044,0,89251,6960],[54410,22225,0,38082,59543],[5884,20362,0,27276,82264],[91766,21142,0,16576,2478],[49266,82372,0,98309,53108],[80280,48219,1,43718,19830],[42227,42303,1,82730,7701],[42440,59411,0,12180,1955],[95003,3500,1,90097,13589],[24692,51103,1,79726,14377],[34387,67707,1,5757,98432],[60176,28377,0,72387,375],[91744,95529,1,55109,8325],[43890,45260,1,8080,79498],[86143,35285,0,26842,1715],[21044,58522,0,80200,74296],[53925,91027,0,72262,4286],[69368,22070,1,8522,1511],[71913,1128,0,29598,383],[69702,4112,0,78286,92235],[57069,93198,0,63853,48877],[43757,21493,0,32012,11004],[85896,28518,0,90503,39466],[12134,10319,0,16936,97641],[9872,58959,1,47338,32394],[18478,22567,0,55649,9786],[48738,69286,0,7894,70833],[88881,5684,1,859,72968],[97772,76782,1,54559,25168],[77612,14744,1,93178,43919],[65651,66043,1,21583,97053],[75796,37289,1,63895,66784],[42487,66080,1,14575,6293],[8526,8343,1,80588,55181],[84098,50649,1,43032,75547],[11753,92407,0,73073,74257],[97622,57756,1,29480,72641],[33172,97320,1,44077,85932],[40871,22666,0,14796,94290],[13176,57379,0,95055,62313],[99455,92029,1,36101,15677],[41189,50062,0,21540,68107],[96694,69904,1,95765,66203],[11621,65307,1,73872,16276],[42169,12829,0,72214,31937],[64924,31789,1,44178,5819],[21825,8092,0,56168,89755],[43466,39946,0,46567,19156],[89875,98260,0,82867,24695],[4574,23096,1,57134,89095],[34530,27533,0,27459,53152],[99087,69058,0,22921,31334],[60912,18763,1,73919,42489],[21095,88721,1,71149,75205],[81522,36946,0,25583,21863],[36957,4194,0,17060,3369],[57190,6831,1,94103,58845],[18979,56096,0,20559,71418],[46968,96312,0,96721,8981],[94087,34355,1,44000,6342],[67963,39997,0,94621,78758],[62983,84658,0,61020,82808],[54660,80372,0,2390,1078],[5686,2115,0,28198,48407],[26703,59049,0,92189,6505],[29046,39093,0,73235,23437],[25298,75076,0,48678,69663],[28165,95431,0,74401,93052],[13116,41182,0,71448,82183],[60903,86657,1,3032,71091],[62709,8884,0,59538,41919],[75067,47046,1,53929,18766],[92274,16283,0,60664,86189],[42655,21813,0,50467,2744],[66063,58197,0,87177,99023],[79502,17667,1,36855,39834],[7829,62398,1,8061,74485],[19577,119,1,78112,53972],[4857,31905,0,95630,50929],[88069,70494,0,76353,40326],[895,2948,0,69571,93746],[83430,50467,1,82289,47696],[94999,720,0,80688,94470],[56216,27998,1,65846,6465],[16960,70929,1,84383,4479],[12709,51938,0,6306,64860],[78466,64214,0,14598,91773],[64033,32834,0,7890,14208],[69798,60896,0,24017,44209],[61068,98486,0,93111,63917],[96274,49075,1,90241,38997],[63428,22576,1,68497,3813],[23113,31873,0,97075,50996],[10112,15887,1,91791,12949],[33270,86798,0,22744,99964],[89990,47379,0,58941,13055],[42328,68173,0,58528,76379],[56935,11431,0,61313,78497],[61931,33604,1,60966,61986],[49668,50287,0,49291,43748],[81979,92009,0,9059,22770],[64539,56440,0,11205,95905],[50895,89869,1,5200,99979],[3524,66064,0,59125,98076],[69463,22961,1,39669,93583],[53275,10144,0,55974,41702],[64505,56308,1,87224,82187],[4046,74721,0,22420,53109],[71537,20304,1,28196,64837],[97383,18041,1,94859,95335],[71877,83706,0,20733,78085],[92487,84749,1,2535,40788],[4947,86598,0,35278,64607],[94381,20592,1,32954,46115],[38622,42437,1,24331,68684],[77417,28035,0,79137,20486],[33055,15870,0,5803,89856],[90090,17985,1,96572,84045],[72945,15103,0,23287,54738],[55284,78649,0,5242,43019],[90532,1639,1,98981,93078],[22321,19357,1,32365,86644],[76356,5507,1,86015,20488],[42785,76833,0,81998,31935],[63064,36919,1,76798,84208],[67973,66231,1,29334,98699],[99055,21234,0,74118,32693],[59614,18187,1,22034,2694],[91387,12328,0,4479,73533],[7228,80244,1,98700,60853],[95128,3171,1,34395,37140],[36153,95762,1,62750,15609],[11506,40723,1,57060,25804],[30826,69099,0,9046,90824],[94156,95148,1,27046,13275],[45834,35289,0,28987,46917],[46080,20886,0,13731,95888],[25784,39777,0,83092,8592],[5406,43566,1,27973,47843],[80061,89743,0,99176,60163],[61310,43517,1,43558,89172],[68411,2506,0,16891,21691],[2645,3460,0,26780,98492],[91856,89563,1,40581,83827],[24269,13991,1,68958,68762],[1172,80243,0,8759,28636],[20943,41041,0,94984,41513],[30047,34365,1,51391,94063],[41632,6405,1,26217,98889],[89341,14383,1,20374,51074],[49417,27193,1,44468,31203],[64992,61192,1,95497,570],[61085,46107,1,44209,7174],[58029,51456,1,63968,92809],[90099,37700,0,65905,60638],[30395,12259,1,84891,21374],[59109,27667,1,21332,70992],[39678,95036,1,891,24676],[74040,78409,1,1793,38393],[83220,97211,1,72636,34031],[10107,98848,1,6106,74679],[72417,91536,0,25721,91159],[62012,99921,0,51732,42416],[39188,63832,1,93063,34553],[79045,21084,1,52972,65512],[72989,29574,0,53291,78345],[58584,9833,1,7386,181],[90486,24892,1,25833,13840],[91467,4933,1,25035,7124],[87691,23412,1,5607,87739],[66243,33503,0,25028,53454],[69028,8509,0,33516,5912],[19057,1808,0,77583,72646],[28278,98207,0,42956,18362],[22597,90151,1,75950,153],[365,76035,1,66320,84749],[99800,3498,0,10453,96892],[63184,60815,0,22387,35364],[68026,2411,1,38183,76429],[73441,76598,0,23754,41902],[12877,95347,1,92749,39758],[26272,74072,0,1613,36757],[27201,28375,0,71066,26031],[65325,41626,1,79195,63175],[94931,13716,1,9833,61035],[33063,62342,0,2644,43583],[62717,90681,0,32311,72089],[16458,6462,1,12602,30344],[6923,39300,1,13456,12638],[36129,36797,0,30851,70650],[97535,79445,0,62586,7314],[53983,57692,0,1602,43393],[81982,56945,1,63967,6776],[94534,57834,1,55711,82498],[3343,22094,1,47542,31533],[8890,18990,1,51803,70957],[71035,76649,1,99070,69556],[42264,48106,1,18468,80727],[27463,54545,0,13582,98623],[10629,22512,0,83234,2798],[10860,59532,0,24336,47067],[69117,72896,0,24039,96519],[54609,9932,1,14235,349],[63139,84798,1,52920,96005],[18859,76525,1,18235,78433],[31020,51065,1,24748,69560],[83195,69917,0,40455,57716],[27096,76004,1,19918,33580],[7021,21437,0,91251,64357],[70675,25854,0,52355,82486],[45183,62621,1,29010,25490],[81984,10529,0,20402,64880],[79070,94120,0,65127,35256],[51591,16193,0,12846,45469],[22112,26066,1,40604,53657],[33792,68109,0,49428,53457],[4478,5234,0,48786,53162],[42192,53713,1,59254,92894],[51347,23020,0,91180,56397],[45774,92280,1,75835,48922],[65580,56995,0,48226,99330],[16198,43783,0,27891,97560],[80335,46945,0,72942,99814],[76542,95310,1,65411,73358],[22794,55450,1,48670,3986],[21855,23997,1,90338,92000],[61610,82075,1,89653,70791],[25177,16063,1,85995,97431],[2149,56164,0,57539,40451],[55073,36131,0,72959,26022],[59337,14640,0,90914,623],[69819,75093,0,31401,4170],[79244,65313,1,26847,24988],[14580,3740,1,81935,36789],[91957,12386,0,48584,58977],[55550,43168,0,66592,39822],[11005,60800,0,20891,74155],[75874,76803,0,68612,38342],[98902,77141,1,37577,89163],[36762,12966,1,21126,23272],[68988,98214,0,56228,90645],[39579,52064,1,30397,21953],[54007,22475,1,31987,28532],[19514,37707,0,83076,9877],[90574,31369,0,84994,39968],[98531,1393,0,53197,51853],[83065,7381,0,78982,6895],[17274,60998,1,38289,31250],[20846,61690,0,83522,76588],[29522,79390,1,68637,54784],[60361,75962,1,17321,83438],[86369,67239,0,4239,17135],[83135,69763,0,76561,1233],[67956,33145,0,94122,4497],[45447,63034,0,30379,42653],[85138,99132,0,92638,27661],[88508,22598,1,86935,96685],[32429,16433,0,6127,67395],[43860,32343,1,59925,94121],[34733,93400,0,15348,5777],[11398,4765,1,65291,6598],[15761,82583,1,78880,48635],[45318,31333,0,33622,24901],[21253,44525,1,86448,96755],[42367,47496,0,10230,27941],[22725,51619,1,27495,81353],[1622,60735,1,49541,45671],[90088,48635,1,78623,78914],[1090,84911,1,98284,10133],[86852,7644,1,53331,48987],[92508,52562,0,39929,83703],[25601,80461,0,39836,3873],[55661,5085,1,755,52912],[26598,71461,1,33584,3105],[78431,91102,0,29276,89685],[85609,18237,1,31371,82470],[34501,43420,0,50486,38005],[2280,82794,1,3384,55728],[2072,14335,0,86813,32544],[2450,53051,1,20140,10093],[28148,25029,1,73747,75462],[91119,46919,1,8196,94560],[28872,25760,0,16722,79003],[36284,45461,1,55642,34569],[54065,46591,0,9820,59581],[28701,82612,1,82985,1348],[66728,78562,1,24797,47080],[75245,88645,1,49054,91882],[25853,86693,1,42303,72458],[71889,35121,1,11746,49416],[24984,96587,1,95386,75682],[25804,28375,1,62790,57571],[651,6335,1,16555,66941],[51026,9305,1,72608,76252],[16803,42277,1,50621,62356],[82571,87766,0,33692,28804],[32304,49418,1,80620,80908],[70215,98041,0,39501,60704],[66274,91626,1,84569,685],[19583,62407,1,99546,2515],[4260,51249,1,96290,14104],[26863,89749,1,94251,48740],[56457,59060,1,55703,8250],[65432,23909,0,24361,13058],[95891,55664,1,28817,23578],[50483,91052,1,93241,78403],[48489,18511,0,30621,33636],[72132,32423,0,10394,26529],[73786,57279,1,99857,5021],[42136,28846,0,56315,11063],[41853,23887,1,30899,46384],[97169,77558,0,37128,21924],[59365,94613,0,89310,3694],[13399,33262,1,13541,94254],[37243,26552,1,95420,29456],[97074,3736,1,9701,44546],[61004,59232,1,73328,83949],[29292,56678,1,49754,78557],[11422,75322,1,86735,51985],[13104,13678,1,46283,46021],[51935,62473,1,26990,84339],[28236,18482,0,15189,96397],[1819,75177,0,63832,45056],[33004,40752,0,27536,91267],[81714,71865,0,86467,33129],[93255,31258,0,74624,39197],[68545,54573,1,75778,72807],[20333,68658,1,66255,29855],[84046,41001,0,72606,97470],[43089,16821,0,51805,94194],[36931,4853,0,93263,4503],[53315,48099,0,65735,60462],[75783,95014,1,83426,66084],[38791,71288,1,52972,88772],[98395,43319,1,63830,10474],[2632,19608,1,8478,85983],[47178,7168,0,83511,50266],[42203,28299,0,56165,30634],[37143,44654,0,29480,27885],[34740,53015,1,61665,53150],[63914,77886,1,34591,2216],[61126,58781,1,69188,55839],[98286,81622,0,78118,47986],[83428,57329,0,22849,86074],[74234,59920,1,81636,68123],[3018,28202,0,48968,95292],[5280,85292,1,8538,42641],[82344,12713,0,68084,47893],[29966,91968,0,43609,16910],[31889,46076,0,35064,32137],[66786,51213,0,1891,34086],[95056,36706,1,15246,63755],[87966,53998,1,12685,8090],[45086,63959,1,70362,78781],[34652,26290,1,95064,50165],[22267,74285,1,9154,73700],[58368,36952,1,97440,48257],[26482,43258,1,48358,22333],[58361,47469,1,71528,94524],[16758,29015,0,43563,87159],[93809,298,0,18198,26358],[17230,73337,0,50051,99301],[18404,16980,1,61922,60907],[12583,2063,1,19180,49685],[11300,97886,0,11184,66753],[34101,38864,0,75368,95712],[97062,43753,0,75807,58078],[11230,66732,0,25319,68819],[47154,90662,1,15006,24737],[2251,76850,0,89671,72859],[13692,39947,0,54626,85599],[72186,22607,1,94277,23069],[6126,3014,0,24646,22668],[95682,93660,0,83382,47110],[6305,86844,1,14485,78230],[21944,28365,0,6618,30612],[22493,55287,0,18512,641],[67021,61247,1,4141,19338],[65339,33419,1,73598,91089],[46652,76989,1,79597,87036],[60707,54587,0,97702,48919],[61073,62844,1,861,24595],[43573,25117,0,43898,61098],[5900,90667,0,34251,89214],[71803,31856,1,94168,56681],[16771,22555,0,66870,74695],[41008,63342,1,72366,33395],[36367,69361,1,32075,68430],[29352,44999,1,36255,74830],[41792,75545,1,34255,31855],[78481,80594,0,85904,65012],[21706,99851,1,72092,88005],[75474,20886,0,57913,62506],[89924,47719,1,9813,70358],[67865,28332,0,87268,90737],[19173,46530,1,70824,67696],[67082,71482,0,21739,83271],[99731,25094,0,27057,70864],[4148,74422,1,24646,60231],[53783,43392,0,41381,23484],[16533,30328,1,72613,63834],[22698,66734,0,16323,76458],[12860,2112,1,23373,10959],[71523,11560,0,91618,1690],[53502,36443,0,45257,85612],[57490,83387,1,60768,78782],[64722,61283,1,13401,44114],[44621,8322,1,74246,89509],[50824,36750,1,43464,8928],[39626,17949,1,85336,87641],[2615,19247,0,24547,81120],[50136,16365,0,52927,22391],[93679,38271,1,81313,69309],[16829,52176,0,80646,49854],[47507,29921,0,13350,27870],[90152,99252,1,10257,3812],[74733,48110,1,50639,15241],[18172,80421,0,28430,27512],[61036,28861,0,60456,33740],[63448,29462,1,2472,1608],[16228,22772,0,30657,41746],[41360,14016,1,61943,18184],[83575,5204,1,75730,46818],[90971,27507,1,65023,17929],[37062,94237,1,2920,47631],[64892,3733,0,30464,6548],[73317,86562,1,23646,63534],[38574,72020,0,25119,16184],[24245,74411,0,42028,17336],[66211,97491,0,97624,6695],[25679,22017,0,19722,86268],[29367,70006,0,32768,94130],[97265,74979,1,67741,80739],[55548,30623,0,49627,76882],[87149,88718,0,86694,23006],[50643,50320,0,86519,15108],[74566,69297,0,71038,25241],[86967,21765,1,30303,61510],[8644,42431,0,65079,16392],[58460,18840,1,51381,14614],[4058,21564,0,80173,74023],[32540,35059,1,36553,5582],[4790,63067,1,84094,10579],[99364,56611,0,57037,27808],[81309,2387,0,35197,98083],[2953,31102,0,94041,26795],[88260,61864,1,84446,20916],[65784,97272,0,36203,48831],[51072,81320,0,49230,9465],[71256,96602,1,38746,131],[39210,15610,0,62070,16230],[47066,85144,0,86202,80827],[21524,80014,0,84141,50463],[49337,75738,0,20793,83213],[70834,20150,1,62917,79267],[94619,51604,0,12972,47190],[98143,58603,0,36808,79336],[24331,22002,1,84661,58355],[25492,51743,0,25205,92089],[56310,24373,1,6737,9829],[6387,86700,0,18709,56760],[24871,79114,1,69090,13016],[41986,57196,1,37237,90136],[24845,55092,0,4297,99168],[42825,32911,1,65049,38493],[11343,42592,0,6929,10970],[7543,23937,1,44339,55468],[96457,5394,1,15894,95936],[63792,33317,0,49428,21957],[56331,29242,1,50852,99420],[91732,12897,1,80336,52510],[42848,85731,0,7176,10142],[34801,96762,0,75047,27937],[56737,28135,0,4830,8619],[40336,84108,0,81603,403],[69528,87426,0,98607,88709],[19034,59011,0,6472,83790],[6127,85556,0,29328,25830],[71735,4061,1,31930,55631],[29979,84948,0,48056,7487],[68726,72019,1,57052,4586],[46984,97867,0,28909,62843],[74879,52752,0,90537,61667],[36794,22200,1,85297,38243],[14047,885,1,73059,51566],[77926,74306,0,17124,94419],[21398,36465,1,5921,37145],[25413,50376,0,60274,6316],[20167,89533,0,20390,18369],[59430,22571,0,22545,74356],[18376,41168,0,79764,16311],[47480,33092,0,6357,23042],[15688,7107,0,6153,39326],[18489,71667,0,90115,86856],[22837,60017,0,56519,1674],[16108,23563,0,5189,5903],[44046,62663,1,35458,97550],[63201,72804,0,66654,89575],[73659,80320,0,29261,40733],[72319,54259,1,2970,38906],[75673,93725,1,57459,26481],[94892,87368,1,19374,23270],[22962,8682,1,28562,65426],[90963,533,0,44950,97015],[3851,67533,1,81906,87476],[32751,17010,0,80790,68866],[45651,27558,1,20970,99554],[54328,57877,0,51538,47385],[48958,39880,1,25557,46390],[15253,46523,0,96351,75574],[19342,36102,0,69231,68937],[34340,74307,0,29323,82896],[60989,27012,1,89066,35546],[85734,87626,1,41252,22519],[48331,40636,0,85857,1632],[69552,78487,1,99011,53585],[37151,91721,1,19033,16881],[89307,74868,0,11031,75289],[75385,81425,0,99995,13609],[23630,29316,1,7191,28877],[48408,53937,1,71767,33180],[57374,51178,0,95223,69845],[87655,92412,1,98737,99358],[60201,92765,1,9425,46851],[76154,83102,0,45863,58583],[37091,15199,1,37871,88722],[63074,56729,1,18861,24830],[49093,78197,0,52382,18423],[67882,41842,0,22140,68888],[13952,10107,0,1892,81973],[63578,41063,1,55226,22645],[78651,43329,0,4182,38560],[11127,3241,0,677,88207],[97502,58583,0,81704,41731],[41241,79304,1,12598,17153],[37783,34787,0,80375,52645],[41559,61615,1,22962,74312],[40792,5444,1,55429,2273],[70807,72651,0,18099,86965],[12642,95151,1,99715,34559],[43833,13020,0,46730,55064],[95526,83676,1,56778,50520],[4822,81003,1,996,15041],[24841,50868,0,92367,38425],[62680,56887,1,51793,57801],[59717,57172,0,77264,38896],[63073,38270,1,8687,20333],[88272,12244,0,89072,85700],[95112,69519,1,99907,23328],[48737,23942,0,56091,68450],[2292,29796,1,74406,23873],[68201,12011,1,6501,28209],[48235,43057,0,18645,30511],[82934,1283,1,21691,64490],[37021,26579,1,80015,73931],[34041,59439,0,39368,42931],[9757,63136,1,63453,6357],[47807,60967,1,47372,2393],[45088,25730,0,9463,10091],[40931,53358,1,41185,34647],[89790,88901,1,16178,50664],[29528,96749,0,62100,18088],[23480,73506,1,31282,37090],[12053,98983,0,57792,48178],[99499,57944,0,51931,6179],[37960,34022,0,43685,85963],[24131,98455,1,79669,49790],[37982,26631,1,91837,99441],[46802,90842,1,37228,87403],[33704,95759,1,85460,28277],[27788,26861,1,50172,4876],[458,73056,0,49098,50802],[45327,29480,0,96484,4520],[30049,82986,1,54158,91868],[41861,43391,1,7619,99367],[36381,33634,1,85901,49294],[78025,74043,1,4570,73167],[80094,88410,1,5043,69105],[89583,30884,1,7749,95590],[49850,89153,0,44442,59497],[36492,98602,1,39088,12604],[71374,68200,0,21533,67942],[58144,34159,0,99161,55790],[73299,4185,1,21347,41797],[6924,24647,1,62125,30047],[62580,73430,0,45800,93554],[56647,22190,1,14197,43281],[9036,27772,0,15886,17467],[15476,26787,1,81378,18411],[61140,49553,1,1445,59802],[19175,48811,1,71699,61363],[82165,62666,1,52843,94226],[10590,5005,1,84934,17097],[42854,63771,1,373,45793],[16079,7962,1,32739,26819]]
veg = 0
mp = 96930
md = 84142
obj = Solution()
ret = obj.filterRestaurants(restaurants, veg, mp, md)
ans = 
