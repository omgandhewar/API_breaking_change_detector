from fastapi import FastAPI


def user_compare(old_contract,new_contract):
    breaking_changes=[] 
    
    for path, method in old_contract["paths"].items():
        if path not in new_contract["paths"]:
            breaking_changes.append(f"removed api:{path}")
            continue
        
        for method1 in method.keys():
            if method1 not in new_contract["paths"][path]:
                breaking_changes.append(f"removed method {method1} in {path}")
                   
    print("paths:",path)
    print("method:",method)
         
    if breaking_changes:
        return{
            "status":"breaking",
            "changes":breaking_changes
        }
        
    return {
        "status": "non_breaking",
        "changes": []
    }