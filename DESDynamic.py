class PSTable:
    ipTable = [] # initial permutation // permutasi pertama di awal
    pc1Table = [] # permuted choice 1 // memilih mana kanan dan kiri
                    # hanya 56 bit yang dipilih, sisanya (8 bit) digunakan untuk parity
    pc2Table = [] # permuted choice 2 // memilih 48 dari 56 bit untuk tiap round
    shiftTable = []
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
        convertedString = ''.join([chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8)])
        return convertedString
    def generateRoundKeys(self,key):
        
        # Key into binary
        keyBinary = self.stringToBinary(key)
        pc1_key_str = ''.join(keyBinary[bit - 1] for bit in self.tables.pc1Table)

        
        # Split the 56-bit key into two 28-bit halves
        c0 = pc1_key_str[:28]
        d0 = pc1_key_str[28:]
        round_keys = []
        for round_num in range(16):
            # Perform left circular shift on C and D
            c0 = c0[self.tables.shiftTable[round_num]:] + c0[:self.tables.shiftTable[round_num]]
            d0 = d0[self.tables.shiftTable[round_num]:] + d0[:self.tables.shiftTable[round_num]]
            # Concatenate C and D
            cd_concatenated = c0 + d0

            # Apply the PC2 permutation
            round_key = ''.join(cd_concatenated[bit - 1] for bit in self.tables.pc2Table)

            # Store the round key
            round_keys.append(round_key)
        return round_keys
    def ipPermute(self,binary):
        
        resultTable = [None] * 64
        
        for i in range(64):
            resultTable[i] = binary[self.tables.ipTable[i] - 1]

        # Convert the result back to a string for better visualization
        resultString = ''.join(resultTable)
        
        return resultString
    
    def splitTextToBlocks(self, text):
        blocksAmount = (len(text)//8) + 1
        blocks = []

        for block in range(blocksAmount):
            chunkText = text[:8]
            blocks.append(chunkText)
            text = text[8:]
        return blocks
    
    def encryptLong(self,text,key):
        blocks = self.splitTextToBlocks(text)
        encryptResult = ''
        for block in blocks:
            encryptResult += self.encrypt(block,key)
        return encryptResult

    def decryptLong(self,text,key):
        blocks = self.splitTextToBlocks(text)
        decryptResult = ''
        for block in blocks:
            decryptResult += self.decrypt(block,key)
        return decryptResult
    
    def encrypt(self,text,key):
        binary = self.stringToBinary(text)

        roundKeys = self.generateRoundKeys(key)

        permutedString = self.ipPermute(binary)

        # the initial permutation result is devided into 2 halfs
        lpt = permutedString[:32]
        rpt = permutedString[32:]




        for round_num in range(16):
            # Perform expansion (32 bits to 48 bits)
            expanded_result = [rpt[i - 1] for i in self.tables.eTable]

            # Convert the result back to a string for better visualization
            expanded_result_str = ''.join(expanded_result)

            # Round key for the current round
            round_key_str = roundKeys[round_num]


            xor_result_str = ''
            for i in range(48):
                xor_result_str += str(int(expanded_result_str[i]) ^ int(round_key_str[i]))


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


            # Convert LPT to a list of bits for the XOR operation
            lpt_list = list(lpt)

            # Perform XOR operation
            new_rpt = [str(int(lpt_list[i]) ^ int(p_box_result[i])) for i in range(32)]

            # Convert the result back to a string for better visualization
            new_rpt_str = ''.join(new_rpt)

            # Update LPT and RPT for the next round
            lpt = rpt
            rpt = new_rpt_str

            # Print or use the RPT for each round


        # After the final round, reverse the last swap
        final_result = rpt + lpt

        # Perform the final permutation (IP-1)
        final_cipher = [final_result[self.tables.ipInverseTable[i] - 1] for i in range(64)]

        # Convert the result back to a string for better visualization
        final_cipher_str = ''.join(final_cipher)

        # Print or use the final cipher(binary)
        # print("Final Cipher binary:", final_cipher_str, len(final_cipher_str))


        # Convert binary cipher to ascii
        final_cipher_ascii = self.binaryToString(final_cipher_str)
        
        return final_cipher_ascii
    def decrypt(self, text, key):
        binary = self.stringToBinary(text)
        
        # Initialize lists to store round keys
        roundKeys = self.generateRoundKeys(key)
        
        # Apply Initial Permutation
        permutedString = self.ipPermute(binary)
        
        lpt = permutedString[:32]
        rpt = permutedString[32:]

        for round_num in range(16):
            # Perform expansion (32 bits to 48 bits)
            expanded_result = [rpt[i - 1] for i in self.tables.eTable]
        
            # Convert the result back to a string for better visualization
            expanded_result_str = ''.join(expanded_result)
            # print(expanded_result_str)
            # Round key for the current round
            round_key_str = roundKeys[15-round_num]
        
            # XOR between key and expanded result 
            xor_result_str = ''
            for i in range(48):
                xor_result_str += str(int(expanded_result_str[i]) ^ int(round_key_str[i]))
        
        
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
        
            # Convert the result back to a string for better visualization
            # p_box_result_str = ''.join(p_box_result)
        
            # Convert LPT to a list of bits for the XOR operation
            lpt_list = list(lpt)
        
            # Perform XOR operation
            new_rpt = [str(int(lpt_list[i]) ^ int(p_box_result[i])) for i in range(32)]
        
            # Convert the result back to a string for better visualization
            new_rpt_str = ''.join(new_rpt)
        
            # Update LPT and RPT for the next round
            lpt = rpt
            rpt = new_rpt_str
        
            # Print or use the RPT for each round
        
        final_result = rpt + lpt
        # Perform the final permutation (IP-1)
        final_cipher = [final_result[self.tables.ipInverseTable[i] - 1] for i in range(64)]

        # Convert the result back to a string for better visualization
        final_cipher_str = ''.join(final_cipher)

        # Print or use the final cipher

        # binary cipher string to ascii
        final_cipher_ascii = self.binaryToString(final_cipher_str)
        return final_cipher_ascii


DESObject = DESCipher(ftable)
encryptedRes = DESObject.encryptLong("AKU KAMU AKU KAMU AKU", "MENGAPAA")
decryptedRes = DESObject.decryptLong(encryptedRes, "MENGAPAA")
print(f'Encrypted: {encryptedRes}')
print(f'Decrypted: {decryptedRes}')

