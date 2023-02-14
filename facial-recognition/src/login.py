from base64 import b64decode
import face_recognition as fr
import time
import os
import pickle

def login_check(username, image):
    face_match = 0
    header, encoded = image.split(",", 1)
    file_new = str(time.time_ns())
    file_exist = str(time.time_ns())

    # Write the image as a file with the 'username' we want to try.
    with open(file_new + ".png", "wb") as f:
        f.write(b64decode(encoded))

    # Load the serialized data
    data = pickle.loads(open("data.pickle", "rb").read())

    with open(file_exist + ".png", "wb") as f:
        if(username in data):
            f.write(b64decode(data[username]))
        else: 
            # Remove the file to save space
            os.remove(file_new + ".png")
            os.remove(file_exist + ".png")    
            return "User does not exist!"
    # Crazy TOCTOU bug here between writing the file and using the file. Neat!
    try:
        # Load the image
        try:
            got_image = fr.load_image_file(file_new + ".png")
            existing_image = fr.load_image_file(file_exist + ".png")
        except Exception as e:
            print(e.__cause__)
            return "Data does not exist!"
        
        # Remove the file to save space
        os.remove(file_new + ".png")
        os.remove(file_exist + ".png")     

        # Compare the faces using the ML model
        got_image_facialfeatures = fr.face_encodings(got_image)[0]
        existing_image_facialfeatures = fr.face_encodings(existing_image)[0]
        results = fr.compare_faces([existing_image_facialfeatures], got_image_facialfeatures)

        # If successful login
        if(results[0]):
            # TODO - Add flag here for specific user
            if(username == "nkirkland"):
                return get_flag()

            return "Successfully Logged in!"
        else:
            return "Failed to Log in!"
    except Exception as e:
        print(e.__cause__)
        return "Image not clear! Please try again!"

# Get the flag :) 
def get_flag(): 
	with open('flag.txt') as f:
		contents = f.read()
		return contents	
print(get_flag())