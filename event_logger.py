from datetime import datetime
import os

import openpyxl

class EventLogger:
    """Create the xlsx file and log the events."""
    def __init__(self):
        os.makedirs('logs',exist_ok=True)
        now = datetime.now()
        date_str = now.strftime("%Y%m%d_%H%M")
        
        self.row_count = 2
        self.book = openpyxl.Workbook()
        sheet = self.book.active
        sheet['A1'] = 'Captured Time'
        sheet['B1'] = 'Exported File'

        self.export_file = f'logs/{date_str}.xlsx'

        
    def event_logging(self,capture_time, capture_file):
        """Log the captured events."""
        sheet = self.book.active
        sheet[f'A{self.row_count}'] = capture_time
        sheet[f'B{self.row_count}'] = capture_file
        self.row_count += 1
        
                
    def close(self):
        """Save and close the xlsx file."""
        self.book.save(self.export_file)
        self.book.close()
