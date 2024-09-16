START
   Declarations
      num targetNumber =    67    
      num guess

   OUTPUT "Guess a number between 1 and 100"

   INPUT guess                    

   WHILE guess not equal to targetNumber
      IF guess > targetNumber THEN
         OUTPUT "Too high, try again"
      ELSE IF guess < targetNumber THEN
         OUTPUT "Too low, try again"
      ENDIF

      INPUT guess                 
   ENDWHILE

   OUTPUT "Congratulations! You guessed the correct number."

STOP
