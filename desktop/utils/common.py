def set_red_border(widget):
    widget.setStyleSheet("QGroupBox { border: 2px solid red; }")

def clear_all_borders(group_boxes):
    for widget in group_boxes:
        widget.setStyleSheet("")