from view.Login import Login

def go_to_login_page(root,frame):
        frame.grid_remove()
        Login(root)
