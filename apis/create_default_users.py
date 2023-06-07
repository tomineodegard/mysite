import uuid
import bcrypt
import sqlite3
import pathlib

# ------------------
def get_values_from_dictionary(dictionary):
    values = ""
    for key in dictionary:
        values += f":{key},"
    values.rstrip(",")
    return values.rstrip(",")	


# ------------------ Make the dict to "json"
def dict_factory(cursor, row):
  col_names = [col[0] for col in cursor.description]
  return {key: value for key, value in zip(col_names, row)}


# ------------------ Connect to the database
def db():
  try:
    db = sqlite3.connect(str(pathlib.Path(__file__).parent.parent.resolve())+"/twitter.db") 
    db.row_factory = dict_factory
    db.execute("PRAGMA foreign_keys = ON")
    return db
  except Exception as ex:
    print(ex)
  finally:
    pass

print(bcrypt.hashpw("password".encode("utf-8"), bcrypt.gensalt()))
print(str(uuid.uuid4()).replace("-",""))
# ------------------ Generate default users for the log in credidentials to work with bcrypt (this can not be done through SQL)

user_admin = {
    "user_id": "e39a38e648d044c1b8c2ad3a161486cb",
    "username": "admin",
    "user_email": "admin@gmail.com",
    "user_password": bcrypt.hashpw("password".encode("utf-8"), bcrypt.gensalt()),
    "user_created_at": 1676120649,
    "user_first_name": "Admin",
    "user_last_name": "",
    "user_bio": "",
    "user_is_verified": 1,
    "user_total_followers": 20,
    "user_total_following": 0,
    "user_total_tweets": 0,
    "user_profile_pictrue": "default_avatar.png",
    "user_cover_picture": "",
    "user_is_activated": 1,
    "user_is_active": 2,
    "user_activation_key": str(uuid.uuid4()).replace("-",""),
    "user_reset_password_key": "",
    "user_deactivate_key": "",
}


user_elonmusk = {
    "user_id": "64c3b11f947248719fc0f7e97fb5cdb0",
    "username": "elonmusk",
    "user_email": "elon@gmail.com",
    "user_password": bcrypt.hashpw("password".encode("utf-8"), bcrypt.gensalt()),
    "user_created_at": 1244725452,
    "user_first_name": "Elon",
    "user_last_name": "Musk",
    "user_bio": "",
    "user_is_verified": 1,
    "user_total_followers": 10,
    "user_total_following": 0,
    "user_total_tweets": 0,
    "user_profile_pictrue": "438b092d344d4628a2deafabcf5b0689.jpeg",
    "user_cover_picture": "64786a3347ed463ea198157991fec3f8.jpeg",
    "user_is_activated": 1,
    "user_is_active": 1,
    "user_activation_key": str(uuid.uuid4()).replace("-",""),
    "user_reset_password_key": "",
    "user_deactivate_key": "",
}


user_shakira = {
    "user_id": "24198c66ba294807a26e235e4bc96c2e",
    "username": "shakira",
    "user_email": "shakira@gmail.com",
    "user_password": bcrypt.hashpw("password".encode("utf-8"), bcrypt.gensalt()),
    "user_created_at": 1270991052,
    "user_first_name": "Shakira",
    "user_last_name": "",
    "user_bio": "",
    "user_is_verified": 0,
    "user_total_followers": 0,
    "user_total_following": 0,
    "user_total_tweets": 0,
    "user_profile_pictrue": "a7b0c6fccd3b43009fe43fef8171c62a.jpeg",
    "user_cover_picture": "8581bbd0f24548169c7f2f8c6cc4ac01.jpeg",
    "user_is_activated": 1,
    "user_is_active": 1,
    "user_activation_key": str(uuid.uuid4()).replace("-",""),
    "user_reset_password_key": "",
    "user_deactivate_key": "",
}

user_rihanna = {
    "user_id": "dd41b0e3eeb94f3c9d4304ba44ff198c",
    "username": "rihanna",
    "user_email": "rihanna@gmail.com",
    "user_password": bcrypt.hashpw("password".encode("utf-8"), bcrypt.gensalt()),
    "user_created_at": 1281531852,
    "user_first_name": "Rihanna",
    "user_last_name": "",
    "user_bio": "",
    "user_is_verified": 1,
    "user_total_followers": 10,
    "user_total_following": 0,
    "user_total_tweets": 0,
    "user_profile_pictrue": "49b99d9e2e60478d8eb4ba7358017319.jpeg",
    "user_cover_picture": "84b6d13c1a7a431694013621ff0739fa.jpeg",
    "user_is_activated": 1,
    "user_is_active": 1,
    "user_activation_key": str(uuid.uuid4()).replace("-",""),
    "user_reset_password_key": "",
    "user_deactivate_key": "",
}

user_barackobama = {
    "user_id": "ae0069977acc4a35ae2921e287951068",
    "username": "barackobama",
    "user_email": "barack@gmail.com",
    "user_password": bcrypt.hashpw("password".encode("utf-8"), bcrypt.gensalt()),
    "user_created_at": 1281531852,
    "user_first_name": "Barack",
    "user_last_name": "Obama",
    "user_bio": "",
    "user_is_verified": 0,
    "user_total_followers": 0,
    "user_total_following": 0,
    "user_total_tweets": 0,
    "user_profile_pictrue": "b3aed51663ad43079f44e05d8963d776.jpeg",
    "user_cover_picture": "f60e3019f269420a8d5589222ffd4eff.jpeg",
    "user_is_activated": 1,
    "user_is_active": 1,
    "user_activation_key": str(uuid.uuid4()).replace("-",""),
    "user_reset_password_key": "",
    "user_deactivate_key": "",
}


user_tomineodegard = {
    "user_id": "2f9214d6266e4a96a95bb6a5fb7d1a47",
    "username": "tomineodegard",
    "user_email": "tomineodegard99@gmail.com",
    "user_password": bcrypt.hashpw("password".encode("utf-8"), bcrypt.gensalt()),
    "user_created_at": 1676120649,
    "user_first_name": "Tomine",
    "user_last_name": "Odegard",
    "user_bio": "",
    "user_is_verified": 0,
    "user_total_followers": 2,
    "user_total_following": 0,
    "user_total_tweets": 0,
    "user_profile_pictrue": "b177c43d19354212a90fde1b9992205c.png",
    "user_cover_picture": "72712dce089e487f9c877ff0b39fd03e.jpeg",
    "user_is_activated": 1,
    "user_is_active": 1,
    "user_activation_key": str(uuid.uuid4()).replace("-",""),
    "user_reset_password_key": "",
    "user_deactivate_key": "",
}

user_beyonce = {
    "user_id": "5293c15d99904c6bbb512f8828216486",
    "username": "beyonce",
    "user_email": "beyonce@gmail.com",
    "user_password": bcrypt.hashpw("password".encode("utf-8"), bcrypt.gensalt()),
    "user_created_at": 1676120649,
    "user_first_name": "Beyonce",
    "user_last_name": "",
    "user_bio": "",
    "user_is_verified": 0,
    "user_total_followers": 0,
    "user_total_following": 0,
    "user_total_tweets": 0,
    "user_profile_pictrue": "95eb1075b6ec4804964e14094f8dae46.jpeg",
    "user_cover_picture": "cef45e69e9f64069a6cec9f995fa5c88.jpeg",
    "user_is_activated": 1,
    "user_is_active": 1,
    "user_activation_key": str(uuid.uuid4()).replace("-",""),
    "user_reset_password_key": "",
    "user_deactivate_key": "",
}

user_billgates = {
    "user_id": "999ac9342c79411c9a4800f2af792847",
    "username": "billgates",
    "user_email": "bill@gmail.com",
    "user_password": bcrypt.hashpw("password".encode("utf-8"), bcrypt.gensalt()),
    "user_created_at": 1676120649,
    "user_first_name": "Bill",
    "user_last_name": "Gates",
    "user_bio": "",
    "user_is_verified": 0,
    "user_total_followers": 0,
    "user_total_following": 0,
    "user_total_tweets": 0,
    "user_profile_pictrue": "720e20d964e844b39068767d25e79623.jpeg",
    "user_cover_picture": "9832d0b2a1e94238b4e2993e46a7b069.jpeg",
    "user_is_activated": 1,
    "user_is_active": 1,
    "user_activation_key": str(uuid.uuid4()).replace("-",""),
    "user_reset_password_key": "",
    "user_deactivate_key": "",
}

user_kyliejenner = {
    "user_id": "38ccc0414dcc4aecb72dfa207b947fa1",
    "username": "kyliejenner",
    "user_email": "kylie@gmail.com",
    "user_password": bcrypt.hashpw("password".encode("utf-8"), bcrypt.gensalt()),
    "user_created_at": 1676120649,
    "user_first_name": "Kylie",
    "user_last_name": "Jenner",
    "user_bio": "",
    "user_is_verified": 0,
    "user_total_followers": 0,
    "user_total_following": 0,
    "user_total_tweets": 0,
    "user_profile_pictrue": "a0fbf16e7daa41daa95e95d6f9b54cfb.jpeg",
    "user_cover_picture": "d5f63d5c523b4816a8c2bfe13f4896bd.jpeg",
    "user_is_activated": 1,
    "user_is_active": 1,
    "user_activation_key": str(uuid.uuid4()).replace("-",""),
    "user_reset_password_key": "",
    "user_deactivate_key": "",
}

user_justinbieber = {
    "user_id": "f415ccbd409f4547bf7e263f92e550af",
    "username": "justinbieber",
    "user_email": "justin@gmail.com",
    "user_password": bcrypt.hashpw("password".encode("utf-8"), bcrypt.gensalt()),
    "user_created_at": 1676120649,
    "user_first_name": "Justin",
    "user_last_name": "Bieber",
    "user_bio": "",
    "user_is_verified": 0,
    "user_total_followers": 0,
    "user_total_following": 0,
    "user_total_tweets": 0,
    "user_profile_pictrue": "6b04b05663294572ab43c5982bdfc1f4.jpeg",
    "user_cover_picture": "3a860033043d48da9bb76d68b5023886.jpeg",
    "user_is_activated": 1,
    "user_is_active": 1,
    "user_activation_key": str(uuid.uuid4()).replace("-",""),
    "user_reset_password_key": "",
    "user_deactivate_key": "",
}

user_jeffbezoz = {
    "user_id": "73efc6d9a14f42d4ba7e7f55393efa5c",
    "username": "jeffbezoz",
    "user_email": "jeff@gmail.com",
    "user_password": bcrypt.hashpw("password".encode("utf-8"), bcrypt.gensalt()),
    "user_created_at": 1676120649,
    "user_first_name": "Jeff",
    "user_last_name": "Bezoz",
    "user_bio": "",
    "user_is_verified": 0,
    "user_total_followers": 0,
    "user_total_following": 0,
    "user_total_tweets": 0,
    "user_profile_pictrue": "06d072b8dc624d93bbc39802cd013ab8.jpeg",
    "user_cover_picture": "fecbbd05a777412f8a5e13fd8846825d.jpeg",
    "user_is_activated": 1,
    "user_is_active": 1,
    "user_activation_key": str(uuid.uuid4()).replace("-",""),
    "user_reset_password_key": "",
    "user_deactivate_key": "",
}

user_magnusnielsen = {
    "user_id": "cab56395cdac4755854aad2c50c6f87f",
    "username": "magnusnielsen",
    "user_email": "magnus@gmail.com",
    "user_password": bcrypt.hashpw("password".encode("utf-8"), bcrypt.gensalt()),
    "user_created_at": 1685183698,
    "user_first_name": "Magnus",
    "user_last_name": "Nielsen",
    "user_bio": "",
    "user_is_verified": 0,
    "user_total_followers": 0,
    "user_total_following": 0,
    "user_total_tweets": 0,
    "user_profile_pictrue": "default_avatar.png",
    "user_cover_picture": "",
    "user_is_activated": 1,
    "user_is_active": 1,
    "user_activation_key": str(uuid.uuid4()).replace("-",""),
    "user_reset_password_key": "",
    "user_deactivate_key": "",
}

user_anderstrapman = {
    "user_id": "e3f6b571c7bc41bd8a48ae7b0eea6ed6",
    "username": "anderstrapman",
    "user_email": "anders@gmail.com",
    "user_password": bcrypt.hashpw("password".encode("utf-8"), bcrypt.gensalt()),
    "user_created_at": 1685183698,
    "user_first_name": "Anders",
    "user_last_name": "Trapman",
    "user_bio": "",
    "user_is_verified": 0,
    "user_total_followers": 0,
    "user_total_following": 0,
    "user_total_tweets": 0,
    "user_profile_pictrue": "default_avatar.png",
    "user_cover_picture": "",
    "user_is_activated": 1,
    "user_is_active": 1,
    "user_activation_key": str(uuid.uuid4()).replace("-",""),
    "user_reset_password_key": "",
    "user_deactivate_key": "",
}

user_lasseweber = {
    "user_id": "83dee0051cd140a8a824e4d477e45a2c",
    "username": "lasseweber",
    "user_email": "lasse@gmail.com",
    "user_password": bcrypt.hashpw("password".encode("utf-8"), bcrypt.gensalt()),
    "user_created_at": 1685183698,
    "user_first_name": "Lasse",
    "user_last_name": "Weber",
    "user_bio": "",
    "user_is_verified": 0,
    "user_total_followers": 0,
    "user_total_following": 0,
    "user_total_tweets": 0,
    "user_profile_pictrue": "default_avatar.png",
    "user_cover_picture": "",
    "user_is_activated": 1,
    "user_is_active": 1,
    "user_activation_key": str(uuid.uuid4()).replace("-",""),
    "user_reset_password_key": "",
    "user_deactivate_key": "",
}


user_santiagodonoso = {
    "user_id": "783dc49004524a27b6e0974bdea77069",
    "username": "santiagodonoso",
    "user_email": "santiago@gmail.com",
    "user_password": bcrypt.hashpw("password".encode("utf-8"), bcrypt.gensalt()),
    "user_created_at": 1685183698,
    "user_first_name": "Santiago",
    "user_last_name": "Donoso",
    "user_bio": "",
    "user_is_verified": 0,
    "user_total_followers": 0,
    "user_total_following": 0,
    "user_total_tweets": 0,
    "user_profile_pictrue": "default_avatar.png",
    "user_cover_picture": "",
    "user_is_activated": 1,
    "user_is_active": 1,
    "user_activation_key": str(uuid.uuid4()).replace("-",""),
    "user_reset_password_key": "",
    "user_deactivate_key": "",
}





values = get_values_from_dictionary(user_elonmusk)




db = db()
db.execute(f"INSERT INTO users VALUES({values})", user_admin).rowcount
db.execute(f"INSERT INTO users VALUES({values})", user_elonmusk).rowcount
db.execute(f"INSERT INTO users VALUES({values})", user_shakira).rowcount
db.execute(f"INSERT INTO users VALUES({values})", user_rihanna).rowcount
db.execute(f"INSERT INTO users VALUES({values})", user_barackobama).rowcount
db.execute(f"INSERT INTO users VALUES({values})", user_tomineodegard).rowcount
db.execute(f"INSERT INTO users VALUES({values})", user_beyonce).rowcount
db.execute(f"INSERT INTO users VALUES({values})", user_billgates).rowcount
db.execute(f"INSERT INTO users VALUES({values})", user_kyliejenner).rowcount
db.execute(f"INSERT INTO users VALUES({values})", user_justinbieber).rowcount
db.execute(f"INSERT INTO users VALUES({values})", user_jeffbezoz).rowcount
db.execute(f"INSERT INTO users VALUES({values})", user_magnusnielsen).rowcount
db.execute(f"INSERT INTO users VALUES({values})", user_anderstrapman).rowcount
db.execute(f"INSERT INTO users VALUES({values})", user_lasseweber).rowcount
db.execute(f"INSERT INTO users VALUES({values})", user_santiagodonoso).rowcount


db.commit()
db.close()



