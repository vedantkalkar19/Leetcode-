story = "once upon a time there was a youtuber names harry who uploaded python course with notes"

#string functions

print(len(story))
print(story.endswith("notes"))

print(story.count("s")) # - 4 
print(story.count("wa"))
print(story.count("once"))
print(story.capitalize()) # capitalises 1st letter of the string
print(story.find("who"))
# print(story.find("hary")) -> -1 (not in the sring)

song = "once upon a time there was a youtuber names harry who uploaded python course with notes once"
print(song.find("upon")) # -> 1st occurance
print(story.replace("harry", "codewithharry")) 
# print(song.replace("once", "new line")) replaces all words not only one word