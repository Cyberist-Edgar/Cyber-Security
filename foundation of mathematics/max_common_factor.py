def max_common_factor(num1, num2):
    """辗转相除法计算最大公因数"""
    min_num = min(num1, num2)
    max_num = max(num1, num2)
    while min_num:
        # 注意不要先把min_num, max_num进行改变，否则赋值的时候不对
        max_num, min_num = min_num, max_num % min_num
    return max_num


question_list = [(166, 332), (984, 1038), (1124, 1213), (1281, 2019), (1338, 2018),
                 (2020, 313), (202003, 1601), (20200310, 1231), (1301, 1373), (1601, 1681)]

for i in question_list:
    print(f"{i[0]}, {i[1]}的最大公因数是： ", max_common_factor(*i))



