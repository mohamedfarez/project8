import unittest
import tkinter as tk
from unittest.mock import patch
from main import result, reset_all

class TestEmailSlicer(unittest.TestCase):

    def setUp(self):
        self.window = tk.Tk()
        self.entry = tk.Entry(self.window)
        self.text_box = tk.Text(self.window)

    def tearDown(self):
        self.window.destroy()

    @patch('main.entry')
    @patch('main.text_box')
    def test_result_valid_email(self, mock_text_box, mock_entry):
        mock_entry.get.return_value = 'test@example.com'
        result()
        expected_output = 'Email entered was: test@example.com\nYour email username is test\nAnd your email domain server is example.com'
        mock_text_box.delete.assert_called_with('1.0', tk.END)
        mock_text_box.insert.assert_called_with(tk.END, expected_output)
        mock_entry.delete.assert_called_with(0, 'end')

    @patch('main.entry')
    @patch('main.text_box')
    def test_result_invalid_email(self, mock_text_box, mock_entry):
        mock_entry.get.return_value = 'invalidemail'
        result()
        mock_text_box.delete.assert_called_with('1.0', tk.END)
        mock_text_box.insert.assert_called_with(tk.END, 'ERROR!')

    @patch('main.entry')
    @patch('main.text_box')
    def test_reset_all(self, mock_text_box, mock_entry):
        reset_all()
        mock_text_box.delete.assert_called_with('1.0', tk.END)
        mock_entry.delete.assert_called_with(0, 'end')

if __name__ == '__main__':
    unittest.main()
