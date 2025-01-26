cd ~/Code/MCB185/data
gunzip -c dictionary.gz | grep "r" | grep  "^[oncaizr]*$" | grep -E "^.{4,}$"

#Previous ideas left for future reference

#gunzip -c ~/Code/MCB185/dictionary.gz | grep "r" | grep  "^[oncaizr]*$" | grep -E "^.{4,}$"

#R appears in every word
#ONCAIZ appears as other letters
#Word must be 4 characters long

#gunzip -c dictionary.gz | grep "r" | grep "[oncaiz]"
#gunzip -c dictionary.gz | grep "r" | grep "^[oncaizr]*$" | grep -E "[oncaizr]{4,}[oncaizr]"
