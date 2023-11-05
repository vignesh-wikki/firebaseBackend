import uvicorn
import pyrebase
from fastapi import FastAPI, HTTPException
from fastapi.requests import Request
from pydantic import BaseModel
import os
from google.cloud import firestore


app = FastAPI(
 description="user managment system",
 title="auth",
 docs_url="/"
)

import firebase_admin
from firebase_admin import credentials,auth,firestore as firestores



if not firebase_admin._apps:
    cred = credentials.Certificate("serviceAccountKey.json")
    firebase_admin.initialize_app(cred)

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "serviceAccountKey.json"
firebaseConfig = {
  "apiKey": "",
  "authDomain": "",
  "projectId": "",
  "storageBucket": "",
  "messagingSenderId": "",
  "appId": "",
  "measurementId": "",
  "databaseURL":""
#leave this databaseURL emapty string 
}
firebase = pyrebase.initialize_app(firebaseConfig)

#schemahttps://github.com/vignesh-wikki/firebaseBackend.git
class registerModel(BaseModel):
    email:str
    fullname:str
    username:str
    password:str


class loginModel(BaseModel):
    email:str
    password:str

@app.post('/register')
async def register(userData:registerModel):
    email=userData.email
    password=userData.password
    fullname=userData.fullname
    username=userData.username

    try:
        user = auth.create_user(
            email = email,
            password = password
        )
        db = firestores.client()
        user_ref = db.collection("users").document(user.uid)
        user_ref.set({
            "email": email,
            "fullname": fullname,
            "username":username,
            "created_at": firestore.SERVER_TIMESTAMP
        })

        return {"message": "User registered successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail="Error: " + str(e))
    


@app.post('/login')
async def login(userData:loginModel):
  email=userData.email
  password=userData.password

  try:
      user = firebase.auth().sign_in_with_email_and_password(
          email,
          password 
      )

      token = user['idToken']
      return {"message": "Logined successfully","token":token}
  except Exception as e:
    raise HTTPException(status_code=401, detail="Login failed: " + str(e))
      


@app.post('/profile')
async def get_profile(request: Request):
    try:
       
        headers = request.headers
        jwt = headers.get("authorization")
        user = auth.verify_id_token(jwt)
        db = firestores.client()
        user_data_ref = db.collection("users").document(user['uid'])
        user_data = user_data_ref.get().to_dict()
        if user_data:
            return user_data
        else:
            raise HTTPException(status_code=404, detail="User not found")

    except Exception as e:
        raise HTTPException(status_code=400, detail="Error: " + str(e))



@app.put('/update')
async def update_profile(request: Request, data: dict):
    try:
      
        headers = request.headers
        jwt = headers.get("authorization")

     
        user = auth.verify_id_token(jwt)

      
        db = firestore.Client()

       
        user_data_ref = db.collection("users").document(user["uid"])
        user_data_ref.update(data)

        return {"message": "Profile updated successfully"}

    except Exception as e:
        raise HTTPException(status_code=400, detail="Error: " + str(e))


@app.delete('/delete')
async def delete_profile(request: Request):
    try:
       
        headers = request.headers
        jwt = headers.get("authorization")

  
        user = auth.verify_id_token(jwt)

  
        db = firestore.Client()

       
        user_data_ref = db.collection("users").document(user['uid'])
        user_data_ref.delete()

        return {"message": "Profile deleted successfully"}

    except Exception as e:
        raise HTTPException(status_code=400, detail="Error: " + str(e))

if __name__=="__main__":
    uvicorn.run("main:app",reload=True)