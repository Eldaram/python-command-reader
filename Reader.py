class Reader(object):
    """docstring for Reader"""
    def __init__(self):
        super(Reader, self).__init__()
        self.cmds = {}
        
    """
    It read a string command and execute it, if it returns somthing, it will return it AND print it
    """
    def read(str):
        pass

    """
    It add a cmd to cmds
    """
    def add_cmds(name, func, args_min, is_text):
        cmds[name] = (func,args_min,is_text)