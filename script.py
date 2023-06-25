from flask import Flask, render_template, request
import numpy as np
from scipy import signal

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    # Get the signal data from the form
    signal_data = request.form['signal']

    # Convert the string input to a NumPy array
    signal_array = np.array(list(map(float, signal_data.split(','))))

    # Apply a signal processing operation (e.g., filtering)
    filtered_signal = signal.medfilt(signal_array)

    # Convert the filtered signal back to a string
    filtered_signal_data = ','.join(map(str, filtered_signal))

    return render_template('result.html', signal=signal_data, filtered_signal=filtered_signal_data)

if __name__ == '__main__':
    app.run(debug=True)
