str1 = "Hello, World..!"
str2 = "Python is fun."

#length of string
print(str1, str2)
print("index 1 character: " + str1[1])
print(f"The length of str1 is {len(str1)}")

#replace string
new_str = str1.replace("o","*0")
print("new string is: " + new_str)

#Split string
new_str1 = str1.split(",")
print("split string with comma:- " + str(new_str1))

#concatenate string
Str3 = str1 + "," + str2
print("concatenated String: " + Str3)

text = "Movie 'Home Alone' is my favourite movie"
#we can use slash instead of quotes.
text1 = "Movie \"Home Alone\" is my favourite movie"
print (text1)