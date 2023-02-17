morse_dic = {"a": ".-",	"b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....",
             "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.",
             "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-",
             "y": "-.--", "z": "--..", "0": "-----", "1": ".----", "2":	"..---", "3": "...--", "4":	"....-",
             "5": ".....", "6":	"-....", "7": "--...", "8":	"---..", "9": "----.", ".":	".-.-.-", ",": "--..--",
             "?": "..--..",	"'": ".----.", "!":	"-.-.--", "/": "-..-.", "(": "-.--.", ")": "-.--.-", "&": ".-...",
             ":": "---...",	";": "-.-.-.", "=":	"-...-", "+": ".-.-.", "-":	"-....-", "_": "..--.-", '"': ".-..-.",
             "$": "...-..-", "@": ".--.-.", "¿": "..-.-", "¡": "--...-"}

"""encode"""
encode = input("what do you want to convert to morse? ").lower()

encode_arr = [morse_dic[x] for x in encode]
# print(encode_arr)

"""String join() examples"""
separator = ", "

# .join() with lists
numList = ["1", "2", "3", "4"]
# print(separator.join(numList))

# .join() with tuples
numTuple = ("1", "2", "3", "4")
# print(separator.join(numTuple))

# .join() with sets - Set items are unordered, unchangeable, and do not allow duplicate values.
numSet = {"2", "1", "3"}
# print(type(numSet))
# print(separator.join(numSet))

# .join() with dictionaries
numDict = {'mat': 1, 'that': 2}
# print(separator.join(numDict))

s1 = "abc"
s2 = "123"

# print('s1.join(s2):', s1.join(s2))
# print('s2.join(s1):', s2.join(s1))

"""Method 1"""
encode_output_m1 = ""
for x in encode_arr:
    encode_output_m1 += x + " "

# print(f"This is your morse code: {encode_output_m1[:-1]}")

"""Method 2"""
def str_conversion(arr):
    encode_output_m2 = " "
    return encode_output_m2.join(arr)

# print(f"This is your morse code: {str_conversion(encode_arr)}")

"""Method 3"""
encode_output_m3 = " ".join(encode_arr)
print(f"This is your morse code: {encode_output_m3}")

"""decode"""
decode = input("what do you want to convert to text? ").lower()

decode_arr = decode.split()
# print(decode_arr)

"""method 1"""
text_dic = {y: x for x, y in morse_dic.items()}
# print(text_dic)

decode_output_m1 = ""
for x in decode_arr:
    decode_output_m1 += text_dic[x]

# print(f"This is your text: {decode_output_m1}")

"""method 2"""
def get_key(val):
    for key, value in morse_dic.items():
        if val == value:
            return key

decode_output_m2 = ""
for x in decode_arr:
    decode_output_m2 += get_key(x)

# print(f"This is your text: {decode_output_m2}")

"""method 3"""
key_list = list(morse_dic.keys())
value_list = list(morse_dic.values())
# print(key_list, value_list)

decode_output_m3 = ""
for x in decode_arr:
    position = value_list.index(x)
    char = key_list[position]
    decode_output_m3 += char

print(f"This is your text: {decode_output_m3}")
