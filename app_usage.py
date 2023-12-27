from Xlib import X, display

def get_active_window():
    disp = display.Display()
    root = disp.screen().root
    window_id = root.get_full_property(disp.intern_atom('_NET_ACTIVE_WINDOW'), 0).value[0]

    window = disp.create_resource_object('window', window_id)
    window.change_attributes(event_mask=X.FocusChangeMask)

    try:
        window_name = window.get_full_property(disp.intern_atom('_NET_WM_NAME'), 0).value
    except UnicodeDecodeError:
        window_name = b""

    return window_name.decode('utf-8')

# Beispiel: Drucke den Namen des aktuellen aktiven Fensters
active_window = get_active_window()
print("Aktives Fenster:", active_window)



