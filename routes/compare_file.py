from fastapi import FastAPI, APIRouter
from services.comparator import user_compare
from utils.loader import load_json_file


router=APIRouter()

@router.post("/compare")
def compare():
    old_contract=load_json_file("app/contract/old_openapi.json")
    new_contract=load_json_file("app/contract/new_openapi.json")
    
    return user_compare(old_contract,new_contract)