from view.StartPage import Start_page
def go_to_main_frame(root, userId,frame):
        frame.grid_remove()
        Start_page(root, userId)