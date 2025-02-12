import tkinter as tk
from ByteLightProject import BinTrig

def on_close(event=None):
    print("Window closed")

def on_mouse_enter(event=None):
    print("Mouse entered")

def on_mouse_leave(event=None):
    print("Mouse left")

def on_fullscreen(event=None):
    print("Window is fullscreen")

def on_minimized(event=None):
    print("Window is minimized")

def on_resize(event=None):
    print(f"Window resized to {event.width}x{event.height}")

def on_key_press(event=None):
    print(f"Key pressed: {event.keysym}")

def on_focus_gain(event=None):
    print("Focus gained")

def on_focus_loss(event=None):
    print("Focus lost")

def on_window_move(event=None):
    print(f"Window moved to {event.x}, {event.y}")

def on_mouse_press(event=None):
    print("Mouse button pressed")

def on_mouse_release(event=None):
    print("Mouse button released")

def on_double_click(event=None):
    print("Mouse double-clicked")

def on_mouse_motion(event=None):
    print("Mouse moved")

def on_window_minimized(event=None):
    print("Window minimized")

def on_window_maximized(event=None):
    print("Window maximized")

def on_window_restored(event=None):
    print("Window restored")

def on_scroll(event=None):
    print("Mouse wheel scrolled")

def on_text_change(event=None):
    print("Text changed")

def on_focus_on_widget(event=None):
    print("Widget gained focus")

def on_focus_off_widget(event=None):
    print("Widget lost focus")

root = tk.Tk()
root.title("ByteLightProject Tk Window")

BinTrig().exit(root, on_close)
BinTrig().mouse_in(root, on_mouse_enter)
BinTrig().mouse_out(root, on_mouse_leave)
BinTrig().fullscreen(root, on_fullscreen)
BinTrig().minimized(root, on_minimized)
BinTrig().resize(root, on_resize)
BinTrig().key_press(root, 'a', on_key_press)
BinTrig().focus_gain(root, on_focus_gain)
BinTrig().focus_loss(root, on_focus_loss)
BinTrig().window_move(root, on_window_move)
BinTrig().mouse_button_press(root, '1', on_mouse_press)
BinTrig().mouse_button_release(root, '1', on_mouse_release)
BinTrig().double_click(root, on_double_click)
BinTrig().mouse_motion(root, on_mouse_motion)
BinTrig().window_minimized(root, on_window_minimized)
BinTrig().window_maximized(root, on_window_maximized)
BinTrig().window_restored(root, on_window_restored)
BinTrig().mouse_wheel_scroll(root, on_scroll)
BinTrig().text_change(root, on_text_change)
BinTrig().focus_on_widget(root, on_focus_on_widget)
BinTrig().focus_off_widget(root, on_focus_off_widget)

root.mainloop()
