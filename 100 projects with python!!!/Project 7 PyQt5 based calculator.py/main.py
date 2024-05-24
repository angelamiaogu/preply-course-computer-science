
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout,QFileDialog

def on_button_click():
    options = QFileDialog.Options()
    file_name, _ = QFileDialog.getOpenFileName(window, 'Open File', '', 'All Files (*);;Images (*.png *.jpg *.jpeg *.bmp *.gif)', options=options)
    if file_name:
        print(f'Selected file: {file_name}')

def on_button2_click():
    print("Button2 clicked!")


# Initialize the application
app = QApplication(sys.argv)

# Create the main window¥
window = QWidget()
window.setWindowTitle('Simple Qt Application')

# Create a vertical layout
layout = QVBoxLayout()

# Create a button and connect its click event
button = QPushButton('upload picture')
button.clicked.connect(on_button_click)


button2 = QPushButton('hahaha')
button2.clicked.connect(on_button2_click)


# Add the button to the layout
layout.addWidget(button)
layout.addWidget(button2)

# Set the layout for the main window
window.setLayout(layout)

# Show the main windowsource 
window.show()

# Run the application's event loop
sys.exit(app.exec_())
