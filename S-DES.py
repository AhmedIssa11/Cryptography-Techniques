Key = (1, 0, 1, 0, 0, 0, 0, 0, 1, 0)
#Key =  (0, 0, 1, 0, 0, 1, 0, 1, 1, 1)
#Key = (1,1,0,0,0,1,1,1,1,0)

Plaintext = (0, 1, 1, 1, 0, 0, 1, 0)
#Plaintext =  (1, 0, 1, 0, 0, 1, 0, 1)
#Plaintext =  (0,0,1,0,1,0,0,0)

IPtable = (2, 6, 3, 1, 4, 8, 5, 7)
FPtable = (4, 1, 3, 5, 7, 2, 8, 6)

P10 = (3, 5, 2, 7, 4, 10, 1, 9, 8, 6)
P8 = (6, 3, 7, 4, 8, 5, 10, 9)
P4 = (2, 4, 3, 1)
EP = (4, 1, 2, 3, 2, 3, 4, 1)

S0table = ((1, 0, 3, 2), (3, 2, 1, 0), (0, 2, 1, 3), (3, 1, 3, 2))
S1table = ((0, 1, 2, 3), (2, 0, 1, 3), (3, 0, 1, 0), (2, 1, 0, 3))

KeyLength = 10
SubKeyLength = 8
DataLength = 8
FLength = 4

# Generate the two sub-keys
def subKeyGen():
    # circular left shift on the first and second five bits
    def leftShift(Key):
        shiftedKey = [None] * KeyLength
        shiftedKey[0:9] = Key[1:10]
        shiftedKey[4] = Key[0]
        shiftedKey[9] = Key[5]
        print("Left Shift:",shiftedKey)
        return shiftedKey

    # P10 Table 
    def P10Table(Key):
        permKeyList = [None] * KeyLength
        for index, elem in enumerate(P10):
          permKeyList[index] = Key[elem - 1]       
        print("Premutation P10:",permKeyList)
        return permKeyList

    # P8 Table 
    def P8Table(Key):
        permKeyList = [None] * DataLength
        for index, elem in enumerate(P8):
          permKeyList[index] = Key[elem - 1]
        print("Premutation P8:",permKeyList)
        return permKeyList
    
    Key1 = P8Table(leftShift(P10Table(Key)))
    print('\u001b[32mKEY 1 ==> %s\033[0m' % Key1) 

    Key2 = P8Table(leftShift(leftShift(leftShift(P10Table(Key)))))
    print('\u001b[32mKEY 2 ==> %s\033[0m' % Key2, "\n")

    return (Key1, Key2)

# Initial Permutation
def intIP(Key):
  permKeyList = [None] * DataLength
  for index, elem in enumerate(IPtable):
    permKeyList[index] = Key[elem - 1]

  print("PlainText:",Plaintext)
  print('\u001b[32mIP: %s\033[0m' % permKeyList, "\n")
  return permKeyList


def encryption():
  def EPfk(Key):
    permKeyList = [None] * DataLength
    for index, elem in enumerate(EP):
      permKeyList[index] = Key[elem - 1]
    print("EP:", permKeyList)
    return permKeyList
  
  def XOR(EP,subKey):
    ans = []
    for i in range(len(subKey)):
        if (EP[i] == subKey[i]):
            ans.append(0)
        else:
            ans.append(1)
    print("XOR with Key:", ans)
    return ans

  def sBoxes(Key):
    S0 = Key[0:4]
    S1 = Key[4:]
    r0 = c0 = r1 = c1 = ""
    r0 = str(S0[0]) + str(S0[-1])
    c0 = str(S0[1]) + str(S0[2])
    r1 = str(S1[0]) + str(S1[-1])
    c1 = str(S1[1]) + str(S1[2])
    print("S0 = %s ==> %s" % (S0table[int(r0,2)][int(c0,2)], bin(S0table[int(r0,2)][int(c0,2)])[2:]), end =" ")
    print("| S1 = %s ==> %s" % (S1table[int(r1,2)][int(c1,2)], bin(S1table[int(r1,2)][int(c1,2)])[2:]))
    print("SBox ==>",str(bin(S0table[int(r0,2)][int(c0,2)])[2:]).zfill(2) + str(bin(S1table[int(r1,2)][int(c1,2)])[2:].zfill(2)))
    return str(bin(S0table[int(r0,2)][int(c0,2)])[2:]).zfill(2) + str(bin(S1table[int(r1,2)][int(c1,2)])[2:].zfill(2))

  # P4 Table 
  def P4Table(Key):
      permKeyList = [None] * FLength
      for index, elem in enumerate(P4):
        permKeyList[index] = int(Key[elem - 1])
      print("Premutation P4:",permKeyList)
      return permKeyList
  
  def Swapping(Key):
      print("After Swapping:", (rightSide + Key),"\n")
      return (rightSide + Key)

  #round 1
  rightSide = IP[4:]
  leftSide = IP[0:4]
 
  print("Right Side:", rightSide)
  r2Input = Swapping(XOR(P4Table(sBoxes(XOR(EPfk(rightSide),subKeys[0]))),leftSide))

  
  #round 2
  print('\033[31m---Round 2---\033[0m') 
  r2Output = XOR(P4Table(sBoxes(XOR(EPfk(r2Input[4:]),subKeys[1]))),r2Input[0:4])
  return (r2Output + r2Input[4:])
  
def FPfk(key):
  permKeyList = [None] * DataLength
  for index, elem in enumerate(FPtable):
    permKeyList[index] = Key[elem - 1]
  print('\u001b[32mFP: %s\033[0m' % permKeyList, "\n")
  return permKeyList

# encryption
print('\033[31mStart the S-DES Algorithm...\033[0m')             
print("The PlainText:", Plaintext)
print("The Original Key:", Key, "\n")

print('\033[31mStep 1: Generating Sub-Keys\033[0m')  
subKeys = subKeyGen()

print('\033[31mStep 2: Initial Permutation\033[0m') 
IP = intIP(Plaintext)

print('\033[31mStep 3: Encryption\033[0m') 
print('\033[31m---Round 1---\033[0m') 

encrypt = encryption()
print("result:", encrypt,"\n")

print('\033[31mStep 4: Final Permutation\033[0m') 
cipher = FPfk(encrypt)


#decryption
print("#"*40)
Plaintext = (0,1,1,1,0,1,1,1) 
print('\033[31mStart the Encryption for S-DES Algorithm...\033[0m')             
print("The Cipher:", Plaintext)
print("The Original Key:", Key, "\n")

print('\033[31mStep 1: Generating Sub-Keys\033[0m')  
subKeys = subKeyGen()
list_x = list(subKeys)
list_x[0], list_x[1] = list_x[1], list_x[0]
subKeys = tuple(list_x)

print('\033[31mStep 2: Initial Permutation\033[0m') 
IP = intIP(Plaintext)

print('\033[31mStep 3: Decryption\033[0m') 
print('\033[31m---Round 1---\033[0m') 

encrypt = encryption()
print("result:", encrypt,"\n")

print('\033[31mStep 4: Final Permutation\033[0m') 
PlainText = FPfk(encrypt)
