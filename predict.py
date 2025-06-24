# predict.py

import os
from typing import Any
import json

# لو عندك مكتبة أو كود خاص لتحليل الرسالة أو جلب السعر ضيفه هنا

# افترض إننا عندنا قاموس ثابت للأسعار للخدمات
from services_data_ready import services
from static_replies_ready import replies, static_prompt

def match_service(user_message: str) -> str:
    # دالة بسيطة تلاقي اسم الخدمة من الرسالة
    for service in services:
        if service["platform"] in user_message.lower() and service["type"] in user_message.lower():
            return f'{service["platform"]} - {service["type"]}'
    return "خدمة غير معروفة"

def get_price(service_name: str) -> str:
    for service in services:
        if service_name == f'{service["platform"]} - {service["type"]}':
            return f'السعر: {service["price"]} جنيه'
    return "السعر غير متاح"

def predict(message: str) -> Any:
    """
    الدالة اللي Replicate بتستخدمها للاستدعاء.
    """
    if not message:
        return "من فضلك اكتب استفسارك عن الخدمة أو السعر."

    service_name = match_service(message)
    price_info = get_price(service_name)

    response = f"✅ الخدمة: {service_name}\n{price_info}\n{replies.get('تأكيد_الطلب', '')}"
    return response
