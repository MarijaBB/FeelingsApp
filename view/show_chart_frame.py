from Chart import Chart

def go_to_chart_frame(root,userId, main_frame):
    Chart(root,userId)
    main_frame.grid_remove()