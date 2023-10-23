# def encrypt(plain_text,shift_num):
#     cipher_text=""
#     for i in plain_text:
#         position=ltrs.index(i)
#         new_position=position+shift_num
#         if new_position>25:
#             new_position-=26
#         cipher_text+=ltrs[new_position]
#     print(f"The encoded message is {cipher_text}")

# def decrypt(cipher_text,shift_num):
#     plain_text=""
#     for i in cipher_text:
#         position=ltrs.index(i)
#         new_position=position-shift_num
#         if new_position<0:
#             new_position+=26
#         plain_text+=ltrs[new_position]
#     print(f"The decoded message is {plain_text}")

def caesar(start_text,shift_num,cipher_direction):
        end_text=""
        if cipher_direction == 'decode':
                shift_num *=-1
        for i in start_text:
            if i in ltrs:
                position=ltrs.index(i)
                new_position=position+shift_num   
                end_text+=ltrs[new_position]
            else:
                end_text+=i
        print(f"The {cipher_direction}d message is {end_text}")

ltrs=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

   
restart=True
while restart:
    direction=input("Type 'encode' to encrypt, 'decode' to decrypt:\n").lower()
    text=input("Type your message:\n").lower()
    shift=int(input("Type your shift number:\n"))
    shift= shift%26 
    caesar(text,shift,direction)
    re=input("Type 'yes' if you want to go again, Otherwise type 'no'.").lower()
    if re != 'yes':
        restart = False
        print("Goodbye...")
