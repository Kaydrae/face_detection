# Expectations:
# Build a proof of concept program  that when fed a picture file can tell the person's emotions and age.
# You will get more data than just the person's mood and age. Do not filter, modify, or customize this.
# Deliverables:
# Include a short video showing all the functionality and explaining your code.
# Submit this zip file.
# Submit a screenshot of the GitHub repository showing all versions.

from deepface import DeepFace

def deepFace():
    imageSelected = input("Please select image 1-10.")
    if 0 < int(imageSelected) < 11:
        # Create an Object with the results of deep face analyze
        obj = DeepFace.analyze(img_path="images/" + imageSelected + ".jpg",
                               actions=['age', 'gender', 'race', 'emotion'])
        print('Age: ' + str(obj['age']))
        print('Gender: ' + obj['gender'])
        print('Race: ' + obj['dominant_race'])
        print('Emotion: ' + obj['dominant_emotion'])

    else:
        print("Input Not Correct.")


if __name__ == '__main__':
    print("Hello, To The Facial Recognition Implementation Program.\n")
    deepFace()
