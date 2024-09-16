START
   Declarations
      string targetWord = "patriot"     
      string currentWord                

   OUTPUT "Open the dictionary to a random page"
   INPUT currentWord                    

   WHILE currentWord not equal to targetWord
      IF currentWord > targetWord THEN   
         OUTPUT "Flip backwards in the dictionary"
      ELSE IF currentWord < targetWord THEN   
         OUTPUT "Flip forwards in the dictionary"
      ENDIF

      INPUT currentWord                 

   OUTPUT "Found the word '", targetWord, "' in the dictionary!"

STOP