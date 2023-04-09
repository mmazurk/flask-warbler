

https://app.quickdatabasediagrams.com/#/


follows
--
user_being_followed_id int PK FK >- users.id
user_following_id int PK FK >- users.id

likes
--
id int PK
user_id int FK >- users.id
message_id int FK >- messages.id

users 
--
id int PK
email text
username text
image_url text
header_image_url text
bio text
location text
password text

messages
--
id int PK
text string(140)
timestamp datetime
user_id int FK >- users.id


