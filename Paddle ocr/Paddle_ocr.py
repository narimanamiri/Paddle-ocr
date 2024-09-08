from paddleocr import PaddleOCR  
import cv2  
import pandas as pd  

# Initialize PaddleOCR  
ocr = PaddleOCR(use_angle_cls=True, lang='en')  # Set use_angle_cls=True for better accuracy with rotated text  

# Load the image  
image_path = r'D:\Downloads\Telegram Desktop\tts.png'  # Use raw string notation  
image = cv2.imread(image_path)  

# Check if the image was loaded successfully  
if image is None:  
    print(f"Error: Unable to load image at {image_path}")  
else:  
    # Perform OCR on the image  
    result = ocr.ocr(image_path, cls=True)  

    # Extract text and bounding boxes  
    data = []  
    for line in result:  
        for word_info in line:  
            text = word_info[1][0]  
            data.append(text)  

    # Assuming the table has a fixed number of columns, you can reshape the data  
    # For example, if the table has 3 columns:  
    num_columns = 3  
    table_data = [data[i:i + num_columns] for i in range(0, len(data), num_columns)]  

    # Create a DataFrame  
    df = pd.DataFrame(table_data)  

    # Save the DataFrame to a CSV file  
    df.to_csv('output_table.csv', index=False)  

    print("Table extracted and saved to output_table.csv")