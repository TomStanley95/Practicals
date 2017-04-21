__author__ = 'Tom Stanley'

from Prac07.programming_language import ProgrammingLanguage

ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
vb = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

programming_language = [ProgrammingLanguage("Ruby", "Dynamic", True, 1995),
                        ProgrammingLanguage("Python", "Dynamic", True, 1991),
                        ProgrammingLanguage("Visual Basic", "Static", False, 1991)]

print([str(language) for language in programming_language])
print("The Dynamically Types Languages are:")
for language in programming_language:
    if language.is_dynamic():
        print(language.name)
