'''
Viết chương trình đảo ngược từ ký tự thường sang ký tự hoa và từ ký tự hoa sang ký tự thường trong một chuỗi.
'''

# str = "abc ADD 12fG"
# print(str.swapcase())





'''
Viết chương trình tìm ra ký tự lớn nhất và ký tự nhỏ nhất của một chuỗi nhập từ bán phím.
Input: "abc AcdE z"
Output:
- Lớn nhất: z
- Nhỏ nhất: A
'''
# str = input('mời nhập chuỗi: ')
# maxx = 'z'
# minn = 'A'
# smalll = []
# for i in range(len(str)):
#     char = str[i]
#     val_char = (ord(char))
#     smalll.append(val_char)
# char_smallest = chr(min(smalll))
# char_largest = chr(max(smalll))
# print ('Lớn nhất:', char_largest)
# print ('Nhỏ nhất: ', char_smallest)


'''
Viết chương trình sinh ra một chuỗi từ 2 ký tự đầu và 2 ký tự cuối trong chuỗi được nhập vào,
nếu độ dài chuỗi nhỏ hơn 2 thì in ra chuỗi rỗng.
'''
# print('chương trình sinh ra một chuỗi từ 2 ký tự đầu và 2 ký tự cuối')
# str = input('mời nhập chuỗi: ')
# if len(str)<= 2:
#     print('  ')
# else:
#     print(str[0 :2] + str[-2 :])
'''
Viết chương trình để xóa bỏ các ký tự có chỉ số là số lẻ trong một chuỗi.
'''
# str = input('mời nhập chuỗi: ')
# print(str[1::2])


''':key Viết chương trình để xóa bỏ ký tự thứ m trong chuỗi không rỗng, với m là số không âm, nhập từ bàn phím.
Input:
 - s = "0123456789"
 - m = 4
Output: "012456789"
'''
# str = input('input string: ')
# m = int(input('index_del: '))
# l = list(str)
# for i in range(len(str)):
#     if i == m:
#         del(l[i])
#         str = ''.join(l)
# print(str)

'''
Viết chương trình thay thế tất cả các ký tự giống ký tự đầu tiên của một Chuỗi thành $
'''
# str = input('moi nhap chuoi: ')
# char = str[0]
# re_pla = str.replace(char,'$')
# print(re_pla)