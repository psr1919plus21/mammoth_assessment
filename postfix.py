import operator

ops = { 
		"+": operator.add,
	 	"-": operator.sub,
	  	"*":operator.mul,
	   	"/":operator.floordiv 
		}  #mapping the string operators to operator function (used in calculate method)

class IllegalExpressionException(Exception):
	"""
	Custom Exception for handling incorrect expressions 
	For Example -
	1. 11++++   --> operators exceeding operands
	2. 11111+-  --> stack list will be left with two or more operand due to less operators    
	"""
	def __init__(self, message):
		super().__init__(message)


def calculate(expr):
	"""
	Calculator function operating on the postfix expression 
	"""
	stack = [] # to store the operands 
	expr_list = expr.split(" ") # spliting the space seperated expression and storing in seperate list
	if (len(expr_list) == 1):
		# space is expected in the expression to differentiate mutiple digit from single digit .e.'22' from '2 2'
		raise IllegalExpressionException("Please separate operators and opreands using spaces.")
	for item in expr_list:
		if(item.isdigit()):				#checking if element in list is digit or operator
			stack.append(int(item))   		#storing operands in stack
		else:
			try:
				operand1 = stack.pop()		
				operand2 = stack.pop() 
				#poping out last two operands whenever operators are encountered
				stack.append(ops[item](operand2, operand1))
			except IndexError as e:
				# checking if operators are more than operand i.e 11++++ , handling exception (pop() from empty list)
				raise IllegalExpressionException("Please check the entered expression") 
				#return ("Please check the entered expression")
	if(len(stack) > 1):
		#checking if operands are more than operator  i.e. 111111+- , it might last with two or more operator in "stack" list
		raise IllegalExpressionException("Please check the entered expression")
	return(stack[0])


def main():
	"""
	Asking for input expression and returning the answer
	"""
	expression = input("Enter expression  ")
	ans = calculate(expression)

	print(ans)

if __name__ == '__main__':
	main()