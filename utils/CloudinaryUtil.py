import cloudinary
from cloudinary.uploader import upload

cloudinary.config(
    cloud_name = "dd6pitmvp",
    api_key="763578662464567",
    api_secret="NxeBeM70nasEfqYs4PFMXO52RoI"
)

#util functionn...

async def upload_image(image):
    result = upload(image)
    print("cloundianry response,",result)
    return result["secure_url"] #string
    