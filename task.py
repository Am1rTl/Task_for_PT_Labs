def never_crash(data: str):
	import math
	
	try:
		number, degree, factor = data.split(",")
		number, degree, factor = int(number), int(degree), int(factor)
	except:
		return 0
		
	if number < 0 or number > 100 or degree < 1 or degree > 100  or factor < 0 or factor > 100:
		return 0	
	
	number /= 1
	first_number = number ** degree + factor
	second_number = number ** degree + factor + 1
	
	if str(first_number).find('e') != -1 or str(second_number).find('e') != -1:
		return 0
	
	expression = math.pi / ( first_number - second_number )
	print(f"My calculated expression: {expression}") 
		
while True:
  print("Try crush:")
  never_crash(input())

