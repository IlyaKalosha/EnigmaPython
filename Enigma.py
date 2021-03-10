import random
import string


class Enigma:
    alphabet = ['a', 'b', 'c', 'd', 'e',
                'f', 'g', 'h', 'i', 'j',
                'k', 'l', 'm', 'n', 'o',
                'p', 'q', 'r', 's', 't',
                'u', 'v', 'w', 'x', 'y', 'z']
    rotorI = ['e', 'k', 'm', 'f', 'l', 'g',
              'd', 'q', 'v', 'z', 'n', 't',
              'o', 'w', 'y', 'h', 'x', 'u',
              's', 'p', 'a', 'i', 'b', 'r',
              'c', 'j']

    rotorII = ['a', 'j', 'd', 'k', 's', 'i',
               'r', 'u', 'x', 'b', 'l', 'h',
               'w', 't', 'm', 'c', 'q', 'g',
               'z', 'n', 'p', 'y', 'f', 'v',
               'o', 'e']

    rotorIII = ['b', 'd', 'f', 'h', 'j', 'l',
                'c', 'p', 'r', 't', 'x', 'v',
                'z', 'n', 'y', 'e', 'i', 'w',
                'g', 'a', 'k', 'm', 'u', 's',
                'q', 'o']

    rotorBeta = ['l', 'e', 'y', 'j', 'v', 'c',
                 'n', 'i', 'x', 'w', 'p', 'b',
                 'q', 'm', 'd', 'r', 't', 'a',
                 'k', 'z', 'g', 'f', 'u', 'h',
                 'o', 's']

    rotorGamma = ['f', 's', 'o', 'k', 'a', 'n',
                  'u', 'e', 'r', 'h', 'm', 'b',
                  't', 'i', 'y', 'c', 'w', 'l',
                  'q', 'p', 'z', 'x', 'v', 'g',
                  'j', 'd']

    reflectorB = {'a': 'y', 'y': 'a', 'b': 'r', 'r': 'b',
                  'c': 'u', 'u': 'c', 'd': 'h', 'h': 'd',
                  'q': 'e', 'e': 'q', 'f': 's', 's': 'f',
                  'g': 'l', 'l': 'g', 'i': 'p', 'p': 'i',
                  'j': 'x', 'x': 'j', 'k': 'n', 'n': 'k',
                  'm': 'o', 'o': 'm', 't': 'z', 'z': 't',
                  'v': 'w', 'w': 'v'}

    def encript(self, string, startpos):
        rotor1 = self.rotorI
        rotor2 = self.rotorBeta
        rotor3 = self.rotorGamma
        key = self.__randkey()
        encode_key = ""
        encoded_message = ""

        rotor1, rotor2, rotor3 = self.__rotor_to_start(rotor1, rotor2, rotor3, startpos)
        for letter in key:
            encode_key += self.__get_roters_char(rotor1, rotor2, rotor3, letter)
            rotor1, rotor2, rotor3 = self.__shift_rotors(rotor1, rotor2, rotor3, '131')

        rotor1, rotor2, rotor3 = self.__rotor_to_start(rotor1, rotor2, rotor3, key)
        for letter in string:
            encoded_message += self.__get_roters_char(rotor1, rotor2, rotor3, letter)
            rotor1, rotor2, rotor3 = self.__shift_rotors(rotor1, rotor2, rotor3, '131')

        print(encode_key)
        print(encoded_message)
        result = startpos + encode_key + encoded_message
        return result

    def decript(self, encoded_message):
        startpos = encoded_message[:3]
        key = encoded_message[3:6]
        string = encoded_message[6:]

        rotor1 = self.rotorI
        rotor2 = self.rotorBeta
        rotor3 = self.rotorGamma
        decode_key = ""
        decoded_message = ""

        rotor1, rotor2, rotor3 = self.__rotor_to_start(rotor1, rotor2, rotor3, startpos)
        for letter in key:
            decode_key += self.__get_roters_char(rotor1, rotor2, rotor3, letter)
            rotor1, rotor2, rotor3 = self.__shift_rotors(rotor1, rotor2, rotor3, '131')

        rotor1, rotor2, rotor3 = self.__rotor_to_start(rotor1, rotor2, rotor3, decode_key)
        for letter in string:
            decoded_message += self.__get_roters_char(rotor1, rotor2, rotor3, letter)
            rotor1, rotor2, rotor3 = self.__shift_rotors(rotor1, rotor2, rotor3, '131')
        print(decode_key)
        print(decoded_message)
        return 1

    def __get_roters_char(self, roter1, roter2, roter3, letter):
        index = self.alphabet.index(letter)
        char = roter3[index]
        index = self.alphabet.index(char)
        char = roter2[index]
        index = self.alphabet.index(char)
        char = roter1[index]
        char = self.reflectorB[char]
        index = roter1.index(char)
        char = self.alphabet[index]
        index = roter2.index(char)
        char = self.alphabet[index]
        index = roter3.index(char)
        char = self.alphabet[index]
        return char

    def __shift_rotors(self, rot1, rot2, rot3, pos):
        rot1_str = ''.join(rot1)
        rot2_str = ''.join(rot2)
        rot3_str = ''.join(rot3)
        rot1_str = self.__shift(rot1_str, int(pos[0]))
        rot2_str = self.__shift(rot2_str, int(pos[1]))
        rot3_str = self.__shift(rot3_str, int(pos[2]))
        rot1 = list(rot1_str)
        rot2 = list(rot2_str)
        rot3 = list(rot3_str)
        return rot1, rot2, rot3

    def __rotor_to_start(self, rot1, rot2, rot3, startpos):
        index = rot1.index(startpos[0])
        rot_str = ''.join(rot1)
        rot_str = self.__shift(rot_str, index)
        rot1 = list(rot_str)
        index = rot2.index(startpos[1])
        rot_str = ''.join(rot2)
        rot_str = self.__shift(rot_str, index)
        rot2 = list(rot_str)
        index = rot3.index(startpos[2])
        rot_str = ''.join(rot3)
        rot_str = self.__shift(rot_str, index)
        rot3 = list(rot_str)
        return rot1, rot2, rot3

    def __randkey(self):
        return random.choice(string.ascii_lowercase) \
               + random.choice(string.ascii_lowercase) \
               + random.choice(string.ascii_lowercase)

    def __shift(self, string, n):
        answer = string[n:] + string[:n]
        return answer
