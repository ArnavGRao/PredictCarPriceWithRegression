def feature_engineer(car):
    ## Numerical attributes
    car["mpg"] = (car["citympg"] + car["highwaympg"]) / 2
    car.drop(
        ["citympg", "highwaympg"], axis=1, inplace=True
    )  # They both are strongly correlated so better to merge.

    ## Categorical attributes (Reduce number of attributes for one hot encoding)

    extract_brands_from_car_names(car)
    # Some brands are known for luxury so they might be more expensive
    simplify_brands(car)

    simplify_carbody(car)
    car.drop(
        "enginelocation", axis=1, inplace=True
    )  # Next to no variance. Only one rear and 163 front.
    simplify_enginetype(car)
    simplify_cylindernumber(car)
    simplify_fuelsystem(car)


def extract_brands_from_car_names(car):
    car["CarName"] = car["CarName"].str.split().str[0]
    car.rename(columns={"CarName": "carcompany"}, inplace=True)


def simplify_brands(car):
    keep_list = [
        "toyota",
        "nissan",
        "mazda",
        "volkswagen",
        "mitsubishi",
        "subaru",
        "volvo",
        "honda",
    ]
    car.loc[~car["carcompany"].isin(keep_list), "carcompany"] = "other_company"


def simplify_carbody(car):
    keep_list = [
        "sedan",
        "hatchback",
        "wagon",
    ]
    car.loc[~car["carbody"].isin(keep_list), "carbody"] = "other_body"


def simplify_enginetype(car):
    car.loc[car["enginetype"] != "ohc", "enginetype"] = "other_enginetype"


def simplify_cylindernumber(car):
    keep_list = [
        "four",
        "six",
    ]
    car.loc[~car["cylindernumber"].isin(keep_list), "cylindernumber"] = (
        "other_cylindernumber"
    )


def simplify_fuelsystem(car):
    keep_list = [
        "mpfi",
        "2bbl",
        "idi",
    ]
    car.loc[~car["fuelsystem"].isin(keep_list), "fuelsystem"] = "other_fuelsystem"
