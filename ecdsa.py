#Michael Brown (mjb4us)
#Implement ECDSA
#@Source: https://pynative.com/python-random-randrange/#:~:text=Use%20a%20random.,8%20%2C9%2C%2010%5D.

#IMPORTS

'''
QUESTIONS:
- is the math mod for standard + and - okay?
'''

#@param int x: num to add
# @param int y: num to add
#@param field_size: the finite field size
#@return: the result of adding these nums in finite field
import random
import sys
from random import shuffle




def finite_add(x, y, field_size):

    return ( x + y ) % field_size

# @param int x: num to mult
# @param int y: num to mult
# @param field_size: the finite field size
# @return: the result of multiplying these nums in finite field
def finite_mult( x, y, field_size):
    return (x * y) % field_size

# @param int base: base num
# @param int exp: exponent
# @param field_size: the finite field size
# @return: the result of exponentiation these nums in finite field
def finite_exp( base, exp, field_size):
    return (base ** exp) % field_size



def finite_sub( x, y, field_size):

    #if (x < 0) & (y < 0):
     #   return finite_sub(y, -1*x, field_size) #-x-(-y) = y - x

    sub_res = x - y
    #IF NEGATIVE, then do the following
    if (sub_res < 0):
        sub_res = field_size - ((-1* sub_res) % field_size) #If result of subtraction was neg, then fix it and mod.
        return sub_res
    return sub_res % field_size

# @param int num: start num
# @param field_size: the finite field size
# @return: the additive inverse
def add_inverse(num, field_size):
    inv_num = field_size - num #-x = p -x
    return inv_num

#DO NOT GIVE IT A NEGATIVE NUM. IF I DO, I NEED TO CHANGE IT OR USE OTHER SUBTRACT
def additive_finite_sub( first, second, field_size):
    #if first is neg, do add inv
    inv_first = 0
    inversed_num = 0
    correct_first = 0
    correct_second = 0

    #-x
    # if first < 0:
    #     inv_first = add_inverse(first, field_size)
    # if second > 0:
    #
    #     correct_second = add_inverse( second, field_size) #had -y
    inversed_num = add_inverse( second, field_size)
    return (first + inversed_num) % field_size

#top / bot
def finite_div( top, bot, field_size):
    result = (top * (bot ** (field_size - 2)) ) % field_size
    return result



#@param pt1: tuple point
#@param pt2: tuple point 2
#@param field_size: size of field
def add_diff_points( pt1, pt2, field_size):
    # HANDLE PT PLUS 0
    if (pt1 == 0):
        return pt2
    if (pt2 == 0):
        return pt1

    #given two points, get x and y vals
    x1 = pt1[0]
    y1 = pt1[1]
    x2 = pt2[0]
    y2 = pt2[1]

    if (is_reflection( pt1, pt2, 43)):
        return 0 #return 0,0 if it is a reflection
    # m = (y2 - y1) / (x2 - x1)


    numerator = finite_sub( y2, y1, field_size) #y2 - y1
    denom = finite_sub( x2, x1, field_size) #x2- x1
    m = finite_div( numerator, denom, field_size) #(y2 - y1) / (x2-x1)

    #SHORTCUT
    #x3 = (m ** 2) - x1 - x2
    partX3 = finite_exp( m , 2, field_size) # m ** 2
    partX3 = finite_sub( partX3, x1, field_size) #(m ** 2) - x1
    x3 = finite_sub( partX3, x2, field_size) #(m ** 2) - x1 - x2
    #y3 = ( m * (x1 - x3) ) - y1
    partY3 = finite_sub( x1, x3, field_size) #x1 - x3
    partY3 = finite_mult( m, partY3, field_size) #( m * (x1 - x3) )
    y3 = finite_sub( partY3, y1, field_size) #( m * (x1 - x3) ) - y1

    return (x3, y3)

#TODO - HANDLE INFINITY!!!
#order is o the order here!
def is_reflection( pt1, pt2, field_size):
    x1 = pt1[0]
    y1 = pt1[1]
    x2 = pt2[0]
    y2 = pt2[1]
    if x1 == x2:
        result = finite_add( y1, y2, field_size)
        if (result == 0): #reflection:y1+y2 = field size p
            return True
        else:
            return False
    else:
        return False


#@param pt1: tuple point
#@param pt2: tuple point 2
#@param field_size: size of field
def add_same_points( pt1, pt2, field_size):
    if (pt1 == 0):
        return 0 #both points are the same... so 0 plus 0 is 0

    #given two same points, get x and y vals
    x1 = pt1[0]
    y1 = pt1[1]
    x2 = pt2[0]
    y2 = pt2[1]



    #m = (3 * (x1**2)) / (2 * y1)
    top = finite_exp( x1, 2, field_size) #x1 ** 2
    top = finite_mult( 3, top, field_size) # 3 * x1 **2
    bot = finite_mult( 2, y1, field_size) #2 * y1
    m = finite_div( top, bot, field_size)

    # SHORTCUT
    # x3 = (m ** 2) - x1 - x2
    partX3 = finite_exp( m, 2, field_size)  # m ** 2
    partX3 = finite_sub( partX3, x1, field_size)  # (m ** 2) - x1
    x3 = finite_sub( partX3, x2, field_size)  # (m ** 2) - x1 - x2
    # y3 = ( m * (x1 - x3) ) - y1
    partY3 = finite_sub( x1, x3, field_size)  # x1 - x3
    partY3 = finite_mult(m, partY3, field_size)  # ( m * (x1 - x3) )
    y3 = finite_sub( partY3, y1, field_size)  # ( m * (x1 - x3) ) - y1

    return (x3, y3)


def mult_points( k, pt, field_size):
    #it is k * Point P
    numsAddingToK = find_powers_2( k) #get list of the powers adding to k

    half_computed = []

    for num in numsAddingToK: #for each power, divide by two till get 1
        result = add_pts_recursively( num, pt, field_size)
        half_computed.append(result) #add point to this

    #print(half_computed)
    got_result = False
    count_of_infin_results = 0 #use this as a counter to stop trying to multiply
    while (got_result != True):

        pt1 = half_computed[0] #Get start point
        for i in range(1, len(half_computed)):

            pt2 = half_computed[i]
            #if pts same, handle it
            if pt1 == pt2:
                #print("SAME PT ADD")
                #print("pt1:", pt1, "+ pt2: ", pt2)
                pt1 = add_same_points( pt1, pt2, field_size)

                #print(pt1)
            #if pts diff, handle it
            else:
                #print("DIFF PT ADD")
                #print("pt1:", pt1, "+ pt2: ", pt2)
                pt1 = add_diff_points( pt1, pt2, field_size)
                #print(pt1)
                if (pt1 == 0):
                    #RESTART THE ALGORITHM if pointss add to 0! Shuffle points
                    #SHUFFLE LIST AND BREAK FOR LOOP
                    #print("PT! EQUALS 0, increment count infin. count infin equals:", count_of_infin_results)
                    count_of_infin_results += 1

                    shuffle(half_computed)
                    break

        #AFTER ADDING POINTS, CHECK WHAT RESULT IS
        if (pt1 != 0):
            return pt1

        #return 0 if tried 7 times
        if (pt1 == 0) &  (count_of_infin_results >= 7):
            return pt1


        #print("Done adding, no return: ", pt1)



     #pt1 gets updated with total
    #return add_pt_list_recursive(self, half_computed, field_size)

#Take list of points and add them recursively
# def add_pt_list_recursive(self, pt_list, field_size):
#     if (len(pt_list) == 1):
#         return pt_list[0]
#     else:
#         nbr_pts = len(pt_list)
#         if nbr_pts % 2 == 0:
#             #even, evenly split pt list
#             half_nbr_pts = int(nbr_pts / 2) #upper half index .
#             left = add_pt_list_recursive(self, pt_list[0 : (half_nbr_pts - 1)], field_size)
#             right = add_pt_list_recursive(self, pt_list[half_nbr_pts : ], field_size)
#
#             #handle if diff
#             if left == right:
#                 return add_same_points(self, left, right, field_size)
#             else:
#                 return add_diff_points(self, left, right, field_size)
#
#         else:
#             half_nbr_pts = int(nbr_pts / 2) #TODO ------------- CHECK THS IS HALF. CHECK  I GET ALLL PTS
#             left = add_pt_list_recursive(self, pt_list[0: (half_nbr_pts )], field_size)
#             right = add_pt_list_recursive(self, pt_list[half_nbr_pts:], field_size)
#
#             # handle if diff
#             if left == right:
#                 return add_same_points(self, left, right, field_size)
#             else:
#                 return add_diff_points(self, left, right, field_size)




#TODO - do i need to use field size for some of this computation?
#given a num, i can add points recursively
#SUPPOSED TO BE GIVEN A POWER OF TWO!!
def add_pts_recursively( num, pt, field_size):
    if (num == 1):
        return pt

    else:
        #divide num in two. compute both halves. then add tofether
        leftNum = num / 2
        rightNum = num / 2

        #check what kind of add i can do
        left = add_pts_recursively( leftNum, pt, field_size)
        right = add_pts_recursively( rightNum, pt, field_size)
        return add_same_points( left, right, field_size)


def multipl_inv(num, p):
    return ((num ** (p-2) ) % p )


#TODO - for now, do not use field size for this
#max range i is 11
def find_powers_2( k):
    i = 11
    powers = []

    while k != 0:
        num = 2 ** i
        if (k - num >= 0):
            powers.append(num)
            k = k - num
        i = i -1
    return powers



#TODO #FIX SUBTRACTION!! edge cases

try:
    if (sys.argv[1] == "userid"):
        print("mjb4us")

    if (sys.argv[1] == "genkey"):
        order = int(sys.argv[3]) #order
        p = int(sys.argv[2]) #prime mod
        base_x = int(sys.argv[4])
        base_y = int(sys.argv[5])


        looking_for_key = True
        while (looking_for_key == True):
            d = random.randint(1, order - 1) #key gen until get a real pub key.

            pubKey = mult_points( d, (base_x, base_y), p) #p works not order
            if (pubKey != 0):
                print(d)
                print(pubKey[0])
                print(pubKey[1])
                looking_for_key = False
                break

    if sys.argv[1]  == "sign":
        order = int(sys.argv[3])  # order
        p = int(sys.argv[2])  # prime mod
        base_x = int(sys.argv[4])
        base_y = int(sys.argv[5])
        d = int(sys.argv[6])
        h = int(sys.argv[7])
        #if r or s == 0, restart!
        #R = k * G
        r = 0
        s = 0

        looking_for_signed = True
        while (looking_for_signed == True):
            #GENERATE k -- OTP
            k = random.randint(1, order - 1)


            R = mult_points(k, (base_x, base_y), p) #k *G mod p
            if (R != 0):
                r = R[0] #Get r if R is not 0

                if (r != 0):
                    k_inv =  multipl_inv(k, order)

                    #compute s
                    partS = finite_mult(r, d, order ) #r *d
                    partS = finite_add(h, partS, order) #h plus that
                    partS = finite_mult(k_inv, partS, order)
                    s = partS % order

                    #VERIFY check
                    #checked = ( k_inv * (h + r * d) ) % order
                    #print("CHECKED:", checked)

                    #print("signature part s :", s)

                    if (s != 0):
                        looking_for_signed = False

        print(r)
        print(s)




    if (sys.argv[1] == "verify"):
        order = int(sys.argv[3])  # order
        p = int(sys.argv[2])  # prime mod
        base_x = int(sys.argv[4])
        base_y = int(sys.argv[5])
        pub_x = int(sys.argv[6])
        pub_y = int(sys.argv[7])
        r = int(sys.argv[8])
        s = int(sys.argv[9])
        h = int(sys.argv[10])

        #due to the derivation, verify with the formula in slides to find R
        # R = s_inv * h (*) G (+) s_inv * r (X) Q
        s_inv = multipl_inv(s, order)

        partEqn = finite_mult(s_inv, h, order) #s inv * h
        #print("modded: s inv * h =", partEqn)

        partEqn = mult_points(partEqn, (base_x, base_y), p) #s_inv * h (*) G
        #print("BASEPOINT: ", base_x, base_y)
        #print("base point times left side: ", partEqn)

        otherPartEqn = finite_mult(s_inv, r, order)

        #print("modded: s inv * r =", otherPartEqn)
        otherPartEqn = mult_points(otherPartEqn, (pub_x, pub_y), p) #s_inv * r (X) Q
        #print("pub key point times right side: ", otherPartEqn)

        if (partEqn != otherPartEqn):
            R = add_diff_points(partEqn, otherPartEqn, p)
            #print("R then (r, s):", R, r, s)
            # print(R == (r, s))
            print(R[0] == r)
        else:
            R = add_same_points(partEqn, otherPartEqn, p)
            #print("R then (r, s):", R, r, s)
            #print(R == (r, s))
            print(R[0] == r)


        #CHECK WORK WITH SIMPLER OPS
        # leftPart = (s_inv * h) #maybe this needs to be done without modding?
        #
        # # print("s inv * h =", leftPart)
        # leftPart = mult_points(leftPart, (base_x, base_y), p) # try p if not?
        #
        #
        # trialorig = mult_points(600, (base_x, base_y), p)  # try p if not?
        # trialone = mult_points(30, (base_x, base_y), p)  # try p if not?
        #
        # print(trialorig, trialone)
        #
        # rightPart = (s_inv * r)
        # # print("s inv * r =", rightPart)
        # rightPart = mult_points(rightPart, (pub_x, pub_y), p) #try p if not?
        # print("right side", rightPart)
        # if (trialorig != rightPart):
        #     R = add_diff_points(trialorig, rightPart, p)
        #
        #     print(add_diff_points(trialorig, rightPart, p))
        #     print(add_diff_points(trialone, rightPart, p))
        #     # print("R then (r, s):", R, r, s)
        #     #print(R == (r, s))
        #     print(R[0] == r)
        # else:
        #     R = add_same_points(trialorig, rightPart, p)
        #     # print("R then (r, s):", R, r, s)
        #     #print(R == (r, s))
        #     print(R[0] == r)



except:
    print(False)
