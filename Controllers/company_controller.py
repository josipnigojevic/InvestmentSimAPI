from Services.company_service import get_company_info

def get_company_information(symbol):
    company_info = get_company_info(symbol)
    if company_info:
        return company_info, 200
    return {"error": "Company information not found."}, 404