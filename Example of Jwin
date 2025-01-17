  layout = """
  +--------+--------+
  |12345678|12345678|
  |12345678|12345678|
  |12345678|12345678|
  +--------+--------+
  """

  widgets_config = [
    {"type": "button", "position": (0, 0), "options": {"text": "Click Me", "id": "button1"}},
    {"type": "input", "position": (1, 0), "options": {"id": "input1"}},
    {"type": "checkbox", "position": (2, 0), "options": {"text": "Accept Terms", "id": "checkbox1"}},
    {"type": "dropdown", "position": (0, 1), "options": {"values": ["Option 1", "Option 2", "Option 3"], "id": "dropdown1"}},
    {"type": "textarea", "position": (1, 1), "options": {"id": "textarea1"}},
    {"type": "slider", "position": (2, 1), "options": {"min": 0, "max": 100, "id": "slider1"}},
  ]

  def button_click_callback():
    print("Button clicked! Running custom callback...")

  def checkbox_callback():
      print("Checkbox state changed!")

  def slider_callback():
      slider_value = dynamic_window.get_value("slider1")
      print("Slider value:", slider_value)

  user_callbacks = {
      "button1": button_click_callback,
      "checkbox1": checkbox_callback,
      "slider1": slider_callback,
  }
