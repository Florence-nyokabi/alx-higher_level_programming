#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def search_replace_elm(elm):
        return (elm if elm != search else replace)
    return list(map(search_replace_elm, my_list))
