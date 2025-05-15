from database import SessionLocal
import models
from sqlalchemy.orm import Session

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def construct_image(id: int, db: Session):
    try:
        data = db.query(models.food_images.filedata,models.food_images.filename).filter(models.food_images.id == id).first()
        print(f"\nFile with id : {id} exists => {True if data is not None else False}")
        if data is not None:
            raw_hex_str = data[0] 

            if raw_hex_str.startswith('\\x'):
                hex_str = raw_hex_str[2:]
                image_bytes = bytes.fromhex(hex_str)
            else:
                return "\nInvalid format, expected string starting with '\\x'\n"

            with open(f"reconstructed_files\\{data[1]}", "wb") as f:
                f.write(image_bytes)
            return "\nFile Created...\n"

        return "\nEmpty file data...\n"

    except Exception as e:
        return str(e)



while True:
    inp = int(input("Enter the Image Id: "))
    db_generator = get_db()
    db = next(db_generator)
    try:
        print(construct_image(inp, db))
    finally:
        db_generator.close()
