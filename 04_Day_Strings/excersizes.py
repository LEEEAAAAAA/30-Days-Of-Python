

def abbreviate(word):
    result = ""
    for char in word:
        if char.isupper():
            result += char
        return result


print('Thirty' + ' ' + 'Days' + ' ' + 'Of' + ' ' + "Python")
print("Coding" + "For" + "All")

company = "Coding For All"
print(company)
print(len(company))

print("Upper: " + company.upper())
print("Lower: " + company.lower())
print("Capatalize: " + company.capitalize())
print("Title: " + company.title())
print("Swapcase: " + company.swapcase())

first_word = company[0:6] #0 till 6
print(first_word)

coding_sentence = "Coding For All"
print(coding_sentence.find("Coding"))
print(coding_sentence.replace("Coding", "Python"))

python_sentence = "Python for Everyone"
print(python_sentence.replace("Everyone", "All"))

print(coding_sentence.split(" "))
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(" "))

print(coding_sentence[0])
print(coding_sentence[-1])
print(coding_sentence[10])

abbreviate(coding_sentence)
abbreviate(python_sentence)

index_of_C = coding_sentence.find("C")
index_of_F = coding_sentence.find("F")
last_occurence_of_I = coding_sentence.rindex("I")
first_occurence_of_because = "You cannot end a sentence with because because because is a conjunction".index("because")
last_occurence_of_becuase= "You cannot end a sentence with because because because is a conjunction".rindex("because")

unsliced_phrase = 'You cannot end a sentence with because because because is a conjunction'
sliced_phrase = unsliced_phrase[31:54]
first_occurence_of_because_again = unsliced_phrase.index("because")

print(unsliced_phrase.find("because"))   # 31

start = unsliced_phrase.find("because")
end = unsliced_phrase.rindex("because") + len("because")
print(unsliced_phrase[start:end])          # because because because

print('Coding For All'.startswith("Coding"))
print('Coding For All'.endswith("Coding"))

print('   Coding For All      '.strip)

print("30DaysOfPython").isidentifier() #False, starts with a number
print("thirty_days_of_python").isidentifier() #True

python_lib_list = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
python_libs_with_hash_list = '# '.join(python_lib_list)

newline_aufgabe = "I am enjoying this challenge.\n I just wonder what is next."
print(newline_aufgabe)

print('Name\tAge\tCountry\tCity')
print('Asabeneh\t250\tFinland\tHelsinki')

radius = 10
area = 3.14 * radius ** 2
print(f'The area of a circle with radius {radius} is {area:.0f} meters square.')

a = 8
b = 6
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')