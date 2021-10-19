print("Goog morning.")
print("Goog afternoon.")
print("Goog evening.")

num01 = 123
num02 = 1.23
print(type(num01))
print(type(num02))

string_a = "Hello World."
print(string_a)
print(type(string_a))

a = 10
b = 1
bool01 = (a > b)
print(bool01)
print(type(bool01))

z = ["sato", "suzuki", "takahashi"]
print(z[0])
print(z[1])
print(z[2])

x = 10
y = 2
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)

print(x > y)
print(x < y)

print(x >= 5 and x <= 10)
print(y >= 5 and y <= 10)
print(x >= 5 or x <= 10)
print(y >= 5 or y <= 10)

age = 0

if age >= 10:
  print("adult")
elif age == 0:
  print("baby")
else:
  print("child")

for i in range(5):
  print(i)

for i in range(5):
  if i == 3:
    break
  print(i)

for i in range(5):
  if i == 3:
    continue
  print(i)

for i in range(3):
  for j in range(3):
    print(i, j, sep="-")

arr = [2, 4, 6, 8, 10]
sum = 0
for i in arr:
  sum += i
print(sum)

def say_hello(greeting):
  for i in range(3):
    print(greeting)

say_hello("Hello World")

hello = say_hello
hello("good morning")

def add(num01, num02):
  return(num01 + num02)
print(add(6, 2))

add_result = add(6,2)

def avgnum():
  a = 9 
  b = 4 
  c = 2 
  avg = ((a + b + c) / 3)
  print(avg)
avgnum()

def div(a, b, c):
  return(a+b+c)/3

div_result = div(9, 4, 2)
print(div_result)