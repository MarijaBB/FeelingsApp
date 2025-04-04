from Search import Search

def go_to_search_frame(root,userId, main_frame):
        main_frame.grid_remove()
        Search(root, userId)