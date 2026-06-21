aufg = int(input("Option 1: Nachicht verschluesseln ODER Option 2:Nachicht entschluesseln? SCHREIBE '1' ODER '2'! :"))

if aufg == 1:
   msg = input("Wie lautet deine Nachicht?: ")
   schluessel =int(input("Wie lautet der schluessel?(zwischen 0 und 25): "))
   ceasar_code = ""
   
   if 0 <= schluessel <= 25 :
         for char in msg:
           if char.isalpha():
              code = ord(char)

              if char.isupper():
                 code = (code -ord('A') + schluessel) % 26 + ord('A')
                 ceasar_code += chr(code)
              elif char.islower():
                   code = (code -ord('a') + schluessel) % 26 + ord('a')
                   ceasar_code += chr(code)
           else:
                 ceasar_code += char
         print(f"die verschluesselte Nachicht lautet: {ceasar_code} ")
   else:
    print("inkorekter Schluessel!")

      
elif aufg == 2:
    msg = input("Wie lautet deine geheime Nachicht? : ")
    schluessel = int(input( "Wie lautet der Schluessel?(zwischen 0 und 25): "))
    if 0 <= schluessel <= 25:
        entschluessel = -abs(schluessel)
        ceasar_code = ""

        for char in msg:
            if char.isalpha():
                code = ord(char)

                if char.isupper():
                    code = (code -ord('A') + entschluessel) % 26 + ord('A')
                    ceasar_code += chr(code)
                elif char.islower():
                     code = (code -ord('a') + entschluessel) % 26 + ord('a')
                     ceasar_code += chr(code)
            else:
                   ceasar_code += char

        print(f"die verschluesselte Nachicht lautet: {ceasar_code} ")

    else:
        print("inkorekter Schluessel!")
            
else:
    print("error: Nur '1' oder '2'!")
