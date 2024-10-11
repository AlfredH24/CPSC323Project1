# Alfred Hernandez
import os


#print(os.getcwd())


dict = {
    "for": "keyword",
    "in": "keyword",
    "if": "keyword",
    "def": "keyword",
    "return": "keyword",
    "print": "keyword", 
    "add": "identifier",
    "a": "identifier",
    "b": "identifier",
    "result": "identifier",
    "=": "operator",
    "==": "operator",
    "+": "operator",
    "(": "delimiter",
    ")": "delimiter",
    ":": "delimiter",
    ",": "delimiter",
    "1": "literal",
    "2": "literal",
    "3": "literal",
    "4": "literal",
    "5": "literal",
    "6": "literal",
    "7": "literal",
    "8": "literal",
    "9": "literal",
    "10": "literal",
    '"': "literal",
    "'": "literal",
    "other": "literal",
    "range": "keyword"
}
literals = []
keywords = []
operators = []
identifiers = []
delimiters = []
comments = []
in_string = False
in_comment = False
comment = ""

f = open('case2.txt', 'r')
lines = f.readlines()
f.close()
in_string = False

for line in lines:
    #remove white space
    line = line.lstrip()


    if line.startswith('#'):
        comments.append(line)
        continue
    elif '#' in line:
        i = line.index('#')
        literal = line[i:]
        comments.append(literal)
        line = line[:i]
    print(line)

        #break up each line into words
    words = line.split()
    modified_words = []
    quote = ""
    for word in words:
        if in_comment:
            comment += ' '
            comment += word
            if ((word.startswith('"') and word.endswith('"')) or (word.startswith("'") and (word.endswith("'")))):
                in_comment = False
                comments.append(comment)
            word = ''


        if in_string:
            #print("in string")
            for char in word:
                if char == '"' or char == "'":
                    quote += (char)
                    in_string == False
                    #modified_words.append(word)
                    if word.index(char) < len(word):
                        i = quote.index(char)
                            #split word at index and take whatevers at the end of the quote
                            #print(quote)
                        word = word[-1]
                        literals.append(quote)             
                else:
                    quote += (char)
        #splits : from word
        if word.endswith(":"):
            separator = word[-1]
            word = word[:-1]
            modified_words += separator
            #splits up string if there are ()

        if word.endswith(")"):
            separator = word[-1]
            word = word[:-1]
    
            modified_words += separator
        if "(" in word:
            index = word.index("(")
            wbeforei = word[:index]
            delimiter = word[index]
            
            modified_words += delimiter, wbeforei
            #print(word)
            if (index + 1 == len(word)):
                word = ''
                
            if index < len(word) - 1:
                wafteri = word[index+1:]
                word = wafteri
        if ((word.startswith('"') and word.endswith('"')) or (word.startswith('"') and word.endswith('"'))):
            in_comment = True
            comment += word
            word = ''
        elif (word.startswith("'")) or (word.startswith('"')):
            in_string = True
            for char in word:
                    quote += (char)
            word = ''
        elif word != '':
            #print(word)
            modified_words.append(word)
    


    #print(modified_words)
    for w in modified_words:
        if w in dict:
            if dict[w] == "keyword":
                #print(f"added {w} to keywords")
                keywords.append(w)
            elif dict[w] == "operator":
                #print(f"added {w} to operators")
                operators.append(w)
            elif dict[w] == "delimiter":
                #print(f"added {w} to delimiters")
                delimiters.append(w)
            elif dict[w] == "literal":
                literals.append(w)
        else:
            identifiers.append(w)
            #print(f"added {w} to identifers")
#should be 14 for case 1
#should be 16 for case 2
total_count = 0

total_count += len(keywords)
total_count += len(literals)
total_count += len(operators)
total_count += len(delimiters)
total_count += len(identifiers)
total_count += len(comments)

print(f"total count: {total_count}\n")

literals = list(set(literals))
keywords = list(set(keywords))
operators = list(set(operators))
delimiters = list(set(delimiters))
identifiers = list(set(identifiers))
comments = list(set(comments))

print(f"literals: {literals}\n")
print(f"keywords: {keywords}\n")
print(f"operators: {operators}\n")
print(f"delimiters: {delimiters}\n")
print(f"identifiers: {identifiers}\n")
print(f"comments: {comments}")


    



