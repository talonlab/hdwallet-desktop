def set_red_border(widget):
    widget.setStyleSheet("QGroupBox { border: 1px solid rgba(255,96,96,0.5); }")

def clear_all_borders(group_boxes):
    for widget in group_boxes:
        widget.setStyleSheet("")