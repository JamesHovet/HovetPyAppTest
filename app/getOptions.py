import random

numbers = [i for i in range(100)]

alpha = 'abcdefghijklmnopqrstuvwxyz'

chars = [i for i in alpha]

imgNumbers = ['3097160.jpg','3097163.jpg','3257280.jpg','3435272.jpg','2988303.jpg','3257325.jpg','3257329.jpg','2899844.jpg','2988344.jpg','3257340.jpg','2899854.jpg','3097129.jpg','3420343.jpg','2899863.jpg','3257343.jpg','3097125.jpg','3420341.jpg','3257283.jpg','3420383.jpg','3257289.jpg','3097140.jpg','3257330.jpg','3257296.jpg','3257291.jpg','3257301.jpg','3257348.jpg','3257310.jpg','3420297.jpg','3097147.jpg','3097137.jpg','2988332.jpg','3257361.jpg','2899848.jpg','3420308.jpg','3420388.jpg','3257353.jpg','3257336.jpg','3097133.jpg','3257339.jpg','2988329.jpg','3420330.jpg','2988338.jpg','3097144.jpg','3420349.jpg','2988336.jpg','3097184.jpg','3257303.jpg','3257364.jpg','3420353.jpg','3097152.jpg','2988270.jpg','2988265.jpg','3097157.jpg','2988304.jpg','3173572.jpg','3431898.jpg','3420271.jpg','3257359.jpg','2899849.jpg','2988268.jpg','2988278.jpg','3420279.jpg','2988277.jpg','3420351.jpg','3420382.jpg','3160012.jpg','3257318.jpg','3257308.jpg','2988351.jpg','3257357.jpg','2988325.jpg','2988281.jpg','3420289.jpg','2899847.jpg','3420311.jpg','3097148.jpg','3097121.jpg','3097161.jpg','3420364.jpg','3420345.jpg','3097141.jpg','3420358.jpg','2988292.jpg','2899862.jpg','3097166.jpg','2988335.jpg','2988321.jpg','3431798.jpg','3257333.jpg','3257345.jpg','3097177.jpg','3257370.jpg','2988366.jpg','3097154.jpg','2988346.jpg','2899852.jpg','3097162.jpg','3097132.jpg','3097126.jpg','3257326.jpg','2988314.jpg','3101517.jpg','3097142.jpg','2988299.jpg','3420346.jpg','3257276.jpg','3420301.jpg','2988307.jpg','3420267.jpg','3257316.jpg','3257322.jpg','3097136.jpg','3257281.jpg','3097146.jpg','3468642.jpg','2899867.jpg','3420298.jpg','3420378.jpg','2988324.jpg','2988356.jpg','3420288.jpg','3257313.jpg','3420255.jpg','3257277.jpg','3472880.jpg','3257344.jpg','3257324.jpg','3257300.jpg','2988367.jpg','2899861.jpg','2988358.jpg','3420291.jpg','2899829.jpg','3257312.jpg','2899851.jpg','3420286.jpg','3097150.jpg','3097143.jpg','2988287.jpg','3097183.jpg','3420258.jpg','3097122.jpg','2988323.jpg','3420265.jpg','2988269.jpg','2988264.jpg','3257346.jpg','3257302.jpg','3420266.jpg','3420280.jpg','3097196.jpg','3097135.jpg','3257307.jpg','3257337.jpg','2988300.jpg','3097192.jpg','3257314.jpg','3097180.jpg','2899864.jpg','3097165.jpg','3097155.jpg','3420273.jpg','2988312.jpg','3420324.jpg','3257327.jpg','3097124.jpg','2988353.jpg','3257334.jpg','3608174.jpg','3257349.jpg','3097182.jpg','3097130.jpg','3097149.jpg','3097179.jpg','3097120.jpg','3097128.jpg','3097117.jpg','3430563.jpg','3257315.jpg','3556335.jpg','3431255.jpg','3431978.jpg','3420276.jpg','2988274.jpg','3097127.jpg','3420379.jpg','3420281.jpg','3257342.jpg','2988313.jpg','3257294.jpg','3420376.jpg','3257323.jpg','2988348.jpg','3420332.jpg','3257282.jpg','3420269.jpg','2899850.jpg','2988276.jpg','3420340.jpg','3257290.jpg','2988365.jpg','2899859.jpg','3257287.jpg','3420268.jpg','3257298.jpg','3257365.jpg','3257352.jpg','3257286.jpg','2899868.jpg','3257362.jpg','3097188.jpg','3431880.jpg','3097171.jpg','3420326.jpg','2988319.jpg','3097168.jpg','3420320.jpg','2899857.jpg','3257331.jpg','3257293.jpg','3097131.jpg','3420277.jpg','3420357.jpg','3257354.jpg','3097181.jpg','3608158.jpg','3459667.jpg','3097190.jpg','3420347.jpg','2988361.jpg','3257297.jpg','3420312.jpg','3097195.jpg','2988286.jpg','2988267.jpg','2988340.jpg','3097151.jpg','3420374.jpg','3097156.jpg','3097119.jpg','2988347.jpg','3257367.jpg','3420287.jpg','2988305.jpg','2988297.jpg','3431913.jpg','3257311.jpg','3097134.jpg','3420296.jpg','3131665.jpg','3257328.jpg','3420295.jpg','3257366.jpg','3257341.jpg','3282755.jpg','3605273.jpg','3257360.jpg','3097185.jpg','2988280.jpg','3097118.jpg','3420369.jpg','3097167.jpg','3097173.jpg','2988357.jpg','2988298.jpg','3257369.jpg','2988345.jpg','3257295.jpg','2988306.jpg','2988279.jpg','3097189.jpg','3097198.jpg','3257320.jpg','3097123.jpg','2988341.jpg','2899858.jpg','3257309.jpg','3257288.jpg','3257356.jpg','3257285.jpg','3097175.jpg','2988296.jpg','2988315.jpg','3097145.jpg','2988285.jpg','2988342.jpg','3257306.jpg','3257363.jpg','3257358.jpg','3108573.jpg','3257292.jpg','3097164.jpg','3420283.jpg','2988349.jpg','2988293.jpg','3097172.jpg','3097138.jpg','2988288.jpg','2988328.jpg','3097186.jpg','3420373.jpg','2899866.jpg','2988343.jpg','2988273.jpg','2988364.jpg','3257304.jpg','3420360.jpg','2899846.jpg','3257305.jpg','3257278.jpg','3097191.jpg','3097176.jpg','3431236.jpg','2988271.jpg','3257274.jpg','2988354.jpg','3097178.jpg','2988295.jpg','3097158.jpg','3420366.jpg','3257347.jpg','3257321.jpg','3282758.jpg','3420307.jpg','3257368.jpg','2988311.jpg','3420261.jpg','3097170.jpg','3097193.jpg','2988362.jpg','2988360.jpg','2988310.jpg']


def returnRandomInNumbers():
    return numbers[random.randrange(0,100)]

def returnRandomInChars():
    return chars[random.randrange(0,26)]

def returnRandomInImgNumbers():
    return imgNumbers[random.randrange(0,len(imgNumbers))][:-4]

def n():
    return imgNumbers[random.randrange(0,len(imgNumbers))][:-4]