import joblib

model = joblib.load("marks_model")
hrs = int(input("enter the number of marks you studied"))

p = model.predict([[hrs]])

print(p)
