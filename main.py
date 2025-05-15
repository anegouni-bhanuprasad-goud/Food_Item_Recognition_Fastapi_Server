from fastapi import FastAPI, UploadFile, File, Depends
from starlette.responses import FileResponse
from typing import Annotated


from database import engine, aws_engine, awsSessionLocal, SessionLocal
import models
from sqlalchemy.orm import Session
from food_model_prediction import predict


app = FastAPI()

def createTables():
    models.Base.metadata.create_all(bind=engine)
    models.Base.metadata.create_all(bind=aws_engine)

createTables()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

def get_aws_db():
    db = awsSessionLocal()
    try:
        yield db
    finally:
        db.close()

aws_db_dependency = Annotated[Session, Depends(get_aws_db)]


@app.get("/")
async def index():
    return FileResponse("index.html")


@app.post("/sendImage")
async def get_image(db : db_dependency, aws_db : aws_db_dependency, file : UploadFile = File(...)):
    try:
        data = await file.read()

        filepath = f"files\\{file.filename}"

        with open(filepath , "wb") as f:
            f.write(data)

        prediction = await predict(filepath)
        new_row =  models.food_images(filename = file.filename, filemime = file.content_type, filepath = filepath, filedata = data, prediction_label = prediction)
        db.add(new_row)
        db.commit()
        db.refresh(new_row)
        print("Done at db1")

        new_row =  models.food_images(filename = file.filename, filemime = file.content_type, filepath = filepath, filedata = data, prediction_label = prediction)
        aws_db.add(new_row)
        aws_db.commit()
        aws_db.refresh(new_row)

        response = {
            "response" : f"The model predicted that the image has {prediction}"
        }

        return response
    
    except Exception as e:
        return {"response" : str(e)}

@app.get("/delete_record")
async def delete_record(db: db_dependency, aws_db : aws_db_dependency, id : int):
    try:
        query = db.query(models.food_images).filter(models.food_images.id == id).first()
        db.delete(query)
        db.commit()
        query2 = aws_db.query(models.food_images).filter(models.food_images.id == id).first()
        aws_db.delete(query2)
        aws_db.commit()
        return {"message" : "Record deleted"}
    
    except Exception as e:
        return {"message" : str(e)}

@app.get("/records")
async def get_records(db : db_dependency):
    try:
        records = db.query(models.food_images).all()
        res =[]
        for record in records:
            res.append({
                "filename" : record.filename ,
                "filemime" : record.filemime ,
                "filepath" : record.filepath ,   
                "prediction_label" : record.prediction_label ,
            })
        return res
    except Exception as e:
        return {"message" : str(e)}
    
@app.get("/aws_records")
async def get_aws_records(aws_db : aws_db_dependency):
    try:
        records = aws_db.query(models.food_images).all()
        res =[]
        for record in records:
            res.append({
                "filename" : record.filename ,
                "filemime" : record.filemime ,
                "filepath" : record.filepath ,
                "prediction_label" : record.prediction_label ,
            })
        return res
    except Exception as e:
        return {"message" : str(e)}
    
@app.get("/reset")
async def reset_db(db : db_dependency, aws_db : aws_db_dependency):
    try:
        models.Base.metadata.drop_all(bind = engine)
        models.Base.metadata.drop_all(bind = aws_engine)

        createTables()

        return {"message" : "Database reset successfully"}
    except Exception as e:
        return {"message" : str(e)}