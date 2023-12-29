import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image , ImageTk 
from tkinter.filedialog import askopenfilename
import cv2
import numpy as np
import time
import CNNModel 
import sqlite3
#import tfModel_test as tf_test
global fn
fn=""
##############################################+=============================================================
root = tk.Tk()
root.configure(background="seashell2")
#root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Crop Prediction Using Machine Learning")


#430
#++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
img=ImageTk.PhotoImage(Image.open("bg2.jpg"))

img2=ImageTk.PhotoImage(Image.open("bg3.jpg"))

img3=ImageTk.PhotoImage(Image.open("bg4.png"))


logo_label=tk.Label()
logo_label.place(x=0,y=0)

x = 1

# function to change to next image
def move():
	global x
	if x == 4:
		x = 1
	if x == 1:
		logo_label.config(image=img)
	elif x == 2:
		logo_label.config(image=img2)
	elif x == 3:
		logo_label.config(image=img3)
	x = x+1
	root.after(2000, move)


move() 


lbl = tk.Label(root, text="Crop Prediction Using Machine Learning", font=('times', 35,' bold '), height=2, width=60,bg="#8B008B",fg="white")
lbl.place(x=0, y=0)


#frame_display = tk.LabelFrame(root, text=" --Display-- ", width=900, height=250, bd=5, font=('times', 14, ' bold '),bg="lightblue4")
#frame_display.grid(row=0, column=0, sticky='nw')
#frame_display.place(x=300, y=100)

#frame_display1 = tk.LabelFrame(root, text=" --Result-- ", width=900, height=200, bd=5, font=('times', 14, ' bold '),bg="lightblue4")
#frame_display1.grid(row=0, column=0, sticky='nw')
#frame_display1.place(x=300, y=430)

#frame_display2 = tk.LabelFrame(root, text=" --Calaries-- ", width=900, height=50, bd=5, font=('times', 14, ' bold '),bg="lightblue4")
#frame_display2.grid(row=0, column=0, sticky='nw')
#frame_display2.place(x=300, y=380)

frame_alpr = tk.LabelFrame(root, text=" --Process-- ", width=220, height=300, bd=5, font=('times', 14, ' bold '),bg="pink")
frame_alpr.grid(row=0, column=0, sticky='nw')
frame_alpr.place(x=20, y=150)

frame_alpr1 = tk.LabelFrame(root, text=" --Process-- ", width=220, height=150, bd=5, font=('times', 14, ' bold '),bg="pink")
frame_alpr1.grid(row=0, column=0, sticky='nw')
frame_alpr1.place(x=20, y=500)


###########################################################################




###########################################################################
def train_model():
 
    update_label("Model Training Start...............")
    
    start = time.time()

    X= CNNModel.main()
    
    end = time.time()
        
    ET="Execution Time: {0:.4} seconds \n".format(end-start)
    
    msg="Model Training Completed.."+'\n'+ X + '\n'+ ET

    print(msg)

import functools
import operator


def convert_str_to_tuple(tup):
    s = functools.reduce(operator.add, (tup))
    return s

def test_model_proc(fn):
    from keras.models import load_model
    from keras.optimizers import Adam

#    global fn
    
    IMAGE_SIZE = 100
    LEARN_RATE = 1.0e-4
    CH=3
    print(fn)
    if fn!="":
        # Model Architecture and Compilation
       
        model = load_model('C:/Users/nikha/Downloads/crop_plant updated/crop_plant/soil_model_cnn.h5')
            
        # adam = Adam(lr=LEARN_RATE, beta_1=0.9, beta_2=0.999, epsilon=None, decay=0.0)
        # model.compile(optimizer=adam, loss='categorical_crossentropy', metrics=['accuracy'])
        
        img = Image.open(fn)
        img = img.resize((IMAGE_SIZE,IMAGE_SIZE))
        img = np.array(img)
        
        img = img.reshape(1,IMAGE_SIZE,IMAGE_SIZE,3)
        
        img = img.astype('float32')
        img = img / 255.0
        print('img shape:',img)
        prediction = model.predict(img)
        print(np.argmax(prediction))
        brain=np.argmax(prediction)
        print(brain)
        
        
        
        if brain == 0:
            Cd="Black Soil"
            _label = tk.Label(root, text="Crop List: \n  Kharif Season (June to October):\n 25°-35° C:Cotton,Soyabean,Pegion Pea \n 20°-30° C:Groundnut,spinach,fenugreek \n 15°-25° C :Sesame,Cluster Beans\n Rabi Season (November to March): \n Wheat, Gram, Mustard \n Zaid Season (March to June): \n Cucumber,Watermelon,Muskmelon", width=48, font=("bold", 15), bg='black', fg='white')
            _label.place(x=515, y=500)
        elif brain == 1:
            Cd="Alluvial Soil"
            _label = tk.Label(root, text="Crop List: \n Suitable Temperature is 20°C to 27°C \n rice, wheat, sugarcane:25°C to 35°C, tobacco, cotton, \n soybean, oilseeds", width=48, font=("bold", 25), bg='black', fg='white')
            _label.place(x=515, y=500)
        elif brain ==2:
            Cd="Laterite Soil"
            _label = tk.Label(root, text="Crop List: \n Suitable Temperature is 14°C to 36°C \n tea, coffee, rubber, cinchona, coconut, areca nut", width=48, font=("bold", 25), bg='black', fg='white')
            _label.place(x=515, y=500)
        elif brain ==3:
            Cd="Yellow Soil"
            _label = tk.Label(root, text="Crop List: \n Suitable Temperature is 15°C to 20°C \n potato, oilseeds, pulses, millets, fruits, vegetables", width=48, font=("bold", 25), bg='black', fg='white')
            _label.place(x=515, y=500)
        elif brain ==4:
            Cd="Sandy Soil"
            _label = tk.Label(root, text="Crop List: \n Suitable Temperature is 10°C to 19°C \n Carrots, Radishes, Potatoes, Lettuce, Tomatoes, , Corn, Watermelon, Beans, and Cucumber.", width=48, font=("bold", 25), bg='black', fg='white')
            _label.place(x=515, y=500)
       
       
        A=Cd
        return A

# def clear_img():
    
#     img11 = tk.Label(frame_display, background='lightblue4',width=160,height=120)
#     img11.place(x=0, y=0)







def update_label(str_T):
    #clear_img()
    result_label = tk.Label(root, text=str_T, width=25, height=1, font=('times', 30,' bold '), bg='goldenrod', fg='black')
    result_label.place(x=450, y=380)
# def train_model():
    
#     update_label("Model Training Start...............")
    
#     start = time.time()

#     X=Model_frm.main()
    
#     end = time.time()
        
#     ET="Execution Time: {0:.4} seconds \n".format(end-start)
    
#     msg="Model Training Completed.."+'\n'+ X + '\n'+ ET

#     update_label(msg)

def test_model():
    global fn
    if fn!="":
        update_label("Model Testing Start...............")
        
        start = time.time()
    
        X=test_model_proc(fn)
        
        X1="Selected Image is {0}".format(X)
        
        end = time.time()
            
        ET="Execution Time: {0:.4} seconds \n".format(end-start)
        
        msg='\n'+ X1 + '\n'
        fn=""
    else:
        msg="Please Select Image For Prediction...."
        
    update_label(msg)
    

def openimage():
   
    global fn
    fileName = askopenfilename(initialdir='C:/Users/nikha/Downloads/crop_plant updated/crop_plant', title='Select image for Aanalysis ',
                               filetypes=[("all files", "*.*")])
    IMAGE_SIZE=200
    imgpath = fileName
    fn = fileName


#        img = Image.open(imgpath).convert("L")
    img = Image.open(imgpath)
    
    img = img.resize((IMAGE_SIZE,200))
    img = np.array(img)
#        img = img / 255.0
#        img = img.reshape(1,IMAGE_SIZE,IMAGE_SIZE,3)


    x1 = int(img.shape[0])
    y1 = int(img.shape[1])


#
#        gs = cv2.cvtColor(cv2.imread(imgpath, 1), cv2.COLOR_RGB2GRAY)
#
#        gs = cv2.resize(gs, (x1, y1))
#
#        retval, threshold = cv2.threshold(gs, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    im = Image.fromarray(img)
    imgtk = ImageTk.PhotoImage(im)
    img = tk.Label(root, image=imgtk, height=250, width=250)
    
    #result_label1 = tk.Label(root, image=imgtk, width=250,height=250)
    #result_label1.place(x=300, y=100)
    img.image = imgtk
    img.place(x=300, y=100)
   # out_label.config(text=imgpath)

def convert_grey():
    global fn    
    IMAGE_SIZE=200
    
    img = Image.open(fn)
    img = img.resize((IMAGE_SIZE,200))
    img = np.array(img)
    
    x1 = int(img.shape[0])
    y1 = int(img.shape[1])

    gs = cv2.cvtColor(cv2.imread(fn, 1), cv2.COLOR_RGB2GRAY)

    gs = cv2.resize(gs, (x1, y1))

    retval, threshold = cv2.threshold(gs, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    print(threshold)

    im = Image.fromarray(gs)
    imgtk = ImageTk.PhotoImage(image=im)
    
    #result_label1 = tk.Label(root, image=imgtk, width=250, font=("bold", 25), bg='bisque2', fg='black',height=250)
    #result_label1.place(x=300, y=400)
    img2 = tk.Label(root, image=imgtk, height=250, width=250,bg='white')
    img2.image = imgtk
    img2.place(x=580, y=100)

    im = Image.fromarray(threshold)
    imgtk = ImageTk.PhotoImage(image=im)

    img3 = tk.Label(root, image=imgtk, height=250, width=250)
    img3.image = imgtk
    img3.place(x=880, y=100)
    #result_label1 = tk.Label(root, image=imgtk, width=250,height=250, font=("bold", 25), bg='bisque2', fg='black')
    #result_label1.place(x=300, y=400)


#################################################################################################################
def window():
    root.destroy()


def livecam() :
    import cv2

    # Create a VideoCapture object
    cap = cv2.VideoCapture(0)

    # Check if the camera is opened successfully
    if not cap.isOpened():
        print("Failed to open the camera")
        exit()

    # Create a function to handle button press event
    def capture_image():
        # Read the current frame from the camera
        ret, frame = cap.read()

        if ret:
            # Save the frame as an image file
            cv2.imwrite("captured_image.jpg", frame)
            print("Image captured successfully!")
        else:
            print("Failed to capture image")

    # Create a named window to display the captured frame
    cv2.namedWindow("Camera")

    while True:
        # Read the current frame from the camera
        ret, frame = cap.read()

        if ret:
            # Display the frame in the named window
            cv2.imshow("Camera", frame)

        # Wait for a key press
        key = cv2.waitKey(1)

        # Check if the 'c' key is pressed (for capturing image)
        if key == ord('c'):
            capture_image()
        # Check if the 'q' key is pressed (for quitting the program)
        elif key == ord('q'):
            break

    # Release the VideoCapture object and destroy the windows
    cap.release()
    cv2.destroyAllWindows()
    #############################################################################
def temperature():
    import tkinter as tk
    import requests
    import json
    import webbrowser

    API_KEY = "5549adb13e3815dd78cdec57835b881c"  # Replace with your OpenWeatherMap API key
    CITY_NAME = "Pune"  # Replace with the desired city name
    
    

    def fetch_weather():
        url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = json.loads(response.text)
        temperature = data["main"]["temp"] if "main" in data and "temp" in data["main"] else "N/A"
        return temperature

    def open_weather_widget():
        widget_url = "https://openweathermap.org/city/" + CITY_NAME.lower().replace(" ", "")
        webbrowser.open(widget_url)

    # Create the GUI window
    window = tk.Tk()
    window.title("Weather Widget")
    img=ImageTk.PhotoImage(Image.open("sun.jpg"))
    # Create a label for displaying the weather information
    weather_label = tk.Label(window, text="Fetching weather data...")
    weather_label.pack()

    # Create a button to open the weather widget in a browser
    #widget_button = tk.Button(window, text="Open Weather Widget", command=open_weather_widget)
    #widget_button.pack()

    def update_weather():
        temperature = fetch_weather()
        weather_label.config(text="Temperature: " + str(temperature) + "°C")

        # Schedule the next weather update after a delay (in milliseconds)
        window.after(60000, update_weather)  # Update every minute (60000 milliseconds)

    # Start the initial weather update
    update_weather()

    # Start the GUI event loop
    root.mainloop()


############################################################################
def location():
   
    import geocoder

    def get_current_location():
        g = geocoder.ip('me')
        return g.city

    #def fetch_temperature():
        # Replace with your logic to fetch the temperature from an API or other sources
    #    temperature = "N/A"
     #   return temperature

    # Create the GUI window
    window= tk.Tk()
    window.title("Weather App")

    # Create a label for displaying the current location
    location_label = tk.Label(window, text="Current Location: ")
    location_label.pack()

    # Create a label for displaying the current temperature
    #temperature_label = tk.Label(window, text="Current Temperature: ")
    #temperature_label.pack()

    def update_weather():
        # Update the current location and temperature labels
        location = get_current_location()
       # temperature = fetch_temperature()
        location_label.config(text="Current Location: " + location)
        #temperature_label.config(text="Current Temperature: " + temperature)

        # Schedule the next weather update after a delay (in milliseconds)
        window.after(60000, update_weather)  # Update every minute (60000 milliseconds)

    # Start the initial weather update
    update_weather()
    

    # Start the GUI event loop
    root.mainloop()
def place():
    from subprocess import call
    call(["python","tnl1.py"])

button1 = tk.Button(frame_alpr, text=" Select_Image ", command=openimage,width=15, height=1, font=('times', 15, ' bold '),bg="maroon",fg="white")
button1.place(x=10, y=60)

button2 = tk.Button(frame_alpr, text="Image_preprocess", command=convert_grey, width=15, height=1, font=('times', 15, ' bold '),bg="maroon",fg="white")
button2.place(x=10, y=115)

button4 = tk.Button(frame_alpr, text="Live Cam", command=livecam, width=15, height=1, font=('times', 15, ' bold '),bg="maroon",fg="white")
button4.place(x=10, y=10)


#button2 = tk.Button(frame_alpr, text="Open_Cam", command=convert_grey, width=15, height=1, font=('times', 15, ' bold '),bg="maroon",fg="white")
#button2.place(x=10, y=10)

# button4 = tk.Button(frame_alpr, text="Train Model", command=train_model, width=12, height=1, font=('times', 15, ' bold '),bg="white",fg="black")
 #button4.place(x=10, y=240)

button3 = tk.Button(frame_alpr, text="CNN_Prediction", command=test_model,width=15, height=1,bg="maroon",fg="white", font=('times', 15, ' bold '))
button3.place(x=10, y=165)
#
#
#button5 = tk.Button(frame_alpr, text="button5", command=window,width=8, height=1, font=('times', 15, ' bold '),bg="yellow4",fg="white")
#button5.place(x=450, y=20)
button11 = tk.Button(frame_alpr1, text=" Current Location ", width=15,command=place, height=1, font=('times', 15, ' bold '),bg="maroon",fg="white")
button11.place(x=10, y=30)

button22 = tk.Button(frame_alpr1, text="Temperature", width=15,command= temperature, height=1, font=('times', 15, ' bold '),bg="maroon",fg="white")
button22.place(x=10, y=80) 

exit = tk.Button(frame_alpr, text="Exit", command=window, width=15, height=1, font=('times', 15, ' bold '),bg="red",fg="white")
exit.place(x=10, y=220)



root.mainloop()