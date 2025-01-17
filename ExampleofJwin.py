  layout = """
+--------+--------+  
|12345678|12345678|  
|12345678|12345678|  
|12345678|12345678|  
+--------+--------+  
"""

# Define widgets with positions and options
widgets_config = [
    {"type": "spinbox", "position": (0, 3), "options": {"min": 1, "max": 10, "id": "spinbox1"}},
    {"type": "progressbar", "position": (3, 2), "options": {"mode": "determinate", "id": "progressbar1"}},
    {"type": "canvas", "position": (2, 2), "options": {"width": 300, "height": 200, "id": "canvas1"}},
    {"type": "listbox", "position": (1, 2), "options": {"values": ["Item 1", "Item 2", "Item 3"], "id": "listbox1"}},
    {"type": "slider", "position": (0, 2), "options": {"min": 0, "max": 100, "id": "slider1"}},
    {"type": "textarea", "position": (3, 1), "options": {"id": "textarea1"}},
    {"type": "radio", "position": (2, 1), "options": {"values": ["Option A", "Option B"], "id": "radio1"}},
    {"type": "dropdown", "position": (1, 1), "options": {"values": ["Option 1", "Option 2"], "id": "dropdown1"}},
    {"type": "checkbox", "position": (0, 1), "options": {"text": "Accept Terms", "id": "checkbox1"}},
    {"type": "password", "position": (3, 0), "options": {"id": "password1"}},
    {"type": "input", "position": (2, 0), "options": {"id": "input1"}},
    {"type": "label", "position": (1, 0), "options": {"text": "This is a label", "id": "label1"}},
    {"type": "button", "position": (0, 0), "options": {"text": "Click Me", "id": "button1"}},
]

# Default callbacks
def button_click_callback():
    print("Button clicked!")
    slider_callback()  # Example of chaining callbacks

def checkbox_callback():
    print("Checkbox state changed!")

def slider_callback():
    slider_value = dynamic_window.get_value("slider1")  # Retrieve slider value dynamically
    print("Slider value:", slider_value)

def spinbox_callback():
    spinbox_value = dynamic_window.get_value("spinbox1")  # Get value from spinbox widget
    print("Spinbox value:", spinbox_value)

def progressbar_callback():
    progress_value = dynamic_window.get_value("progressbar1")  # Get progress from progressbar widget
    print("Progress bar value:", progress_value)

def canvas_callback():
    print("Canvas interaction (e.g., drawing or click) occurred!")

def listbox_callback():
    selected_item = dynamic_window.get_value("listbox1")  # Get selected item from listbox
    print("Listbox selected item:", selected_item)

def textarea_callback():
    text_value = dynamic_window.get_value("textarea1")  # Get text from textarea widget
    print("TextArea content:", text_value)

def radio_callback():
    selected_option = dynamic_window.get_value("radio1")  # Get selected radio button option
    print("Radio button selected option:", selected_option)

def dropdown_callback():
    selected_option = dynamic_window.get_value("dropdown1")  # Get selected dropdown option
    print("Dropdown selected option:", selected_option)

def password_callback():
    password_value = dynamic_window.get_value("password1")  # Get entered password from password field
    print("Password entered:", password_value)

def input_callback():
    input_value = dynamic_window.get_value("input1")  # Get input field value
    print("Input field value:", input_value)

def label_callback():
    print("Label was interacted with!")

# User-defined callback functions for each widget
user_callbacks = {
    "button1": button_click_callback,        # Button callback
    "checkbox1": checkbox_callback,          # Checkbox callback
    "slider1": slider_callback,              # Slider callback
    "spinbox1": spinbox_callback,            # Spinbox callback
    "progressbar1": progressbar_callback,    # Progress bar callback
    "canvas1": canvas_callback,              # Canvas callback
    "listbox1": listbox_callback,            # Listbox callback
    "textarea1": textarea_callback,          # Textarea callback
    "radio1": radio_callback,                # Radio button callback
    "dropdown1": dropdown_callback,          # Dropdown callback
    "password1": password_callback,          # Password callback
    "input1": input_callback,                # Input callback
    "label1": label_callback,                # Label callback
}
