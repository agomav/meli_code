from configuration.configProvider import configurationServer

prop=configurationServer()



current_get_endpoints={"items": prop.getProperty('me_Li_item_api_endpoint'),
                       "categories":prop.getProperty('me_Li_category_api_endpoint'),
                       "currencies":prop.getProperty('me_Li_currency_api_endpoint'), 
                       "users":prop.getProperty('me_Li_user_api_endpoint')}


def _build_items_endpoint(site,identifier):
    base_url=current_get_endpoints.get("items")

    return base_url.replace('{}',site+identifier,1)


def _build_categories_endpoint(category_id):
    base_url=current_get_endpoints.get("categories")
    return base_url.replace('{}',category_id,1)

def _build_currencies_endpoint(currencyid):
    base_url=current_get_endpoints.get("currencies")
    return base_url.replace('{}',str(currencyid),1)

def _build_users_endpoint(userid):
    base_url=current_get_endpoints.get("users")
    return base_url.replace('{}',str(userid),1)

