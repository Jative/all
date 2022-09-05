a = input("Введи диапозон, в котором необходимо найти простые числа: ")
x = [str(2)]
for i in range(3, int(a)+1):
    if i%2 == 0:
	    continue
    else:
        for j in range(2, int(i**0.5)+1):
            if i%j == 0:
                break
        else:
            x.append(str(i))
final = ', '.join(x)

s = 0
for number in x:
	s += int(number)

middle = s / len(x)

print(final+".")
print(f"Среднее значение: {str(middle)}.")
input()
