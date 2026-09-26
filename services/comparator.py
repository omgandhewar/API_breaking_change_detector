from fastapi import FastAPI


def user_compare(old_contract,new_contract):
    breaking_changes=[]
    
    for old_api in old_contract["paths"]:
        if old_api not in new_contract["paths"]:
            breaking_changes.append(f"removed api:{old_api}")
            
    if breaking_changes:
        return{
            "message":"Breaking",
            "changes":breaking_changes
        }       
    
    return {
        "status": "non_breaking",
        "changes": []
    }