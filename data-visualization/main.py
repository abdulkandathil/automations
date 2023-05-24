import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QDateEdit, QLabel, QPushButton
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import pandas as pd
from datetime import datetime, date

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Read the CSV file into a pandas DataFrame
        self.data = pd.read_csv('temperatures.csv')

        # Create a Figure object and a Canvas
        self.fig = Figure(figsize=(5, 4), dpi=100)
        self.canvas = FigureCanvas(self.fig)

        # Create an axis
        self.ax = self.fig.add_subplot(111)

        # Create date range selection widgets
        start_label = QLabel('Start Date:')
        self.start_date_edit = QDateEdit()
        end_label = QLabel('End Date:')
        self.end_date_edit = QDateEdit()
        self.update_button = QPushButton('Update')
        self.update_button.clicked.connect(self.update_plot)

        # Create a QVBoxLayout and add the widgets to it
        layout = QVBoxLayout()
        layout.addWidget(start_label)
        layout.addWidget(self.start_date_edit)
        layout.addWidget(end_label)
        layout.addWidget(self.end_date_edit)
        layout.addWidget(self.update_button)
        layout.addWidget(self.canvas)

        # Create a central widget and set the layout
        central_widget = QWidget()
        central_widget.setLayout(layout)

        # Set the central widget of the main window
        self.setCentralWidget(central_widget)

        # Show the main window
        self.show()

    def update_plot(self):
        # Get the selected start and end dates
        start_date = self.start_date_edit.date().toPyDate()
        end_date = self.end_date_edit.date().toPyDate()

        # Convert start_date and end_date to pandas datetime objects
        start_date = pd.to_datetime(start_date)
        end_date = pd.to_datetime(end_date)

        # Filter the data based on the selected date range
        filtered_data = self.data[
            (pd.to_datetime(self.data['Date']) >= start_date) &
            (pd.to_datetime(self.data['Date']) <= end_date)
        ]

        # Clear the existing plot
        self.ax.clear()

        # Plot the filtered data
        self.ax.plot(filtered_data['Date'], filtered_data['Temperature'])
        self.ax.set_xlabel('Date')
        self.ax.set_ylabel('Temperature')
        self.ax.set_title('Temperature Variation')

        # Redraw the canvas
        self.canvas.draw()


if __name__ == '__main__':
    # Create the application and the main window
    app = QApplication(sys.argv)
    window = MainWindow()

    # Start the event loop
    sys.exit(app.exec_())
