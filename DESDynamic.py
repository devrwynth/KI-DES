class PSTable:
    ipTable = [] # initial permutation // permutasi pertama di awal
    pc1Table = [] # permuted choice 1 // memotong key dari 64 bit ke 56 bit lalu di permute
    pc2Table = [] # permuted choice 2 // compress dan permute key untuk digunakan tiap round
    shiftTable = [] # memutar subkey tiap round ke kiri sebanyak n bit
    eTable = [] # expansion table // expand 32 bit menjadi 48 bit
    sTable = [] # substituion box
    pTable = [] # permutation table // shuffle 32 bit block
    ipInverseTable = [] # inverse of ipTable






# main code
## angka angka dari wikipedia DES Supplementary Material
ftable = PSTable()
ftable.ipTable = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]
ftable.pc1Table = [
    57, 49, 41, 33, 25, 17, 9, 1,
    58, 50, 42, 34, 26, 18, 10, 2,
    59, 51, 43, 35, 27, 19, 11, 3,
    60, 52, 44, 36, 63, 55, 47, 39,
    31, 23, 15, 7, 62, 54, 46, 38,
    30, 22, 14, 6, 61, 53, 45, 37,
    29, 21, 13, 5, 28, 20, 12, 4
]

ftable.pc2Table = [
    14, 17, 11, 24, 1, 5, 3, 28,
    15, 6, 21, 10, 23, 19, 12, 4,
    26, 8, 16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55, 30, 40,
    51, 45, 33, 48, 44, 49, 39, 56,
    34, 53, 46, 42, 50, 36, 29, 32
]

ftable.shiftTable = [1, 1, 2, 2,
                  2, 2, 2, 2,
                  1, 2, 2, 2,
                  2, 2, 2, 1]

ftable.eTable = [
    32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
]

ftable.sTable = [ 

    [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
    ],

    [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
    ],

    [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
    ],

    [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
    ],

    [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
    ],

    [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
    ],

    [
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
    ],

    [
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
    ]
]

ftable.pTable = [
    16, 7, 20, 21, 29, 12, 28, 17,
    1, 15, 23, 26, 5, 18, 31, 10,
    2, 8, 24, 14, 32, 27, 3, 9,
    19, 13, 30, 6, 22, 11, 4, 25
]

ftable.ipInverseTable = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25
]

class DESCipher():
    def __init__(self, tables):
         self.tables = tables
    def stringToBinary(self,string):
        
            binaryString = ''
            
            for char in string:
                # ubah char jadi binary
                binaryChar = format(ord(char), '08b')
                binaryString += binaryChar
                binaryString = binaryString[:64] #truncate
            
            # truncate lalu pad dengan 0
            binaryString = binaryString[:64].ljust(64, '0')
            
            return binaryString

    def binaryToString(self,binary):
        convertedString = ''
        for i in range(0, len(binary), 8):
            byteChunk = binary[i:i+8]
            convertedString += chr(int(byteChunk, 2)) 
        return convertedString
    
    def binaryToHex(self,binary):
        convertedString = ''
        for i in range(0, len(binary), 8):
            byteChunk = binary[i:i+8]
            convertedString += hex(int(byteChunk, 2)) 
        return convertedString
    def generateRoundKeys(self,key):
        
        # dapatkan key dalam bentuk binary dari string key yang diberikan
        keyBinary = self.stringToBinary(key)

        # key dengan index 8,16,24,32,40,48,56, dan 64 di drop lalu dipermute
        # diimplementasikan dengan tabel pc1 yang menyimpan tabel posisi bit setelah drop dan permute
        keypc1 = ''
        for i in self.tables.pc1Table:
            keypc1 += keyBinary[i - 1] 
        
        # split 56 bit tersebut jadi 2 half masing masing 28bit
        keyL = keypc1[:28]
        keyR = keypc1[28:]
        # menyimpan keys yang akan digunakan tiap round
        roundKeys = []
        for round_num in range(16):
            # shift ke kiri sebanyak angka di shift table
            keyL = keyL[self.tables.shiftTable[round_num]:] + keyL[:self.tables.shiftTable[round_num]]
            keyR = keyR[self.tables.shiftTable[round_num]:] + keyR[:self.tables.shiftTable[round_num]]
            keyLR = keyL + keyR

            # compress key dan drop bit index 9, 18, 22, 25, 35, 38, 43, dan 54
            # diimplementasikan menggunakan tabel pc2
            roundKey = ''
            for i in self.tables.pc2Table:
                roundKey += keyLR[i - 1] 

            # masukan ke array
            roundKeys.append(roundKey)
        return roundKeys
    
    def splitTextToBlocks(self, text):
        blocksAmount = (len(text)//8)
        if (len(text)%8 != 0): 
            blocksAmount += 1
        blocks = []

        for block in range(blocksAmount):
            chunkText = text[:8]
            blocks.append(chunkText)
            text = text[8:]
        return blocks
    
    def encryptLong(self,text,key, returnBinary=False):
        blocks = self.splitTextToBlocks(text)
        encryptResult = ''
        for block in blocks:
            encryptResult += self.encrypt(block,key,returnBinary)
        return encryptResult

    def decryptLong(self,text,key, returnBinary=False):
        blocks = self.splitTextToBlocks(text)
        decryptResult = ''
        for block in blocks:
            decryptResult += self.decrypt(block,key,returnBinary)
        return decryptResult
    
    def feistelFunction(self,usedHalf,otherHalf,roundKey):
        # Perform expansion (32 bits to 48 bits)
        expanded_result = [usedHalf[i - 1] for i in self.tables.eTable]

        # Convert the result back to a string for better visualization
        expanded_result_str = ''.join(expanded_result)



        xor_result_str = ''
        for i in range(48):
            xor_result_str += str(int(expanded_result_str[i]) ^ int(roundKey[i]))


        # Split the 48-bit string into 8 groups of 6 bits each
        six_bit_groups = [xor_result_str[i:i+6] for i in range(0, 48, 6)]

        # Initialize the substituted bits string
        s_box_substituted = ''

        # Apply S-box substitution for each 6-bit group
        for i in range(8):
            # Extract the row and column bits
            row_bits = int(six_bit_groups[i][0] + six_bit_groups[i][-1], 2)
            col_bits = int(six_bit_groups[i][1:-1], 2)

            # Lookup the S-box value
            s_box_value = self.tables.sTable[i][row_bits][col_bits]
                
            # Convert the S-box value to a 4-bit binary string and append to the result
            s_box_substituted += format(s_box_value, '04b')

        # Apply a P permutation to the result
        p_box_result = [s_box_substituted[i - 1] for i in self.tables.pTable]

        # # Convert the result back to a string for better visualization
        # p_box_result_str = ''.join(p_box_result)


        # XOR half yang tidak difunctionkan
        xorResult = ''
        for i in range(32):
            xorResult += str(int(otherHalf[i]) ^ int(p_box_result[i]))
        #return hasil
        return xorResult


    def encrypt(self,text,key, returnBinary=False):
        # initial permutation
        binary = self.stringToBinary(text)
        permutedString = ''
        for i in range(64):
            permutedString += binary[self.tables.ipTable[i] - 1] 
        # split menjadi left dan right half
        strL = permutedString[:32]
        strR = permutedString[32:]

        # dapatkan array roundkeys yang akan digunakan
        roundKeys = self.generateRoundKeys(key)

        for round in range(16):
            #jalankan melalui feistel function (F-function)
            cipheredHalf = self.feistelFunction(strR,strL,roundKeys[round])
            strL = strR
            strR = cipheredHalf

        # gabung menjadi satu string agar dapat di inverse
        strRL = strR + strL

        # apply inverse ip dan jadikan string
        encryptedText = ''
        for i in range(64):
            encryptedText += strRL[self.tables.ipInverseTable[i] - 1] 

        # opsi return sebagai binary
        if (not returnBinary):
            encryptedText = self.binaryToString(encryptedText)
        
        return encryptedText
    def decrypt(self, text, key, returnBinary=False):
        # initial permutation
        binary = self.stringToBinary(text)
        permutedString = ''
        for i in range(64):
            permutedString += binary[self.tables.ipTable[i] - 1] 
        # split menjadi left half dan right half
        strL = permutedString[:32]
        strR = permutedString[32:]

        # dapatkan array roundkey yang akan digunakan
        roundKeys = self.generateRoundKeys(key)

        for round in range(16):
            #jalankan melalui feistel function (F-function)
            cipheredHalf = self.feistelFunction(strR,strL,roundKeys[15-round])
            strL = strR
            strR = cipheredHalf
        
        # gabung menjadi satu string agar dapat di inverse
        strRL = strR + strL

        # apply inverse ip dan jadikan string
        decryptedText = ''
        for i in range(64):
            decryptedText += strRL[self.tables.ipInverseTable[i] - 1] 


        # opsi return sebagai binary
        if (not returnBinary):
            decryptedText = self.binaryToString(decryptedText)
        return decryptedText


DESObject = DESCipher(ftable)
encryptedRes = DESObject.encryptLong("halo aku adalah des encryption", "saltsalt")
enBin = DESObject.encryptLong("halo aku adalah des encryption", "saltsalt",True)
decryptedRes = DESObject.decryptLong(encryptedRes, "saltsalt")
print(f'EncryptedHex: {DESObject.binaryToHex(enBin)}')
print(f'Encrypted: {encryptedRes}')
print(f'Decrypted: {decryptedRes}')

