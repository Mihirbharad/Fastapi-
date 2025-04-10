from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel
import razorpay
import hmac
import hashlib

app = FastAPI()

# Razorpay credentials
razorpay_client = razorpay.Client(auth=("rzp_test_26QypB3rHZrlZL", "a6ReEJTcPIhrQolLWM6xp4sG"))

# Request models
class CreateOrderRequest(BaseModel):
    amount: int
    currency: str
    receipt: str

class VerifyOrderRequest(BaseModel): 
    razorpay_order_id: str
    razorpay_payment_id: str
    razorpay_signature: str


# async def create_order(data: CreateOrderRequest):
#     try:
#         options = {
#             "amount": data.amount * 100,  # amount in paise
#             "currency": data.currency,
#             "receipt": data.receipt
#         }
#         order = razorpay_client.order.create(options)
#         return order
#     except Exception as e:
#         print(e)
#         raise HTTPException(status_code=500, detail="Something went wrong while creating order")
 
async def create_order(data: CreateOrderRequest):
    try:
        options = {
            "amount": data.amount,  # ✅ removed * 100 here
            "currency": data.currency,
            "receipt": data.receipt
        }
        order = razorpay_client.order.create(options)
        return order
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Something went wrong while creating order")



async def verify_order(data: VerifyOrderRequest):
    try:
        RMDrXtNPRQu2rELYPFF0Mlblsecret = ""
        generated_signature = hmac.new(
            key=bytes(secret, 'utf-8'),
            msg=bytes(data.razorpay_order_id + "|" + data.razorpay_payment_id, 'utf-8'),
            digestmod=hashlib.sha256
        ).hexdigest()

        if generated_signature == data.razorpay_signature:
            return { "status": "success" }
        else:
            raise HTTPException(status_code=400, detail="Invalid signature")
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Verification failed")