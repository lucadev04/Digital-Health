from Xlib import X, display


def get_active_app():
    disp = display.Display()
    root = disp.screen().root
    window_id = root.get_full_property(disp.intern_atom('_NET_ACTIVE_WINDOW'), 0).value[0]

    window = disp.create_resource_object('window', window_id)
    window.change_attributes(event_mask=X.FocusChangeMask)

    try:
        appname = window.get_full_property(disp.intern_atom('WM_CLASS'), 0).value
        appname = appname.decode('utf-8', errors='ignore')
        appname_new = appname.replace('\x00', '/')

    except UnicodeDecodeError:
        appname = b""

    return(str(appname_new).split('/')[0])

