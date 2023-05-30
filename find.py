from models import Author, Qoutes
import connect

def searh_by_name(arg):
    
    name = arg
    s =[]
    notes = Qoutes.objects()
    for note in notes:
        note.authors.fullname == name
        s.append(note['quote'])
    return s
    
def searh_by_tag(arg):

    tag = arg
    s =[]
    notes = Qoutes.objects()
    for note in notes:
        for i in note.tags:
            if i in tag: 
                s.append(note['quote'])
    return s

def searh_by_tags(arg):

    data = arg
    tags = ''.join(data)
    tags = tags.split(',')
    s =[]
    notes = Qoutes.objects()
    for note in notes:
        for i in note.tags:
            if i in tags: 
                s.append(note['quote'])
    return s

def exit(_):
    return "Good bye!"

HANDLER = {
        
            "name:": searh_by_name,
            "tags:": searh_by_tags,
            "tag:": searh_by_tag,
            "exit": exit
}

def parser(user_input):
    
    user_input = user_input.split()
    
    if len(user_input) == 3:
        cmd, *args = user_input
    else:
        cmd, args = (user_input[0]), user_input[1:]

    try:
        handler = HANDLER[cmd.lower()]
    except KeyError:
        if args:
            cmd = f"{cmd} {args[0]}"
            args = args[1:]
           
        handler = HANDLER[cmd, "Unknown command"]
    return handler, args


def main():
    while True:
        user_input = input()
        handler, *args = parser(user_input)
        
        result = handler(*args)
        
        if not result or result == 'Good bye!':
            print("Good bye!")
            break
        print(result)

            
if __name__ == "__main__":
      main()
   