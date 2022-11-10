.data
N: .word 5
Result: .word 0
A: .word 1,2,3,4,5

.text

Main:
	lw $a1, N # Load N into $a1 register
	jal Calc # Jump to Calc function

	sw $v0, Result # Store final result to memory location of Result

	li $v0, 10 # Load value to terminate program into $v0
	syscall # syscall to terminate program



Calc:
	li $t1, 0 # i
	li $t2, 0 # S
	la $t3, A # Address of A
	addi $a1, $a1, 1 # Add one to N to account for i being equal to N
	For:
		beq $t1, $a1, ExitFor # If i becomes equal to N + 1, jump to ExitFor
		lw $t4, 0($t3) # Load next value of A into $t4
		mul $t5, $t4, $t1 # Multiply next value of A times i
		add $t2, $t2, $t5 # Add product of previous calculation to S
		
		addi $t1, $t1, 1 # Increment I by 1
		addi $t3, $t3, 4 # Increment to next element in A
		
		j For # Jump to beginning of loop
		
	ExitFor:
	add $v0, $v0, $t2	# Store final value of S into $v0
	jr $ra # Jump Back to Main
		