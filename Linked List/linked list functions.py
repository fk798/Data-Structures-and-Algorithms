import DoublyLinkedList

def remove_all(lnk_lst, elem):
    if(lnk_lst.is_empty()):
        return
    cursor = lnk_lst.first_node()
    while(cursor is not lnk_lst.trailer):
        if(cursor.data == elem):
            next_node_saver = cursor.next
            lnk_lst.delete(cursor)
            cursor = next_node_saver
        else:
            cursor = cursor.next


# assumes that lnk_lst is not empty
def max_in_linked_list(lnk_lst):
    return max_in_sublinked_list(lnk_lst, lnk_lst.first_node())

def max_in_sublinked_list(lnk_lst, sublist_head):
    if(sublist_head.next is lnk_lst.trailer):
        return sublist_head.data
    else:
        rest_max = max_in_sublinked_list(lnk_lst, sublist_head.next)
        if(rest_max > sublist_head.data):
            return rest_max
        else:
            return sublist_head.data

