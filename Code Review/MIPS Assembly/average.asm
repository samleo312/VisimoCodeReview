.data
NUM: .float 5
sum: .float 0
tmp: .float 0
Avg: .float 0

i: .float 0

one: .float 1 
promptMessage: .asciiz "Please Enter a Float Value: " 
answerMessage: .asciiz "Average is Equal to "

.text
Main:
	lwc1 $f10, i				# Load initial value for i into $f10
	
	lwc1 $f11, NUM				# Load value of NUM into $f11
	lwc1 $f4, sum
	
	l.s $f31, one				# Load static value of 1 into $f31
	For:
		c.eq.s $f10, $f11		# Conditional : If i becomes equal to Num, exit for loop
		bc1t EndFor
		
		la $a0, promptMessage		# Load address of promptMessage into $a0
		jal PrintString			# Print Prompt Message
		jal GetInput			# Get Float input from user
		add.s $f4, $f4, $f0		# Add input to sum
		
		add.s $f10, $f10, $f31		# Increment by 1
		
		j For				# Jump to begining of for loop
		 
	EndFor:
		swc1 $f4, sum			# Load total sum to memory
		jal Average			# Calculate average
		
		la $a0, answerMessage		# Load address of answer message
		jal PrintString			# Print answer message

		jal PrintFloat			# Print answer
		
#################################################
Average:
	lwc1 $f0, sum		# Load sum from memory into $f0
	lwc1 $f1, NUM		# Load NUM from memory into $f1
	
	div.s $f12, $f0, $f1	# Divide sum by NUM
	jr $ra			# Jump back to main


GetInput:
	li $v0, 6		# Load value for float input into $v0
	syscall			
	
	jr $ra

PrintString:
	li $v0, 4		# Load value for print string into $v0
	syscall
	
	jr $ra


PrintFloat:
	li $v0, 2		# Load value for print float into $v0
	syscall
	
	jr $ra


Exit:
	li $v0, 10		# Load value to exit into $v0
	syscall