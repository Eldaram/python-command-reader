class Reader(object):
    """docstring for Reader"""
    def __init__(self):
        super(Reader, self).__init__()
        self.cmds = {}
        self.not_in_cmds = ""
        
    """
    It read a string command and execute it, if it returns somthing, it will return it AND print it
    """
    def read(self, string):
        sliced_str = string.split()
        if len(sliced_str) != 0 and sliced_str[0] in self.cmds:
            args_need = sliced_str[1:self.cmds[sliced_str[0]][1]]
            args_supp = sliced_str[self.cmds[sliced_str[0]][1]+1:]
            if not self.cmds[sliced_str[0]][2]:
                return self.cmds[sliced_str[0]][0](args_need,args_supp)
            else :
                txt = ""
                for x in args_supp:
                    txt += " " + x
                return self.cmds[sliced_str[0]][0](args_need,txt[1:])
        elif self.not_in_cmds != "":
            print(self.not_in_cmds)
            return self.not_in_cmds
        else :
            print("This is not a command.")
            return "This is not a command."

    """
    It add a cmd to cmds
    cmd added to cmds MUST have the following form : cmd([must_arg_list], followed_string OR [followed_arg_list])
    func is a function / args_min is a number / is_text is a boolean
    """
    def add_cmds(self, name, func, args_min, is_text):
        if " " in name:
            print("Error Reader.add_cmds, name should not contain spaces")
        else :
            self.cmds[name] = (func,args_min,is_text)