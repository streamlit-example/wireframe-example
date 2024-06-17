# 検索
def search(div):
    div.title("Search Commands")
    div.multiselect("Status", options=["just_uploaded", "calculating", "calculated"])
    div.text_input("Name")
    div.text_input("Type")
    div.number_input("Max Size", value=None)
    div.number_input("Min Size", value=None)

    div.title("Reload")
    div.button("Reload Data")
