import string

def decode(x):
  for i in range(97):
    calculated = pow(i, 101, 97)
    if calculated == x:
      return i
  return 0

def string_to_utf8_codes(s):
    return [ord(c) for c in s]

# Przykład użycia
s = '''
XP�WE5,6_A_"]HV/0OY	FP
&Q$@XO%I	  (GS]O=3=DX	$()'I$L>\<CLA
7%GXF
-.C0NO3H#35X:E�3
SA
H_W;:8@>
+`^QY^.]
P
Z
0X2$!U4BHRT^,1'`()Z^T
3GU0(=D'@�W9_L>*/3" &Q	G?78_=T["=
)�MESOJ-RN'<C-`I)\B,M\(,'I@<7TI&SO	H	L_E/PTS<RP
6=>:'^[/I4)&Q	0)<A1�0)7I"O"QK=O	
4\* E)=	:U_UY	[XYA\;!LS]1<T5[/2M2R,\KL>$!E5(*(
7)N*CNKJ?^A5@*3
8YW2H[/V?0N[F
4`2,0NIWT22Z^Q^_
Q]^1]U=(�VAX2/P)0".\MO%
F4
N,QKXHK:8 `G9B&[Q)<C)W&A
=
0Y`\ [F3K*%
3N'N] ZB%0	!D.<CYBR$+
0$C5J@<7TX*%@T#B2[2V@#)5.]HKV<W:J*A+
5J\$E2368K,DU&A^3R6_$B(
(S4
25VD.
QP!OTI	X$-68
&=
=E.-)5I@>+E%2
P
JS8S]^M`9#'%;D
S4UY	78V=XGV/Z RJ9[F3J^0_L>]F-N,HV)J*	GS 9Y^��K.UC0RJS!K$
4>:
'''

def convert_and_shift(indexes):
    # List to hold the shifted strings
    shifted_strings = []

    # narrowed down from 0-99
    for i in range(18,19):
        # Add i to every index
        shifted_indexes = [((index) + i) for index in indexes]

        # Convert back to string, taking care of bounds
        shifted_string = ''.join(string.printable[index % 97] for index in shifted_indexes)

        # Add the shifted string to the list
        shifted_strings.append(shifted_string)

    return shifted_strings

utf8_codes = string_to_utf8_codes(s)
results_before_shift = []
num_to_carry = 0
my_dict = {
  #',': 'l',
}
#c_values = [1, 49, 65, 73, 39, 81, 14, 85, 54, 68, 53, 89, 15, 7, 13, 91, 40, 27, 46, 34, 37, 75, 38, 93, 66, 56, 18, 52, 87, 55, 72, 94, 50, 20, 61, 62, 21, 23, 5, 17, 71, 67, 88, 86, 69, 19, 64, 95, 2, 33, 78, 28, 11, 9, 30, 26, 80, 92, 74, 76, 35, 36, 77, 47, 3, 25, 42, 10, 45, 79, 41, 31, 4, 59, 22, 60, 63, 51, 70, 57, 6, 84, 90, 82, 8, 44, 29, 43, 12, 83, 16, 58, 24, 32, 48, 96]
c_values=[66]
for c in c_values:
    print(c)
    for code in utf8_codes:
        partial_result = (((decode(code) - num_to_carry)) * c) % 97
        num_to_carry = code
        results_before_shift.append(partial_result)

    results = convert_and_shift(results_before_shift)
    #print(utf8_codes)
    #print(result_before_shift)
    #print(len(utf8_codes))
    with open('results7.txt', 'w') as file:
        for text in results:
            for key, value in my_dict.items():
                text = text.replace(key, value)
            file.write(text)
