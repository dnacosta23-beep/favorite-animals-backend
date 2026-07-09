from flask import Flask, request
from flask_cors import CORS
from dotenv import load_dotenv
from supabase import create_client
import os

load_dotenv()

app = Flask(__name__)
CORS(app)

URL=os.getenv("VITE_SUPABASE_URL")
KEY=os.getenv("VITE_SUPABASE_PUBLISHABLE_KEY")

supabase=create_client(URL,KEY)

@app.route("/")
def home():
    return {"message": "Favorite Animals API is running"}


@app.route("/animals", methods=["GET"])
def get_animals():
    response=supabase.table("animals").select("*").execute()
   
    return response.data 


@app.route("/animals", methods=["POST"])
def add_animal():
    data = request.get_json()

    response = supabase.table("animals").insert(data).execute()


    return response, 201


if __name__ == "__main__":
    app.run(debug=True)