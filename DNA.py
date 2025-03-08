"""
Given a DNA strand, what is its complement?
"""
def bindingStrand(strand):
    mappings = {"A" : "T", "T" : "A",
                "C" : "G", "G" : "C"}
    
    res = []
    for ch in strand:
        res.append(mappings[ch])
    return "".join(res)

print(bindingStrand("AGCC"))