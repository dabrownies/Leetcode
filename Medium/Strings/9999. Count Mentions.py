"9999. Count Mention"

# You are given two arrays, members and messages. Members contains a list of all Twitter handles, and messages contains
# strings of different messages that can potenially contain Twitter handles from members.

# Return an array with all the Twitter handles from members, and the amount of times they were mentioned in messages.

# A valid mention starts with an '@' symbol and group mentions are valid if they are in this format:
# " Hello @id876,id898,id786 "
# A valid mention followed by commas are considered to be valid mentions as well

# Example 1:

# members = ["id123", "id234", "id7","id321"]
# messages = ["Hey @id123,id321 review this.",
#             "Hey @id7 nice appro@ch!",
#             "@id123,id321 thx!",
#             "@id234 whats up bro",
#             "i h@te you ,,,,,,,@bro",
#             "id123 @id123",
#             "@id7,id7,id7,,,,,,,,,,,@@@@@@@ sndbsjdh , ,,s   ,s, ,ss @, ",
#             "@id989,id234"
#             ]

# Output:
# ['id123 = 3', 'id321 = 2', 'id7 = 4', 'id234 = 2']


def countMentions(members, messages):
    members_set = set(members) # constant look up time
    count = {} # hash map for frequencies

    # first step is to split every single word
    s = [word for message in messages for word in message.split()]
    # isolate mentions by selecting words that start with '@'
    s = [word for word in s if word.startswith('@')]
    # now isolate words by commas to locate potential mention groups
    s = [word for message in s for word in message.split(',')]
    # split by @ symbol to isolate the handle alone, then only select strings that have letters and numbers
    # alternatives: check for words that start with "id" after splitting by '@'
    s = [word for message in s for word in message.split('@') if word.startswith("id")]

    # populate frequency maps
    for word in s:
        if word in members_set:
            count[word] = count.get(word, 0) + 1

    # populate final array
    res = []
    for handle in count:
        res.append(f"{handle} = {count[handle]}")

    return res


# testing
members = ["id123", "id234", "id7","id321"]
messages = ["Hey @id123,id321 review this.",
            "Hey @id7 nice appro@ch!",
            "@id123,id321 thx!",
            "@id234 whats up bro",
            "i h@te you ,,,,,,,@bro",
            "id123 @id123",
            "@id7,id7,id7,,,,,,,,,,,@@@@@@@ sndbsjdh , ,,s   ,s, ,ss @, ",
            "@id989,id234"
            ]

print(countMentions(members, messages))

