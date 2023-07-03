import os
import openai
from pydantic import BaseModel


class Document(BaseModel):
    prompt: str = ''

def inference(prompt:str)->list:
    openai.organization = "org-iq062ID6BVE1ixIS9w2FuMJM"
    openai.api_key = "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"
    print('[PROCESANDO]'.center(40, '-'))
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": """Eres un profesor de programacion para niños, genera una explicacion para el tema que se te proporciona
        E.G: Programación
        -Es como armar un rompecabezas donde cada pieza forma el sistema completo"""},
            {"role": "user", "content": prompt}
        ]
    )
    print('[SE TERMINO DE PROCESAR]'.center(40, '-'))
    content = completion.choices[0].message.content
    total_tokens = completion.usage.total_tokens
    return [content, total_tokens]