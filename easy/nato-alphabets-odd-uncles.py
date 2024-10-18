#https://www.codingame.com/ide/puzzle/nato-alphabets-odd-uncles

import sys

# Define the different alphabets for each version (1908, 1917, 1927, 1956)
year1 = "Authority, Bills, Capture, Destroy, Englishmen, Fractious, Galloping, High, Invariably, Juggling, Knights, Loose, Managing, Never, Owners, Play, Queen, Remarks, Support, The, Unless, Vindictive, When, Xpeditiously, Your, Zigzag"
year2 = "Apples, Butter, Charlie, Duff, Edward, Freddy, George, Harry, Ink, Johnnie, King, London, Monkey, Nuts, Orange, Pudding, Queenie, Robert, Sugar, Tommy, Uncle, Vinegar, Willie, Xerxes, Yellow, Zebra"
year3 = "Amsterdam, Baltimore, Casablanca, Denmark, Edison, Florida, Gallipoli, Havana, Italia, Jerusalem, Kilogramme, Liverpool, Madagascar, New-York, Oslo, Paris, Quebec, Roma, Santiago, Tripoli, Uppsala, Valencia, Washington, Xanthippe, Yokohama, Zurich"
year4 = "Alfa, Bravo, Charlie, Delta, Echo, Foxtrot, Golf, Hotel, India, Juliett, Kilo, Lima, Mike, November, Oscar, Papa, Quebec, Romeo, Sierra, Tango, Uniform, Victor, Whiskey, X-ray, Yankee, Zulu"

# Organize the years into a list for easy access
cat = [year1.split(", "), year2.split(", "), year3.split(", "), year4.split(", ")]

# Read the input string, split into individual words
a_word_spelled_out = input().split()

# Result array to store the translated words
res = []

# Function to determine the current version and find the corresponding next version
def find_and_translate(a_word_spelled_out):
    # Track potential candidate versions
    possible_versions = [0, 1, 2, 3]
    for word in a_word_spelled_out:
        # For each word, check which version it's from and eliminate others
        for i in reversed(possible_versions):
            if word != cat[i][ord(word[0]) - ord('A')]:
                possible_versions.remove(i)

        # If we narrowed down to one version, calculate the next version
        if len(possible_versions) == 1:
            current_version = possible_versions[0]
            next_version = (current_version + 1) % 4
            # Translate the word using the next version's alphabet
            return [cat[next_version][ord(word[0]) - ord('A')] for word in a_word_spelled_out]

    # If no valid version was found
    return []

# Translate the input word by upgrading to the next version
res = find_and_translate(a_word_spelled_out)

# Join the result into a string and print it
print(" ".join(res))
