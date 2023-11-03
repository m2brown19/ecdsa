import unittest
import ecdsa #file name


class MyTestCase(unittest.TestCase):

    #Test finite field add with larger field size than result
    def test_finite_add(self):
        result = ecdsa.finite_add( 2, 3, 10)
        self.assertEqual(result, 5)

    # Test finite field add with same field size as result
    def test_finite_add_same_size(self):
        result = ecdsa.finite_add( 5, 5, 10)
        self.assertEqual(result, 0)

    # Test finite field add with smaller field than result
    def test_finite_add_smaller_size(self):
        result = ecdsa.finite_add( 5, 5, 8)
        self.assertEqual(result, 2)

    #Test finite field mult with larger field size than result
    def test_finite_mult(self):
        result = ecdsa.finite_mult( 5, 3, 10)
        self.assertEqual(result, 5)

    # Test finite field mult with same field size as result
    def test_finite_mult_same_size(self):
        result = ecdsa.finite_mult( 5, 5, 25)
        self.assertEqual(result, 0)

    # Test finite field mult with smaller field than result
    def test_finite_mult_smaller_size(self):
        result = ecdsa.finite_mult( 5, 5, 30)
        self.assertEqual(result, 25)

#EXPONENTIATION
    #Test finite field exp with larger field size than result
    def test_finite_exp(self):
        result = ecdsa.finite_exp( 2, 4, 40)
        self.assertEqual(result, 16)

    # Test finite field exp with same field size as result
    def test_finite_exp_same_size(self):
        result = ecdsa.finite_exp( 2, 4, 16)
        self.assertEqual(result, 0)

    # Test finite field exp with smaller field than result
    def test_finite_exp_smaller_size(self):
        result = ecdsa.finite_exp( 2, 4, 10)
        self.assertEqual(result, 6)

    def test_sub_no_additive_inv(self):
        result = ecdsa.finite_sub( 15, 10, 17)
        self.assertEqual(result, 5)

    def test_sub_with_additive_inv(self):
        result = ecdsa.finite_sub( 15, 10, 17)
        self.assertEqual(result, 5)

    def test_sub_with_additive_inv_neg(self):
        result = ecdsa.finite_sub( 10, 15, 17)
        self.assertEqual(result, 12)

    def test_sub_with_additive_inv_max_neg_diff(self):
        result = ecdsa.finite_sub( 0, 16, 17)
        self.assertEqual(result, 1)

    def test_sub_with_additive_inv_max_neg_closer(self):
        result = ecdsa.finite_sub( 5, 16, 17)
        self.assertEqual(result, 6)

    def test_sub_with_additive_inv_same_nums(self):
        result = ecdsa.finite_sub( 16, 16, 17)
        self.assertEqual(result, 0)

    def test_sub_neg_neg(self):
        result= ecdsa.finite_sub(-5, -10, 17)
        self.assertEqual(result, 5)

    def test_sub_neg_neg_needing_switch(self):
        result= ecdsa.finite_sub(-5, -1, 17)
        self.assertEqual(result, 13)

#ADDITIVE SOLN
    # def test_sub_with_additive_inv(self):
    #     result = ecdsa.additive_finite_sub( 15, 10, 17)
    #     self.assertEqual(result, 5)
    #
    # def test_sub_with_additive_inv_neg(self):
    #     result = ecdsa.additive_finite_sub( 10, 15, 17)
    #     self.assertEqual(result, 12)
    #
    # def test_sub_with_additive_inv_max_neg_diff(self):
    #     result = ecdsa.additive_finite_sub( 0, 16, 17)
    #     self.assertEqual(result, 1)
    #
    # def test_sub_with_additive_inv_max_neg_closer(self):
    #     result = ecdsa.additive_finite_sub( 5, 16, 17)
    #     self.assertEqual(result, 6)
    #
    # def test_sub_with_additive_inv_same_nums(self):
    #     result = ecdsa.additive_finite_sub( 16, 16, 17)
    #     self.assertEqual(result, 0)
#DIVIDING
    def test_div_larger(self):
        result = ecdsa.finite_div( 13, 5, 17)
        self.assertEqual(result, 6) #Verify by saying result * a (the bottom) = top. then mod it.

    def test_div_same(self):
        result = ecdsa.finite_div( 13, 13, 17)
        self.assertEqual(result, 1)

    def test_div_smaller(self):
        result = ecdsa.finite_div( 2, 10, 17)
        self.assertEqual(result, 7)

    def test_div_smaller_again(self):
        result = ecdsa.finite_div( 1, 16, 17)
        self.assertEqual(result, 16)

    def test_add_diff_pts(self):
        result = ecdsa.add_diff_points( (12, 31), (29, 31), 43)
        self.assertEqual(result, (2,12))

    def test_add_diff_pts_2(self):
        result = ecdsa.add_diff_points( (37, 36), (29, 31), 43)
        self.assertEqual(result, (13,22))

    def test_add_diff_0(self):
        result = ecdsa.add_diff_points( 0, (29, 31), 43)
        self.assertEqual(result, (29,31))

    def test_add_diff_00(self):
        result = ecdsa.add_diff_points( (29, 31), 0, 43)
        self.assertEqual(result, (29,31))

    def test_add_diff_pts_3(self):
        result = ecdsa.add_diff_points( (20, 3), (13, 22), 43)
        self.assertEqual(result, (20,40))

    def test_add_diff_pts_4(self):
        result = ecdsa.add_diff_points( (7, 36), (2, 12), 43)
        self.assertEqual(result, (2,31))

    def test_add_diff_pts_infin_case(self):
        result = ecdsa.add_diff_points( (2, 12), (2, 31), 43)
        self.assertEqual(result, 0)

    def test_add_diff_pts_infin_case2(self):
        result = ecdsa.add_diff_points( (37, 7), (37, 36), 43)
        self.assertEqual(result, 0)

    def test_add_diff_pts_infin_case3(self):
        result = ecdsa.add_diff_points( (42, 7), (42, 36), 43)
        self.assertEqual(result, 0)

    def test_add_diff_pts_infin_case4(self):
        result = ecdsa.add_diff_points( (21, 18), (21, 25), 43)
        self.assertEqual(result, 0)

#SAME PTS TEST ADD
    def test_add_same_0(self):
        result = ecdsa.add_same_points( 0, 0, 43)
        self.assertEqual(result, 0)

    def test_add_same_pts(self):
        result = ecdsa.add_same_points( (12, 31), (12, 31), 43)
        self.assertEqual(result, (42, 36))

    def test_add_same_pts2(self):
        result = ecdsa.add_same_points( (7, 36), (7, 36), 43)
        self.assertEqual(result, (21, 25))

    def test_add_same_pts3(self):
        result = ecdsa.add_same_points( (42, 36), (42, 36), 43)
        self.assertEqual(result, (40, 25))

#TEST POWERS FUNCTION
    def test_add_pows(self):
        result = ecdsa.find_powers_2( 21)
        self.assertEqual(result, [16, 4, 1])

    def test_add_pows2(self):
        result = ecdsa.find_powers_2( 32)
        self.assertEqual(result, [32])

    def test_add_pows3(self):
        result = ecdsa.find_powers_2( 15)
        self.assertEqual(result, [8, 4, 2, 1])

#TEST MULTIPLY
    def test_mult(self):
        result = ecdsa.mult_points( 1, (12, 31), 43)
        self.assertEqual(result, (12, 31))

    def test_mult2(self):
        result = ecdsa.mult_points( 2, (12, 31), 43)
        self.assertEqual(result, (42, 36))

    def test_mult3(self):
        result = ecdsa.mult_points( 3, (12, 31), 43)
        self.assertEqual(result, (38, 22))

    def test_mult4(self):
        result = ecdsa.mult_points( 4, (12, 31), 43)
        self.assertEqual(result, (40, 25))

    def test_mult5(self):
        result = ecdsa.mult_points( 5, (12, 31), 43)
        self.assertEqual(result, (29, 31))

    def test_mult6(self):
        result = ecdsa.mult_points( 6, (12, 31), 43)
        self.assertEqual(result, (2, 12))

    def test_mult21(self):
        result = ecdsa.mult_points( 21, (12, 31), 43)
        self.assertEqual(result, (37, 7))

    def test_mult1000(self):
        result = ecdsa.mult_points( 1000, (12, 31), 43)
        self.assertEqual(result, (20, 3))

    def test_mult1024(self):
        result = ecdsa.mult_points( 1024, (12, 31), 43)
        self.assertEqual(result, (12, 31))

    def test_mult3000(self):
        result = ecdsa.mult_points( 3000, (2, 31), 43)
        self.assertEqual(result, (25, 18))

    def test_multinfin(self):
        result = ecdsa.mult_points( 1054, (12, 31), 43)
        self.assertEqual(result, 0)

    def test_multinfin_diff_pt(self):
        result = ecdsa.mult_points( 248, (2, 31), 43)
        self.assertEqual(result, 0)

    def test_mult_recur_fn1(self):
        result = ecdsa.add_pts_recursively( 1, (12, 31), 43)
        self.assertEqual(result, (12, 31))

    def test_mult_recur_fn2(self):
        result = ecdsa.add_pts_recursively( 2, (12, 31), 43)
        self.assertEqual(result, (42, 36))

    def test_mult_recur_fn4(self):
        result = ecdsa.add_pts_recursively( 4, (12, 31), 43)
        self.assertEqual(result, (40, 25))

    def test_mult_recur_fn8(self):
        result = ecdsa.add_pts_recursively( 8, (12, 31), 43)
        self.assertEqual(result, (20, 3))

    def test_mult_recur_fn16(self):
        result = ecdsa.add_pts_recursively(16, (12, 31), 43)
        self.assertEqual(result, (13, 21))

    def test_mult_recur_fn32(self):
        result = ecdsa.add_pts_recursively( 32, (12, 31), 43)
        self.assertEqual(result, (12, 31))

    def test_mult_recur_fn64(self):
        result = ecdsa.add_pts_recursively( 64, (12, 31), 43)
        self.assertEqual(result, (42, 36))

    def test_mult_recur_fn128(self):
        result = ecdsa.add_pts_recursively( 128, (12, 31), 43)
        self.assertEqual(result, (40, 25))

    def test_mult_recur_fn256(self):
        result = ecdsa.add_pts_recursively( 256, (12, 31), 43)
        self.assertEqual(result, (20, 3))

    def test_mult_recur_fn512(self):
        result = ecdsa.add_pts_recursively( 512, (12, 31), 43)
        self.assertEqual(result, (13, 21))

    def test_mult_recur_fn1024(self):
        result = ecdsa.add_pts_recursively( 1024, (12, 31), 43)
        self.assertEqual(result, (12, 31))

    def test_mult_recur_fn2048(self):
        result = ecdsa.add_pts_recursively( 2048, (12, 31), 43)
        self.assertEqual(result, (42, 36))

    def test_mult_recur_mult29(self):

        self.assertEqual((34,40), ecdsa.mult_points(29, (25, 25), 43))

if __name__ == '__main__':
    unittest.main()
