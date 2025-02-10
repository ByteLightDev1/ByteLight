import tkinter as tk
from ByteLightProject import BinTrig

def on_close(event):
    print("Window closed")

def on_mouse_enter(event):
    print("Mouse entered")

def on_mouse_leave(event):
    print("Mouse left")

def on_fullscreen(event):
    print("Window is fullscreen")

def on_minimized(event):
    print("Window is minimized")

def on_resize(event):
    print(f"Window resized to {event.width}x{event.height}")

def on_key_press(event):
    print(f"Key pressed: {event.keysym}")

def on_focus_gain(event):
    print("Focus gained")

def on_focus_loss(event):
    print("Focus lost")

def on_window_move(event):
    print(f"Window moved to {event.x}, {event.y}")

def on_mouse_press(event):
    print("Mouse button pressed")

def on_mouse_release(event):
    print("Mouse button released")

def on_double_click(event):
    print("Mouse double-clicked")

def on_mouse_motion(event):
    print("Mouse moved")

def on_window_minimized(event):
    print("Window minimized")

def on_window_maximized(event):
    print("Window maximized")

def on_window_restored(event):
    print("Window restored")

def on_scroll(event):
    print("Mouse wheel scrolled")

def on_text_change(event):
    print("Text changed")

def on_focus_on_widget(event):
    print("Widget gained focus")

def on_focus_off_widget(event):
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
